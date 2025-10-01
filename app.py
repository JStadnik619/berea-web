from flask import Flask
from berea.bible import BibleClient


app = Flask(__name__)

@app.route("/")
def john_3_16():
    bible = BibleClient('KJV')
    verse_records = bible.get_verse('john', '3', '16')
    for verse in verse_records:
        return verse['text']
