# Production Data Engineering Pipeline

This project shows a simple real-world data engineering workflow.

It takes raw data, cleans it, and stores it in a database so it can be used for analysis.

---

## What this project does

- Extracts data from an external source
- Cleans and transforms the data
- Adds a new feature column
- Loads the data into a database
- Prepares data for analysis

---

## Project Structure

production-data-engineering-pipeline-khatantamir/

data/
- raw/          # Raw data
- processed/    # Clean data

src/
- extract.py    # Data extraction
- transform.py  # Data cleaning
- load.py       # Load to database

main.py         # Pipeline runner  
requirements.txt  
README.md  

---

## Tech Stack

- Python
- Pandas
- SQLite

---

## How to Run

Clone the repository:

git clone https://github.com/Khatantamir/production-data-engineering-pipeline-khatantamir.git
cd production-data-engineering-pipeline-khatantamir

Install dependencies:

pip install -r requirements.txt

Run the pipeline:

python main.py

---

## Pipeline Steps

1. Extract data from source  
2. Clean and transform data  
3. Save cleaned data  
4. Load data into database  

---

## Results

### Raw Data
![Raw Data](images/raw.png)

### Clean Data
![Clean Data](images/clean.png)

---

## Example Transformation

A new column is added:

total_bill_with_tax = total_bill * 1.1

---

## Example SQL Query

SELECT day, SUM(total_bill)
FROM sales
GROUP BY day;

---

## Summary

This project demonstrates how to build a simple data pipeline using Python.

It shows how raw data can be turned into clean, usable data for analysis.

---

## Author

Khatantamir
