import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("E-commerce Customers Dashboard")

df = pd.read_csv("ecommerce_customers.csv")

st.subheader("Dataset Preview")
st.dataframe(df.head())

st.subheader("Dataset Information")
st.write(df.describe())

st.subheader("Customer Data")
st.write("Total Customers:", len(df))

st.subheader("Data Visualization")

numeric_cols = df.select_dtypes(include="number").columns

if len(numeric_cols) > 0:
    column = st.selectbox("Select a column", numeric_cols)
    fig, ax = plt.subplots()
    sns.histplot(df[column], kde=True, ax=ax)
    st.pyplot(fig)
