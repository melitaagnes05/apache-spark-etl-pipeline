from pyspark.sql import SparkSession
import logging

logging.basicConfig(
    filename="logs/project.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def extract_data():
    """
    Extract employee and department datasets using PySpark.
    """

    spark = SparkSession.builder \
        .appName("Apache Spark ETL Pipeline") \
        .getOrCreate()

    logging.info("Spark session created.")

    employees = spark.read.csv(
        "data/employees.csv",
        header=True,
        inferSchema=True
    )

    logging.info("Employees dataset loaded.")

    departments = spark.read.csv(
        "data/departments.csv",
        header=True,
        inferSchema=True
    )

    logging.info("Departments dataset loaded.")

    print("\nEmployees Dataset")
    employees.show()

    print("\nDepartments Dataset")
    departments.show()

    return spark, employees, departments