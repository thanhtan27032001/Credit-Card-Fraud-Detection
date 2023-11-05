import read_dataset
import show_chart_dataset
import numpy as np
from matplotlib import pyplot as plt
from collections import Counter


def remove_duplicated_rows(df):
    df.drop_duplicates(inplace=True)
    print("Duplicated values dropped succesfully")
    print("*" * 100)

    df = df.drop('Time', axis=1)
    return df


def IQR_method(df, n, features):
    """
    Takes a dataframe and returns an index list corresponding to the observations
    containing more than n outliers according to the Tukey IQR method.
    """
    outlier_list = []

    for column in features:
        # 1st quartile (25%)
        Q1 = np.percentile(df[column], 25)
        # 3rd quartile (75%)
        Q3 = np.percentile(df[column], 75)
        # Interquartile range (IQR)
        IQR = Q3 - Q1
        # outlier step
        outlier_step = 1.5 * IQR
        # Determining a list of indices of outliers
        outlier_list_column = df[(df[column] < Q1 - outlier_step) | (df[column] > Q3 + outlier_step)].index
        # appending the list of outliers
        outlier_list.extend(outlier_list_column)

    # selecting observations containing more than x outliers
    outlier_list = Counter(outlier_list)
    multiple_outliers = list(k for k, v in outlier_list.items() if v > n)

    # Calculate the number of records below and above lower and above bound value respectively
    out1 = df[df[column] < Q1 - outlier_step]
    out2 = df[df[column] > Q3 + outlier_step]

    print('Total number of deleted outliers is:', out1.shape[0] + out2.shape[0])

    return multiple_outliers


def remove_duplicated_rows_and_outliers(raw_df, numeric_columns):
    # remove duplicated rows
    df = raw_df.copy()
    df = remove_duplicated_rows(df)

    # detecting outliers
    Outliers_IQR = IQR_method(df, 1, numeric_columns)

    # dropping outliers
    df_out = df.drop(Outliers_IQR, axis=0).reset_index(drop=True)

    print("Done remove_duplicated_rows_and_outliers()")
    return df_out


if __name__ == '__main__':
    raw_df = read_dataset.read_raw_dataset()

    # show origin dataset
    show_chart_dataset.show_barchart(raw_df)

    # remove duplicated rows
    df = raw_df.copy()
    df = remove_duplicated_rows(df)

    # check outliers
    numeric_columns = (list(raw_df.loc[:, 'V1':'Amount']))
    show_chart_dataset.boxplots_custom(
        dataset=raw_df,
        columns_list=numeric_columns,
        rows=8,
        cols=4,
        suptitle='Boxplots for each variable'
    )

    # detecting outliers
    Outliers_IQR = IQR_method(df, 1, numeric_columns)

    # dropping outliers
    df_out = df.drop(Outliers_IQR, axis=0).reset_index(drop=True)

    # show plot and done
    show_chart_dataset.show_barchart(df_out)
    plt.tight_layout()
    plt.show()
    print("All done")
