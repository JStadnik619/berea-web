from flask import Flask, render_template
from berea.bible import BibleClient


app = Flask(__name__)


@app.route("/")
def index():
    return "Welcome to Berea"


# TODO:
# @app.route("/search/") should display the search form
# def search():


@app.route("/search/<translation>/<phrase>")
def search_bible(translation, phrase):
    bible = BibleClient(translation)
    verses = bible.search_bible(phrase)
    context = {
        'translation': translation,
        'verse_records': verses,
    }
    # TODO: Render results underneath the search form (fetch?)
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
