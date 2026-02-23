from flask import Flask
from utils.get_datas import co_occurrence_query, search_word_in_co_occurrence
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config.from_object('config')
app.json.ensure_ascii = False
db = SQLAlchemy(app)

@app.route('/')
def index():
    return "Hello, this is the Novel Corpus API. Documents are from Aozora Bunko."

@app.route('/co_occurrence/<identifier>/<dep>/<word>/<minimum_count>')
def get_co_occurrence(identifier, dep, word, minimum_count):
    return co_occurrence_query(db, identifier, dep, word, minimum_count)

@app.route('/get_relative_words/<identifier>/<keyword>')
def get_relative_words(identifier, keyword):
    return search_word_in_co_occurrence(db, identifier, keyword)

if __name__ == "__main__":
    app.run(debug=True, port=8888, threaded=True)  