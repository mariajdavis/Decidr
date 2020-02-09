from flask import Flask, jsonify, render_template
from filter import get_model
import pandas as pd
from getter import get_list

app = Flask(__name__, template_folder="templates",
            static_folder="static", static_url_path="")
MODEL = get_model()
MOVIES = pd.read_csv('dataset//movies.csv')


# Valid user_ids: 13 and 276
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
    lst = [MOVIES.query(f'Id=={i}')['Title']._values[0] for i in movie_list]
    return jsonify(lst)


@app.route("/")
def pls_work():
    return render_template("index.html")


@app.route("/login")
def login():
    return render_template("elements.html")

@app.route('/sliders/<uid>')
def sliders(uid):



if __name__ == '__main__':
    app.run(debug=True)
