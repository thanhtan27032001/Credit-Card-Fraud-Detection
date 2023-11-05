from matplotlib import pyplot as plt
import seaborn as sns
from IPython.display import Image

import numpy as np
import pandas as pd
import seaborn as sns
import plotly.express as px
from matplotlib import pyplot as plt
from sklearn.model_selection import cross_val_score

from sklearn import metrics
from collections import Counter

import read_dataset
import preprocessing
import feature_scaling
import baseline_model
from sklearn.model_selection import train_test_split

if __name__ == '__main__':
    # read dataset
    raw_df = read_dataset.read_raw_dataset()

    # preprocess
    numeric_columns = (list(raw_df.loc[:, 'V1':'Amount']))
    df = preprocessing.remove_duplicated_rows_and_outliers(raw_df=raw_df, numeric_columns=numeric_columns)

    # split dataset
    X = df.drop('Class', axis=1)
    y = df['Class']
    X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.3, random_state=42)

    # feature scaling
    col_names = ['Amount']
    X_train = feature_scaling.standard_scaler(X_train, col_names)
    X_test = feature_scaling.standard_scaler(X_test, col_names)

    # baseline model
    baseline_model.train(x_train=X_train, y_train=y_train)
