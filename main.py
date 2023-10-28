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

if __name__ == '__main__':
    raw_df = pd.read_csv('creditcard.csv')

    labels = ["Genuine", "Fraud"]

    fraud_or_not = raw_df["Class"].value_counts().tolist()
    values = [fraud_or_not[0], fraud_or_not[1]]

    fig = px.pie(values=raw_df['Class'].value_counts(),
                 names=labels,
                 width=700,
                 height=400,
                 color_discrete_sequence=["skyblue", "black"],
                 title="Fraud vs Genuine transactions")
    fig.show()

    plt.figure(figsize=(3, 4))
    ax = sns.countplot(x='Class', data=raw_df)
    for i in ax.containers:
        ax.bar_label(i, labels=raw_df['Class'].value_counts().tolist())
