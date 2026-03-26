import pandas as pd
import sqlite3

def load():
    conn = sqlite3.connect("sales.db")
    df = pd.read_csv("data/processed/clean.csv")

    df.to_sql("sales", conn, if_exists="replace", index=False)
    print("Data loaded!")

if __name__ == "__main__":
    load()
