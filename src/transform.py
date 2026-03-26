import pandas as pd

def transform():
    df = pd.read_csv("data/raw/raw.csv")

    # clean column names
    df.columns = df.columns.str.strip()

    # create new column
    df["total_bill_with_tax"] = df["total_bill"] * 1.1

    # save clean data
    df.to_csv("data/processed/clean.csv", index=False)

    print("Data transformed!")