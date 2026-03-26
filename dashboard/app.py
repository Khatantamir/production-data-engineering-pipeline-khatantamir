import streamlit as st
import pandas as pd
from src.config import DATA_PATH

st.set_page_config(page_title="Data Engineering Dashboard", layout="wide")

st.title("Production Data Engineering Dashboard")
st.write("This dashboard shows the processed output from the ETL pipeline.")

try:
    df = pd.read_csv(DATA_PATH)

    st.subheader("Processed Data Preview")
    st.dataframe(df.head(20), use_container_width=True)

    st.subheader("Key Metrics")
    total_revenue = df["total_bill"].sum()
    avg_tip = df["tip"].mean()

    col1, col2 = st.columns(2)
    col1.metric("Total Revenue", f"${total_revenue:.2f}")
    col2.metric("Average Tip", f"${avg_tip:.2f}")

    st.subheader("Total Bill by Day")
    sales_by_day = df.groupby("day")["total_bill"].sum()
    st.bar_chart(sales_by_day, use_container_width=True)

    st.subheader("Average Tip by Day")
    avg_tip_by_day = df.groupby("day")["tip"].mean()
    st.bar_chart(avg_tip_by_day, use_container_width=True)

    st.subheader("Filter by Day")
    selected_day = st.selectbox("Select Day", df["day"].unique())

    filtered_df = df[df["day"] == selected_day]
    st.dataframe(filtered_df, use_container_width=True)

    st.subheader("Dataset Info")
    st.write(f"Rows: {df.shape[0]}")
    st.write(f"Columns: {df.shape[1]}")

except FileNotFoundError:
    st.error("clean.csv not found. Please run the pipeline first using: python main.py")