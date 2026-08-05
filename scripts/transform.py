from pyspark.sql.functions import col, when, avg
import logging


def transform_data(employees, departments):
    """
    Transform employee dataset.
    """

    employee_data = employees.join(
        departments,
        on="DepartmentID",
        how="inner"
    )

    logging.info("Joined employee and department datasets.")

    print("\nJoined Dataset")
    employee_data.show()

    employee_data = employee_data.withColumn(
        "ExperienceLevel",
        when(col("Experience") >= 5, "Senior")
        .otherwise("Junior")
    )

    logging.info("Experience level column created.")

    print("\nEmployee Data with Experience Level")
    employee_data.show()

    high_salary = employee_data.filter(
        col("Salary") > 60000
    )

    logging.info("Filtered employees with salary greater than 60000.")

    print("\nEmployees with Salary > 60000")
    high_salary.show()

    avg_salary = employee_data.groupBy("Department").agg(
        avg("Salary").alias("AverageSalary")
    )

    logging.info("Calculated average salary by department.")

    print("\nAverage Salary by Department")
    avg_salary.show()

    return employee_data