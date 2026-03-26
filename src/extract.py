import pandas as pd

def extract():
    url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
    df = pd.read_csv(url)
    df.to_csv("data/raw/raw.csv", index=False)
    print("Data extracted!")

if __name__ == "__main__":
    extract()
