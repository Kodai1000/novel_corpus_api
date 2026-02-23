from utils.base_dir import get_base_data_dir
import json
from sqlalchemy import create_engine, select, and_, or_
from sqlalchemy.orm import sessionmaker
from typus.co_occurrence import co_occurrence
import jaconv
from flask import jsonify
import Levenshtein

"""
db_path = get_base_data_dir() / "data/db/words_data.db"
engine = create_engine(f"sqlite:///{db_path.as_posix()}")

SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()
"""

def co_occurrence_query(db, identifier, dep, word, minimum_count):
    result = db.session.scalars(
        select(co_occurrence).where(
            co_occurrence.identifier == identifier,
            co_occurrence.dep == dep,
            co_occurrence.count >= int(minimum_count),
            or_(
                co_occurrence.head_word == word,
                co_occurrence.target_word == word
            )
            
        )
    )
    result_rows = result.all()
    print("head word sample is ", result_rows[0].head_word)

    returned_json = []
    for row in result_rows:
        returned_json.append(row.to_json())


    return jsonify(returned_json)

def get_word_Levenstein_distance_from_reading_or_lemma(keyword, lemma, reading):
    Levenshtein_distance_in_lemma = Levenshtein.distance(keyword, lemma)
    Levenshtein_distance_in_reading = Levenshtein.distance(keyword, reading)
    if Levenshtein_distance_in_lemma <= Levenshtein_distance_in_reading:
        return Levenshtein_distance_in_lemma
    else:
        return Levenshtein_distance_in_reading

def search_word_in_co_occurrence(db, identifier, keyword):
    katakana = jaconv.hira2kata(keyword)

    result_rows = db.session.scalars(
        select(co_occurrence).where(
            and_(
                co_occurrence.identifier == identifier,
                or_(
                    co_occurrence.head_word == keyword,
                    co_occurrence.head_reading == katakana,
                    co_occurrence.head_word.contains(keyword),
                    co_occurrence.head_word.contains(katakana),
                    co_occurrence.target_word.contains(keyword),
                    co_occurrence.target_reading.contains(katakana),
                ),
            )
        )
    )
    result_array = []
    for row in result_rows:
        result_array.append([row.to_json()["head_word"], get_word_Levenstein_distance_from_reading_or_lemma(keyword, row.to_json()["head_word"], row.to_json()["head_reading"])])       
        result_array.append([row.to_json()["target_word"], get_word_Levenstein_distance_from_reading_or_lemma(keyword, row.to_json()["target_word"], row.to_json()["target_reading"])])
        
    sorted_list = sorted(list(set(tuple(x) for x in result_array)), key=lambda x: x[1])
    return jsonify(sorted_list)