# ACME HR Portal

FastAPI GET endpoints for reading employee records from a MySQL database.

## Setup

From this directory, install the dependencies:

```powershell
py -m pip install -r requirements.txt
```

Set the database environment variables before starting the API. Copy `.env.example` as a reference and replace its example values; the app reads environment variables directly and does not load a `.env` file automatically.

```powershell
$env:MYSQL_HOST = "localhost"
$env:MYSQL_PORT = "3306"
$env:MYSQL_USER = "your_mysql_username"
$env:MYSQL_PASSWORD = "your_mysql_password"
$env:MYSQL_DATABASE = "your_database_name"
py -m uvicorn main:app --reload
```

The database must contain an `employees` table with an `employee_id` column. The list and detail endpoints return each database row as JSON.

## Endpoints

- `GET /` — Welcome message.
- `GET /employees` — All employee records.
- `GET /employees/{employee_id}` — One employee, or `404` if the ID does not exist.

Open <http://127.0.0.1:8000/docs> to try the endpoints in Swagger UI.
