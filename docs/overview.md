# Pipe Break Prediction Project – High-Level Overview

## 🛠 Project Summary

Aging water infrastructure is a growing concern for municipalities nationwide. This project uses data-driven modeling and statistical analysis to **predict pipe breaks** based on historical data obtained from a local utility via a **FOIL (Freedom of Information Law)** request. The objective is to support proactive maintenance, optimize replacement schedules, and reduce emergency repair costs.

The project includes a:
- 📊 **Streamlit web app** for exploring model predictions and infrastructure metrics
- 📑 **Quarto-generated technical report** for deep-dive analysis, results, and insights

---

## 📥 Data Acquisition

- Data was requested and obtained from the local water utility via a formal **FOIL request**
- Includes features such as:
  - Pipe material
  - Diameter
  - Install year
  - Geographic location
  - Break history
  - Soil conditions (where available)
  - Surrounding land use and pressure zone (if available)
  
---

## ⚙️ Methodology

### 🔍 **1. Data Preparation & Feature Engineering**
- Clean and normalize field names and formats
- Generate derived features (e.g., pipe age, diameter bins, age groups)
- Handle missing data using imputation and domain rules
- Encode categorical features for modeling

### 📈 **2. Statistical Validation**
- Use **Chi-Squared tests** to examine associations between:
  - Pipe age group and break likelihood
  - Pipe material and break occurrence
- Calculate **Degrees of Freedom** and assess **p-values** to validate model features statistically

### 🤖 **3. Machine Learning**
Planned models include:
- **Random Forest Classifier** (baseline model)
- **XGBoost** for improved performance on imbalanced data
- **Logistic Regression** as a transparent benchmark
- Ensemble modeling to improve generalization

Key steps:
- Address **class imbalance** via SMOTE or reweighting
- Perform **cross-validation** for robust performance metrics
- Evaluate using precision, recall, AUC, and F1-score

### 📌 **4. Deployment & Reporting**
- **Streamlit App**: Interactive dashboard for users to explore pipe asset risk, filter data by neighborhood or pipe characteristics, and download flagged assets.
- **Quarto Report**: Structured document including:
  - Executive summary
  - Methodology
  - Feature importance analysis
  - Predictive performance
  - Recommendations for utility planning teams

---

## 🚧 Anticipated Challenges
- Class imbalance (majority of pipes don’t break)
- Incomplete or inconsistent asset metadata
- Spatial autocorrelation effects in geographic clustering
- Interpreting black-box models (will be mitigated with SHAP)

---

## 📍 Future Work
- Integrate GIS heatmaps for visualizing high-risk zones
- Add time-series forecasting for seasonal trends in breaks
- Connect to live data systems for continuous model retraining

---

## 📂 Project Structure (In Development)

pipe_break_prediction/
├── app/ # Streamlit UI
├── data/ # FOIL data (cleaned and raw)
├── notebooks/ # EDA and modeling notebooks
├── quarto_report/ # Published Quarto report and assets
├── src/ # Core logic and pipeline code
├── tests/ # Unit tests for pipeline
├── overview.md # This file
└── README.md # Project summary and launch instructions


---

## 📌 Status

- [x] FOIL data acquired
- [x] Environment set up
- [ ] EDA and statistical testing in progress
- [ ] Model development underway
- [ ] Streamlit dashboard in prototyping
- [ ] Quarto report skeleton complete

---

**Author**: Brice Nelson  
**Project**: Part of the *Pencils & Python* initiative  
**Purpose**: Showcase real-world ML + statistical modeling for municipal infrastructure

