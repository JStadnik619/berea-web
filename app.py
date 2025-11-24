import logging
from textwrap import dedent

from flask import Flask, render_template, request
from berea.bible import BibleClient, BibleInputError


logger = logging.getLogger(__name__)


app = Flask(__name__)


@app.route("/")
def index():
    # TODO: Render input options with available translations, books, chapters
    return render_template('search_form.html')


@app.route("/search")
def search():
    # TODO: Required inputs
    translation = request.args.get('translation')
    phrase = request.args.get('phrase')
    
    # Optional inputs
    book = request.args.get('book')
    chapter = request.args.get('chapter')
    testament = request.args.get('testament')
    
    bible = BibleClient(translation)
    
    verse_records = []
    results_description = ""
    
    try:
        
        # TODO: Validate inputs/input combinations
        if book and chapter:
            verse_records = bible.search_chapter(phrase, book, chapter)
            book_name = bible.get_book_from_abbreviation(book)
            results_description = f"{len(verse_records)} occurrences of '{phrase}' in {book_name} {chapter} ({translation})"
        elif book:
            verse_records = bible.search_book(phrase, book)
            book_name = bible.get_book_from_abbreviation(book)
            results_description = f"{len(verse_records)} occurrences of '{phrase}' in {book_name} ({translation})"
        elif testament in ['New Testament', 'Old Testament']:
            verse_records = bible.search_testament(phrase, 'nt' if testament == 'New Testament' else 'ot')
            results_description = f"{len(verse_records)} occurrences of '{phrase}' in the {testament} ({translation})"
        else:
            verse_records = bible.search_bible(phrase)
            results_description = f"{len(verse_records)} occurrences of '{phrase}' in the {translation} Bible"
    
    except BibleInputError as bible_ex:
        return render_template('search_error.html', error_msg=str(bible_ex))
    
    except Exception as ex:
        input_msg = dedent(f"""
            User provided invalid search input:
            {phrase=}
            {book=}
            {chapter=}
            {testament=}\n
        """)
        logger.exception(input_msg)
        logger.exception(ex)
        return render_template('search_error.html', error_msg='Invalid input.')
    
    context = {
        'translation': translation,
        'phrase': phrase,
        'verse_records': verse_records,
        'results_description': results_description,
    }
    return render_template('search_results.html', **context)


@app.route("/reference/<translation>/<book>/<chapter>/<verse>")
def reference(translation, book, chapter, verse):
    bible = BibleClient(translation)
    chapter_verses = bible.get_verses_by_chapter(book, chapter)
    context = {
        'translation': translation,
        'book': book,
        'chapter': chapter,
        'chapter_verses': chapter_verses,
        'verse_number': verse,
    }
    # TODO: render 404 for invalid input
    # TODO: Anchor to specific verse
    return render_template('reference_passage.html', **context)
