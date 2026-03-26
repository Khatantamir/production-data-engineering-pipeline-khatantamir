import streamlit as st
import pandas as pd

st.set_page_config(page_title="Data Engineering Dashboard", layout="wide")

st.title("Production Data Engineering Dashboard")
st.write("This dashboard shows the processed output from the ETL pipeline.")

try:
    df = pd.read_csv("data/processed/clean.csv")

    st.subheader("Processed Data Preview")
    st.dataframe(df.head(20))

    st.subheader("Total Bill by Day")
    sales_by_day = df.groupby("day")["total_bill"].sum()
    st.bar_chart(sales_by_day)

    st.subheader("Average Tip by Day")
    avg_tip_by_day = df.groupby("day")["tip"].mean()
    st.bar_chart(avg_tip_by_day)

    st.subheader("Dataset Info")
    st.write(f"Rows: {df.shape[0]}")
    st.write(f"Columns: {df.shape[1]}")

except FileNotFoundError:
    st.error("clean.csv not found. Please run the pipeline first using: python main.py")
