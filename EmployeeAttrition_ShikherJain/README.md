# Employee Attrition Prediction (Machine Learning Project)

## 📌 Overview

This project builds a machine learning system to predict employee attrition (whether an employee will leave the company). The goal is to help HR teams proactively identify at-risk employees and take preventive action.

---

## 🎯 Objectives

* Predict employee attrition using historical HR data
* Identify key factors driving employee exits
* Provide actionable insights for HR decision-making

---

## 📂 Dataset

* Source: IBM HR Analytics Dataset (Kaggle)
* Records: 1470 employees
* Target Variable: `Attrition` (Yes/No)

---

## 🛠️ Tech Stack

* Python
* Pandas, NumPy
* Scikit-learn
* Matplotlib, Seaborn

---

## ⚙️ Workflow

### 1. Data Preprocessing

* Dropped irrelevant columns (EmployeeNumber, Over18, etc.)
* Encoded categorical variables using One-Hot Encoding
* Scaled numerical features using StandardScaler

### 2. Exploratory Data Analysis

* Attrition trends by department and job role
* Income vs attrition analysis
* Work-life balance and tenure analysis

### 3. Model Building

Trained and compared:

* Logistic Regression
* Random Forest Classifier
* Gradient Boosting Classifier

Handled class imbalance using `class_weight='balanced'`.

---

## 📊 Model Evaluation

Metrics used:

* Precision
* Recall
* F1 Score
* ROC-AUC

Best Model: **[Fill after running — likely Random Forest]**

---

## 🔍 Key Insights

* Employees working overtime are significantly more likely to leave
* Lower income groups show higher attrition rates
* Early tenure employees (0–3 years) have the highest churn
* Sales roles experience higher attrition compared to other departments

---

## 💡 Business Recommendations

* Reduce overtime workload in high-risk roles
* Implement retention programs for early-stage employees
* Improve work-life balance policies
* Conduct targeted HR interventions for high-risk departments

---

## ⚠️ Limitations

* Dataset lacks behavioral and psychological factors
* Model does not account for external job market conditions

---

## 🚀 How to Run

```bash
pip install -r requirements.txt
jupyter notebook analysis.ipynb
```

---

## 📁 Project Structure

```
EmployeeAttrition_ShikherJain/
│
├── analysis.ipynb
├── HR_Attrition.csv
├── README.md
├── requirements.txt
├── charts/
│   ├── *.png
```

---

## 📌 Future Improvements

* Add SHAP for model explainability
* Deploy model using FastAPI
* Integrate real-time HR dashboards

---

## 👨‍💻 Author

Shikher Jain
