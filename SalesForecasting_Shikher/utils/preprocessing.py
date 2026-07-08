import pandas as pd

def load_data(path):
    df = pd.read_csv(path)

    df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True)
    df['Ship Date'] = pd.to_datetime(df['Ship Date'], dayfirst=True)

    df['Sales'] = pd.to_numeric(df['Sales'], errors='coerce')
    df = df.dropna(subset=['Order Date', 'Sales'])

    df = df.sort_values('Order Date')
    df.set_index('Order Date', inplace=True)

    return df


def create_time_series(df):
    monthly = df['Sales'].resample('ME').sum()
    weekly = df['Sales'].resample('W').sum()

    return monthly, weekly