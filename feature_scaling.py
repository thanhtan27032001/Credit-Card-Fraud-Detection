from sklearn.preprocessing import StandardScaler


# Creating function for scaling
def standard_scaler(df, col_names):
    features = df[col_names]
    scaler = StandardScaler().fit(features.values)
    features = scaler.transform(features.values)
    df[col_names] = features
    return df
