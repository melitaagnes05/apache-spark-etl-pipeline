# Apache Spark ETL Pipeline

## Overview

This project demonstrates an end-to-end ETL (Extract, Transform, Load) pipeline using Apache Spark (PySpark), Python, and MySQL. The pipeline extracts employee and department datasets from CSV files, performs data transformations using Spark DataFrames, and loads the processed data into a MySQL database.

---

## Features

- Extract data from CSV files using PySpark
- Join employee and department datasets
- Create a new Experience Level column
- Filter employees based on salary
- Calculate average salary by department
- Load transformed data into MySQL
- Logging and exception handling
- Environment variable configuration using `.env`

---

## Tech Stack

- Python
- Apache Spark (PySpark)
- Pandas
- MySQL
- SQL
- Git & GitHub

---

## Project Structure

```
apache-spark-etl-pipeline/
│
├── config/
│   └── config.py
│
├── data/
│   ├── employees.csv
│   └── departments.csv
│
├── logs/
│   └── project.log
│
├── scripts/
│   ├── extract.py
│   ├── transform.py
│   └── load.py
│
├── sql/
│   ├── schema.sql
│   └── queries.sql
│
├── .env
├── .gitignore
├── main.py
├── README.md
└── requirements.txt
```

---

## ETL Workflow

### Extract

- Read employee and department datasets using PySpark.

### Transform

- Join datasets
- Create Experience Level column
- Filter employees with salary greater than 60000
- Calculate average salary by department

### Load

- Convert Spark DataFrame to Pandas DataFrame
- Load processed data into MySQL

---

## Database Schema

| Column | Type |
|----------|------|
| EmployeeID | INT |
| Name | VARCHAR(50) |
| DepartmentID | INT |
| Salary | FLOAT |
| Experience | INT |
| Department | VARCHAR(50) |
| ExperienceLevel | VARCHAR(20) |

---

## How to Run

1. Clone the repository

```
git clone https://github.com/melitaagnes05/apache-spark-etl-pipeline.git
```

2. Install dependencies

```
pip install -r requirements.txt
```

3. Configure environment variables in `.env`

4. Create the MySQL database and execute `schema.sql`

5. Run the project

```
python main.py
```

---

## Output

- Employee dataset extraction
- Department dataset extraction
- Joined dataset
- Employee classification
- Salary filtering
- Department-wise average salary
- Data successfully loaded into MySQL

---

## Author

**Melita Agnes D'Souza**

LinkedIn: https://www.linkedin.com/in/melita-agnes-d-souza

GitHub: https://github.com/melitaagnes05