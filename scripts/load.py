import mysql.connector
import logging

from config.config import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME

logging.basicConfig(
    filename="logs/project.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def load_data(employee_data):
    """
    Load Spark DataFrame into MySQL.
    """

    connection = None
    cursor = None

    try:

        connection = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )

        logging.info("Connected to MySQL database.")

        cursor = connection.cursor()

        cursor.execute("DELETE FROM employees")

        logging.info("Deleted existing records from employees table.")

        data = employee_data.toPandas()

        query = """
        INSERT INTO employees
        (EmployeeID, Name, DepartmentID, Salary, Experience, Department, ExperienceLevel)
        VALUES (%s,%s,%s,%s,%s,%s,%s)
        """

        for _, row in data.iterrows():

            values = (
                int(row["EmployeeID"]),
                row["Name"],
                int(row["DepartmentID"]),
                float(row["Salary"]),
                int(row["Experience"]),
                row["Department"],
                row["ExperienceLevel"]
            )

            cursor.execute(query, values)

        connection.commit()

        logging.info("Employee data loaded successfully into MySQL.")

        print("✅ Data loaded successfully into MySQL!")

    except mysql.connector.Error as err:

        logging.error(f"MySQL Error: {err}")

        print(f"MySQL Error: {err}")

    finally:

        if cursor:
            cursor.close()

        if connection:
            connection.close()

        logging.info("Database connection closed.")