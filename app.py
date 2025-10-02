from flask import Flask, render_template, request
from berea.bible import BibleClient


app = Flask(__name__)


@app.route("/index/")
def index():
    return render_template('search_form.html')
    # TODO: Render results underneath the search form (fetch?)


# TODO: Condition search method on provided query params
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
    # TODO: Build results description
    
    # TODO: Validate inputs/input combinations
    if book and chapter:
        verse_records = bible.search_chapter(phrase, book, chapter)
    elif book:
        verse_records = bible.search_book(phrase, book)
    elif testament:
        verse_records = bible.search_testament(phrase, testament.lower())
    else:
        verse_records = bible.search_bible(phrase)
    
    context = {
        'translation': translation,
        'phrase': phrase,
        'verse_records': verse_records,
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
