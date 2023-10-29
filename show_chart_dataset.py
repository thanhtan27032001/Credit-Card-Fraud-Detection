import pandas as pd
import seaborn as sns
import plotly.express as px
from matplotlib import pyplot as plt


def show_dataset_ratio():
    # raw_df = pd.read_csv('creditcard.csv')

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


# checking boxplots
def boxplots_custom(dataset, columns_list, rows, cols, suptitle):
    fig, axs = plt.subplots(rows, cols, sharey=True, figsize=(15,25))
    fig.suptitle(suptitle,y=1, size=25)
    axs = axs.flatten()
    for i, data in enumerate(columns_list):
        sns.boxplot(data=dataset[data], orient='h', ax=axs[i])
        axs[i].set_title(data + ', skewness is: '+str(round(dataset[data].skew(axis = 0, skipna = True),2)))


if __name__ == '__main__':
    raw_df = pd.read_csv('creditcard.csv')

    # show_dataset_ratio()

    numeric_columns = (list(raw_df.loc[:, 'V1':'Amount']))
    boxplots_custom(dataset=raw_df, columns_list=numeric_columns, rows=8, cols=4, suptitle='Boxplots for each variable')
    plt.tight_layout()
    plt.show()

    print("All done")
