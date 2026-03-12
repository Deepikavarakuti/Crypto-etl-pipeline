# Crypto ETL Pipeline 🚀

## Project Overview

This project demonstrates a simple **ETL (Extract, Transform, Load) pipeline** that collects cryptocurrency price data from the CoinGecko API, processes it using Python, and stores it in a PostgreSQL database.

The goal of this project is to practice **data ingestion, data transformation, and database loading**, which are core skills for a Data Engineer.

---

## Architecture

CoinGecko API
↓
Python Extract Script
↓
Python Transform Script
↓
PostgreSQL Database

---

## Tech Stack

* Python
* Pandas
* Requests
* PostgreSQL
* psycopg2
* Git & GitHub

---

## Project Structure

crypto-etl-pipeline/

extract.py        # Extracts crypto data from API
transform.py      # Cleans and formats the data
load.py           # Loads data into PostgreSQL
pipeline.py       # Runs the complete ETL pipeline
requirements.txt  # Project dependencies
README.md         # Project documentation

---

## Dataset Source

The data is fetched from the CoinGecko public API.

Example cryptocurrencies used:

* Bitcoin
* Ethereum

---

## Setup Instructions

### 1. Clone the repository

git clone https://github.com/yourusername/crypto-etl-pipeline.git

cd crypto-etl-pipeline

### 2. Install dependencies

pip install -r requirements.txt

### 3. Create PostgreSQL table

Run this SQL command:

CREATE TABLE crypto_prices (
id SERIAL PRIMARY KEY,
crypto_name TEXT,
price_usd FLOAT,
timestamp TIMESTAMP
);

### 4. Update database credentials

Open **load.py** and update:

host
database
user
password

### 5. Run the pipeline

python pipeline.py

---

## Example Output

crypto_name | price_usd | timestamp
BITCOIN     | 65000     | 2026-03-12
ETHEREUM    | 3200      | 2026-03-12

---

## What I Learned

* Extracting data from an API
* Transforming data using Python and Pandas
* Loading data into PostgreSQL
* Building a basic ETL pipeline
* Organizing a data engineering project

---

## Future Improvements

* Schedule pipeline using Apache Airflow
* Containerize the project with Docker
* Store historical crypto prices
* Deploy pipeline on cloud

---

## Author

Your Name
GitHub: https://github.com/Deepikavarakuti
