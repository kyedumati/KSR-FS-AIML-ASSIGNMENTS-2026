import os
from typing import Any

import mysql.connector
from fastapi import FastAPI, HTTPException
from mysql.connector import Error

app = FastAPI(title="ACME HR Portal")


def get_db_connection() -> mysql.connector.MySQLConnection:
    """Create a connection using the MySQL settings in the environment."""
    required_settings = ("MYSQL_USER", "MYSQL_PASSWORD", "MYSQL_DATABASE")
    missing_settings = [name for name in required_settings if not os.getenv(name)]
    if missing_settings:
        raise HTTPException(
            status_code=500,
            detail=f"Missing database configuration: {', '.join(missing_settings)}",
        )

    try:
        return mysql.connector.connect(
            host=os.getenv("MYSQL_HOST", "localhost"),
            port=int(os.getenv("MYSQL_PORT", "3306")),
            user=os.environ["MYSQL_USER"],
            password=os.environ["MYSQL_PASSWORD"],
            database=os.environ["MYSQL_DATABASE"],
        )
    except (Error, ValueError) as exc:
        raise HTTPException(
            status_code=500,
            detail="Could not connect to the employee database.",
        ) from exc


def fetch_employee(query: str, params: tuple[Any, ...] = ()) -> list[dict[str, Any]]:
    connection = get_db_connection()
    cursor = None
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query, params)
        return cursor.fetchall()
    except Error as exc:
        raise HTTPException(
            status_code=500,
            detail="Could not retrieve employee records from the database.",
        ) from exc
    finally:
        if cursor is not None:
            cursor.close()
        connection.close()


@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "Welcome to ACME HR Portal"}


@app.get("/employees")
def get_employees() -> list[dict[str, Any]]:
    return fetch_employee("SELECT * FROM employees")


@app.get("/employees/{employee_id}")
def get_employee(employee_id: int) -> dict[str, Any]:
    employees = fetch_employee(
        "SELECT * FROM employees WHERE employee_id = %s",
        (employee_id,),
    )
    if not employees:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employees[0]
