from flask import Flask, jsonify, render_template
from filter import get_model
import pandas as pd
from getter import get_list

import request

app = Flask(__name__, template_folder="templates", static_folder="static")
MODEL = get_model()
MOVIES = pd.read_csv('dataset//movies.csv')


@app.route('/<user_id>/<mood>/<company>')
def send_all(user_id, mood, company):
    movie_list = list()
    mood = int(mood)
    company = int(company)
    user_id = int(user_id)

    if mood == 0 and company == 0:
        movie_list = get_list(user_id*100+0, MODEL, MOVIES)
    elif mood == 0 and company == 1:
        movie_list = get_list(user_id*100+1, MODEL, MOVIES)
    if mood == 0 and company == 2:
        movie_list = get_list(user_id*100+2, MODEL, MOVIES)
    if mood == 1 and company == 0:
        movie_list = get_list(user_id*100+3, MODEL, MOVIES)
    if mood == 1 and company == 1:
        movie_list = get_list(user_id*100+4, MODEL, MOVIES)
    if mood == 1 and company == 2:
        movie_list = get_list(user_id*100+5, MODEL, MOVIES)

    """ endpoint: takes HTTP request and return movie recommendation(s) """
    lst = [int(i) for i in movie_list]
    return jsonify(lst)


if __name__ == '__main__':
    app.run(debug=True)
