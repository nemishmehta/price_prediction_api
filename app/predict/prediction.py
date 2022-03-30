import pickle
import pandas as pd


def prediction(prepped_df):
    """
    Use model and prepped dataframe to predict property price
    """

    model = pickle.load(open('model/model.pkl', 'rb'))

    price = round(model.predict(prepped_df)[0], 2)

    return price