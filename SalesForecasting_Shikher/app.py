import streamlit as st
import pandas as pd
import os

# Import utils
from utils.preprocessing import load_data, create_time_series
from utils.anomaly import detect_anomalies
from utils.clustering import customer_clustering

st.set_page_config(layout="wide")

st.title("📊 Demand Intelligence Dashboard")

# =========================
# LOAD DATA (clean way)
# =========================
BASE_DIR = os.path.dirname(__file__)
train_csv = os.path.join(BASE_DIR, "data", "train.csv")
# print(f"Loading data from: {train_csv}")  # Debugging line
df = load_data(train_csv)

monthly_sales, weekly_sales = create_time_series(df)

# =========================
# SIDEBAR NAVIGATION
# =========================
page = st.sidebar.radio("Navigation", [
    "Overview",
    "Forecast",
    "Anomaly Detection",
    "Segmentation"
])

# =========================
# PAGE 1 — OVERVIEW
# =========================
if page == "Overview":
    st.subheader("Monthly Sales Trend")

    st.line_chart(monthly_sales)

    st.subheader("Weekly Sales Trend")
    st.line_chart(weekly_sales)

# =========================
# PAGE 2 — FORECAST
# =========================
elif page == "Forecast":
    st.subheader("Sales Forecast")

    horizon = st.slider("Months Ahead", 1, 3, 3)

    forecast_df = pd.read_csv(f"{BASE_DIR}/data/forecast.csv")

    # Ensure date format
    forecast_df['Date'] = pd.to_datetime(forecast_df['Date'])
    forecast_df.set_index('Date', inplace=True)

    # Apply horizon filter
    forecast_df = forecast_df.head(horizon)

    st.write("Forecast Data")
    st.dataframe(forecast_df)

    st.line_chart(forecast_df)

# =========================
# PAGE 3 — ANOMALY DETECTION
# =========================
elif page == "Anomaly Detection":
    st.subheader("Weekly Anomaly Detection")

    anomaly_df = detect_anomalies(weekly_sales)

    st.line_chart(anomaly_df['Sales'])

    st.subheader("Detected Anomalies")
    st.dataframe(anomaly_df[anomaly_df['is_anomaly']])

# =========================
# PAGE 4 — SEGMENTATION
# =========================
elif page == "Segmentation":
    st.subheader("Customer Segmentation")

    clusters = customer_clustering(df)

    st.dataframe(clusters)

    st.subheader("Cluster Distribution")
    st.bar_chart(clusters['cluster'].value_counts())