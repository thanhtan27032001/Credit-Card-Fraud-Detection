import pandas as pd


def read_raw_dataset():
    raw_df = pd.read_csv('creditcard.csv')
    return raw_df
