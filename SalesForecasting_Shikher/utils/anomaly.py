from sklearn.ensemble import IsolationForest


def detect_anomalies(series):
    df = series.to_frame(name='Sales')

    df['rolling_mean'] = df['Sales'].rolling(4).mean()
    df = df.dropna()

    model = IsolationForest(contamination=0.05)
    df['anomaly'] = model.fit_predict(df[['Sales','rolling_mean']])

    df['is_anomaly'] = df['anomaly'] == -1

    return df