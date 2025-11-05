from flask import Flask, render_template, request
from berea.bible import BibleClient


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
    fts = request.args.get('full-text')
    
    bible = BibleClient(translation)
    
    verse_records = []
    results_description = ""
    
    # TODO: Validate inputs/input combinations
    if book and chapter:
        verse_records = bible.search_chapter(phrase, book, chapter, fts)
        book_name = bible.get_book_from_abbreviation(book)
        results_description = f"{len(verse_records)} occurrences of '{phrase}' in {book_name} {chapter} ({translation})"
    elif book:
        verse_records = bible.search_book(phrase, book, fts)
        book_name = bible.get_book_from_abbreviation(book)
        results_description = f"{len(verse_records)} occurrences of '{phrase}' in {book_name} ({translation})"
    elif testament in ['New Testament', 'Old Testament']:
        verse_records = bible.search_testament(phrase, 'nt' if testament == 'New Testament' else 'ot', fts)
        results_description = f"{len(verse_records)} occurrences of '{phrase}' in the {testament} ({translation})"
    else:
        verse_records = bible.search_bible(phrase, fts)
        results_description = f"{len(verse_records)} occurrences of '{phrase}' in the {translation} Bible"
    
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
