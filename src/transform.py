import pandas as pd

def transform():
    df = pd.read_csv("data/raw/raw.csv")

    df = df.dropna()
    df["total_bill_with_tax"] = df["total_bill"] * 1.1

    df.to_csv("data/processed/clean.csv", index=False)
    print("Data transformed!")

if __name__ == "__main__":
    transform()
