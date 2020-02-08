from flask import Flask, jsonify
import json
from filter import get_trained_model
import pandas as pd

app = Flask(__name__)
MODEL = get_trained_model()
MOVIES = pd.read_csv('dataset//movies.csv')


@app.route('/<user_id>/<mood>/<company>')
def send_all(user_id, mood, company):
    """ endpoint: takes HTTP request and return movie recommendation(s) """
    movie_recommendation = ["movie1", "movie2"]
    return jsonify(movie_recommendation)


if __name__ == '__main__':
    app.run(debug=True)
