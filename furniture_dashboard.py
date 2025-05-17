
import streamlit as st
import pandas as pd

st.title("E-commerce Furniture Sales Dashboard")

df = pd.read_csv("/Users/rishavkumarsharma/Downloads/ecommerce_furniture_dataset_2024.csv")
df['price'] = df['price'].replace(r'[\$,]', '', regex=True).astype(float)

st.subheader("Top 10 Products by Units Sold")
top_products = df.sort_values(by='sold', ascending=False).head(10)
st.bar_chart(top_products.set_index('productTitle')['sold'])

st.subheader("Shipping Tags Distribution")
st.bar_chart(df['tagText'].value_counts())
