from scripts.extract import extract_data
from scripts.transform import transform_data
from scripts.load import load_data


def main():

    spark, employees, departments = extract_data()

    employee_data = transform_data(
        employees,
        departments
    )

    load_data(employee_data)

    spark.stop()


if __name__ == "__main__":
    main()