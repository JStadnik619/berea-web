from flask import Flask, render_template
from berea.bible import BibleClient


app = Flask(__name__)


@app.route("/")
def john_3_16():
    bible = BibleClient('KJV')
    verse_records = bible.get_verse('john', '3', '16')
    for verse in verse_records:
        return verse['text']


# TODO:
# @app.route("/search/") should display the search form
# def search():


@app.route("/search/<translation>/<phrase>")
def search_bible(translation, phrase):
    bible = BibleClient(translation)
    verses = bible.search_bible(phrase)
    return render_template('search_results.html', verse_records=verses)
