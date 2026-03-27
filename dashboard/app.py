import streamlit as st
import pandas as pd

RAW_DATA_PATH = "data/raw/raw.csv"
CLEAN_DATA_PATH = "data/processed/clean.csv"

st.set_page_config(page_title="Production Data Engineering Dashboard", layout="wide")

st.title("Production Data Engineering Dashboard")
st.write("This dashboard shows the raw input, cleaned output, key metrics, charts, and filtered views from the ETL pipeline.")

try:
    raw_df = pd.read_csv(RAW_DATA_PATH)
    clean_df = pd.read_csv(CLEAN_DATA_PATH)

    raw_df.columns = raw_df.columns.str.strip()
    clean_df.columns = clean_df.columns.str.strip()

    st.subheader("Pipeline Summary")
    st.write("This pipeline extracts raw data, transforms it into clean data, adds a new feature column, loads it into storage, and visualizes the final output.")

    st.subheader("Raw Data Preview")
    st.dataframe(raw_df.head(10), use_container_width=True)

    st.subheader("Clean Data Preview")
    st.dataframe(clean_df.head(10), use_container_width=True)

    st.subheader("Key Metrics")
    total_revenue = clean_df["total_bill"].sum()
    avg_tip = clean_df["tip"].mean()
    total_rows = clean_df.shape[0]
    total_columns = clean_df.shape[1]

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Revenue", f"${total_revenue:.2f}")
    col2.metric("Average Tip", f"${avg_tip:.2f}")
    col3.metric("Rows", total_rows)
    col4.metric("Columns", total_columns)

    st.subheader("Total Bill by Day")
    sales_by_day = clean_df.groupby("day")["total_bill"].sum()
    st.bar_chart(sales_by_day, use_container_width=True)

    st.subheader("Average Tip by Day")
    avg_tip_by_day = clean_df.groupby("day")["tip"].mean()
    st.bar_chart(avg_tip_by_day, use_container_width=True)

    st.subheader("Filter by Day")
    selected_day = st.selectbox("Select Day", clean_df["day"].unique())
    filtered_df = clean_df[clean_df["day"] == selected_day]
    st.dataframe(filtered_df, use_container_width=True)

    st.subheader("Dataset Info")
    st.write(f"Rows: {clean_df.shape[0]}")
    st.write(f"Columns: {clean_df.shape[1]}")

    st.subheader("Column Names")
    st.write(list(clean_df.columns))

    st.subheader("Example Transformation")
    st.code("total_bill_with_tax = total_bill * 1.1", language="python")

except FileNotFoundError as e:
    st.error(f"Required data file not found: {e}")

except KeyError as e:
    st.error(f"Missing expected column in dataset: {e}")

except Exception as e:
    st.error(f"Unexpected error: {e}")