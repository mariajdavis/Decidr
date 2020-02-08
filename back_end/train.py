import pandas as pd
import numpy as np
from surprise import KNNBaseline


def get_trained_model(dataset):
    # To use item-based cosine similarity
    sim_options = {
        "name": "msd",
        "user_based": False,  # Compute  similarities between items
    }
    model = KNNBaseline(sim_options=sim_options)

    training_set = dataset.build_full_trainset()
    model.fit(training_set)
    return model
