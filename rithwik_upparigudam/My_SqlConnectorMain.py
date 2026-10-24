from fastapi import FastAPI
import mysql.connector
test=FastAPI()
connection=mysql.connector.connect(
    database="mydb",password="1234",user="root",host="localhost"
)
cursor=connection.cursor()
@test.get("/")
def welcomemessage():
    msg="Hello Welcome To AcmeHr Project"
    return f"{msg}"
@test.get("/getemployees")
def getemployees():
    try:
        cursor.execute("Select * from employeefastapi")
        x=cursor.fetchall()
        return x
    except mysql.connector.errors.ProgrammingError as e:
        return e


@test.get("/getemployees/{id}")
def getempbyid(id:int):
    try:
        query=f"select * from employeefastapi where id={id}"
        cursor.execute(query)
        x=cursor.fetchone()
        return x
    except mysql.connector.errors.ProgrammingError as e:
        return e
