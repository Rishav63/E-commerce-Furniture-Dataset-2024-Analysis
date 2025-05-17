# 🪑 E-commerce Furniture Dataset 2024 – Analysis & Dashboard

This project explores the E-commerce Furniture Dataset 2024 with the goal of deriving actionable business insights and building predictive models to support decision-making. The project also includes an interactive dashboard built using Streamlit.

---

## 📦 Dataset

**File**: `ecommerce_furniture_dataset_2024.csv`  
The dataset includes product-level details such as:

- `productTitle`
- `price`
- `sold`
- `category`
- `tagText` (shipping labels)
- Other relevant attributes

---

## 📊 Exploratory Data Analysis (EDA)

We performed the following EDA tasks:

- Handled missing values and cleaned monetary columns
- Visualized price distributions
- Identified top 10 products by sales volume
- Analyzed shipping tags (`tagText`) distribution
- Correlation analysis between features like `price` and `sold`

---

## 🤖 Machine Learning Models

We tested three classification algorithms to predict performance based on features:

| Model                | Accuracy  |
|---------------------|-----------|
| Random Forest        | 64.29%    |
| Logistic Regression  | 68.37%    |
| Support Vector Machine (SVM) | **70.41%** |

We also extracted **feature importance** using Random Forest to understand the most influential features.

---

## 📈 Streamlit Dashboard

An interactive dashboard was created to present key insights:

- Top 10 Products by Units Sold
- Shipping Tag Distribution

### To run the dashboard:
```bash
streamlit run furniture_dashboard.py
