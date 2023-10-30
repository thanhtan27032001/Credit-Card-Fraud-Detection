import pandas as pd
import show_chart_dataset
from matplotlib import pyplot as plt


def remove_duplicated_rows(df):
    df.drop_duplicates(inplace=True)
    print("Duplicated values dropped succesfully")
    print("*" * 100)

    df = df.drop('Time', axis=1)
    return df


if __name__ == '__main__':
    raw_df = pd.read_csv('creditcard.csv')

    # origin
    show_chart_dataset.show_barchart(raw_df)

    # after remove duplicated rows
    df = raw_df.copy()
    df = remove_duplicated_rows(df)
    show_chart_dataset.show_barchart(df)

    # check outliers
    numeric_columns = (list(raw_df.loc[:, 'V1':'Amount']))
    show_chart_dataset.boxplots_custom(
        dataset=raw_df,
        columns_list=numeric_columns,
        rows=8,
        cols=4,
        suptitle='Boxplots for each variable'
    )

    # show plot and done
    plt.tight_layout()
    plt.show()
    print("All done")
