from statsmodels.tsa.statespace.sarimax import SARIMAX
from prophet import Prophet
import pandas as pd


def sarima_forecast(series, steps=3):
    model = SARIMAX(series, order=(1,1,1), seasonal_order=(1,1,1,12))
    fit = model.fit()

    forecast = fit.forecast(steps)
    return forecast


def prophet_forecast(series, steps=3):
    df = series.reset_index()
    df.columns = ['ds','y']

    model = Prophet()
    model.fit(df)

    future = model.make_future_dataframe(periods=steps, freq='ME')
    forecast = model.predict(future)

    return forecast[['ds','yhat']].tail(steps)