import pandas as pd
from surprise import Dataset, Reader

from train import get_trained_model


def get_model():
    df = pd.read_csv("dataset//training_data.csv")
    reader = Reader(rating_scale=(1, 5))

    data = Dataset.load_from_df(df[["user", "item", "rating"]], reader)

    model = get_trained_model(data)
    return model
