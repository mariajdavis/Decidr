import pandas as pd
import numpy as np


def get_list(user_id, model, movie_data):
    """ returns a list of recommended movies """
    movie_list = []

    while len(movie_list) < 10:

        random_movie = movie_data.sample(1)
        movie_id = random_movie['Id'].values[0]

        rating_object = model.predict(user_id, movie_id)
        rating = rating_object.est
        # movie_id = rating_object.iid

        if rating >= 4:
            movie_list.append(movie_id)

    return movie_list
