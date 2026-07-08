# 📊 Time Series Forecasting System

### SARIMA vs Prophet vs XGBoost

---

## 🚀 Project Overview

This project implements a **complete time series forecasting pipeline** to predict future sales using:

* **SARIMA** (statistical model)
* **Prophet** (trend + seasonality modeling)
* **XGBoost** (machine learning with lag features)

It also includes:

* Exploratory Data Analysis (EDA)
* Stationarity testing
* Feature engineering
* Model comparison
* Anomaly detection
* Customer segmentation
* Future forecasting (3-month horizon)

---

## 🎯 Objectives

* Forecast sales accurately using multiple approaches
* Compare statistical vs ML vs hybrid models
* Identify best-performing model using error metrics
* Detect anomalies in weekly sales
* Segment customers based on purchasing behavior

---

## 📂 Dataset

* Source: `data/train.csv`
* Key Columns:

  * `Order Date`
  * `Ship Date`
  * `Sales`
  * `Category`
  * `Region`
  * `Customer ID`

---

## 🔹 Task Breakdown

### 1. Data Preprocessing

* Converted dates to datetime
* Handled missing values
* Created `Shipping Delay` feature
* Sorted and indexed by time

---

### 2. Time Series Aggregation

* Monthly sales (`ME`)
* Weekly sales (`W`)

---

### 3. Exploratory Data Analysis

* Monthly trend visualization
* Category-wise sales
* Region-wise sales
* Seasonal decomposition

---

### 4. Stationarity Check

* Augmented Dickey-Fuller (ADF) test
* Used to validate SARIMA assumptions

---

### 5. Train-Test Split

* Last 12 months used as test set

---

### 6. Models Implemented

#### 🔸 SARIMA

* Captures trend + seasonality
* Parameters: `(1,1,1)(1,1,1,12)`
* Strength: interpretable, statistical rigor

---

#### 🔸 Prophet

* Handles trend + seasonality + holidays
* Minimal feature engineering
* Business-friendly model

---

#### 🔸 XGBoost

* Uses lag-based features:

  * `lag1`, `lag2`
  * `month`
* Learns nonlinear patterns
* Requires feature engineering

---

### 7. Evaluation Metrics

* **MAE** → absolute error
* **RMSE** → penalizes large errors (primary metric)
* **MAPE** → percentage error

---

### 8. Model Comparison

| Model   | MAE | RMSE | MAPE |
| ------- | --- | ---- | ---- |
| SARIMA  | ✔   | ✔    | ✔    |
| Prophet | ✔   | ✔    | ✔    |
| XGBoost | ✔   | ✔    | ✔    |

👉 Best model selected based on **lowest RMSE**

---

## 🔮 Forecasting

* Generated **3-month future forecasts**
* Implemented:

  * SARIMA direct forecasting
  * Prophet future dataframe
  * XGBoost iterative prediction

---

## 🚨 Anomaly Detection

* Model: **Isolation Forest**
* Features:

  * Weekly sales
  * Rolling mean
* Output:

  * Identified abnormal spikes/drops

---

## 👥 Customer Segmentation

* Features:

  * Total spend
  * Average spend
  * Order count
* Model: **KMeans (k=3)**
* Use case:

  * Targeted marketing
  * Customer profiling

---

## 🧠 Key Learnings

* SARIMA requires stationarity and parameter tuning
* Prophet simplifies time series modeling
* XGBoost performs well with proper feature engineering
* Forecasting pipelines must avoid data leakage
* Time series ≠ standard ML (ordering matters)

---

## ⚠️ Limitations

* SARIMA assumes linearity
* Prophet sensitive to parameter choices
* XGBoost depends heavily on feature quality
* No external variables (holidays, promotions)

---

## 🔥 Future Improvements

* Hyperparameter tuning (Grid / Bayesian)
* Add exogenous variables (weather, holidays)
* Use `auto_arima` for optimal SARIMA
* Implement walk-forward validation
* Ensemble models for robustness
* Deploy as API (FastAPI / Flask)

---

## 🛠️ Tech Stack

* Python
* Pandas, NumPy
* Matplotlib, Seaborn
* Statsmodels
* Prophet
* XGBoost
* Scikit-learn

---

## 📌 How to Run

```bash
pip install -r requirements.txt
```

```bash
jupyter notebook
```

---

## 🏁 Final Verdict

This project demonstrates:

* End-to-end time series pipeline
* Multi-model comparison
* Strong understanding of forecasting techniques
* Practical ML + statistical modeling integration

---

## 💼 Resume Bullet (Use This)

> Built a multi-model time series forecasting system using SARIMA, Prophet, and XGBoost, achieving optimal performance based on RMSE; included anomaly detection and customer segmentation for business insights.

---