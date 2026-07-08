import pandas as pd

def create_features(df):
    df = df.copy()

    for lag in [1,2,3]:
        df[f'lag_{lag}'] = df['Sales'].shift(lag)

    df['rolling_mean'] = df['Sales'].rolling(3).mean()
    df['rolling_std'] = df['Sales'].rolling(3).std()

    df['month'] = df.index.month
    df['quarter'] = df.index.quarter

    return df.dropna()