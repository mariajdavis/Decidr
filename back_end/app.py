from flask import Flask, jsonify
import json

app = Flask(__name__)


@app.route('/<user_id>/<mood>/<company>')
# def hello_world():
#     return "Hello, World!"
def send_all(user_id, mood, company):
    """ endpoint: takes HTTP request and return movie recommendation(s) """
    movie_recommendation = ["movie1", "movie2"]
    return jsonify(movie_recommendation)


if __name__ == '__main__':
    app.run(debug=True)
