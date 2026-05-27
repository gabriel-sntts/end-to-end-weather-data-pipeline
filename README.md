# End-to-End Weather Data Pipeline

Modern data engineering pipeline built with Python, Docker, LocalStack, S3, Parquet and DuckDB.

This project simulates a real-world cloud ETL pipeline, extracting weather data from a public API, transforming the data and storing it inside a simulated AWS S3 Data Lake using LocalStack.

---

# Architecture

```text
Weather API
    ↓
Extract (CSV)
    ↓
Transform (Parquet)
    ↓
S3 Data Lake (LocalStack)
    ↓
Analytics with DuckDB
```

---

# Technologies Used

- Python
- Pandas
- Docker
- LocalStack
- AWS S3 (simulated)
- Boto3
- DuckDB
- Parquet

---

# Features

- Extract weather data from API
- Transform and clean datasets
- Convert CSV to Parquet
- Upload data to S3 bucket
- Query data using SQL analytics
- Simulate cloud environment locally

---

# Project Structure

```text
├── analytics/
│   └── query_data.py
│
├── etl/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── inspect_s3.py
│
├── docker-compose.yml
├── pipeline_runner.py
├── requirements.txt
└── README.md
```

---

# Pipeline Steps

## 1. Extract

Consumes weather data from a public API and stores it as CSV.

## 2. Transform

Cleans and transforms the dataset using Pandas and converts it to Parquet format.

## 3. Load

Uploads transformed data into an S3 bucket running locally with LocalStack.

## 4. Analytics

Uses DuckDB to run analytical SQL queries on the dataset.

---

# How to Run

## Clone repository

```bash
git clone https://github.com/gabriel-sntts/end-to-end-weather-data-pipeline.git
```

## Create virtual environment

```bash
python -m venv venv
```

## Activate virtual environment

### Windows

```bash
venv\Scripts\activate
```

## Install dependencies

```bash
pip install -r requirements.txt
```

## Start LocalStack

```bash
docker compose up -d
```

## Run pipeline

```bash
python pipeline_runner.py
```

---

# Concepts Practiced

- ETL Pipelines
- Data Engineering
- Cloud Simulation
- Data Lakes
- Object Storage
- Analytics Engineering
- SQL Analytics
- Docker Containers
- Data Transformation
- Pipeline Orchestration

---

# Future Improvements

- Airflow orchestration
- Real AWS deployment
- Automated scheduling
- Data validation layer
- Dashboard visualization
- CI/CD pipeline
- Terraform infrastructure

---

# Author

Gabriel Santos

Computer Science student focused on Data Engineering, Machine Learning and Cloud Computing.
