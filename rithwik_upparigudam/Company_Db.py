import mysql.connector
import os
import logging
logging.basicConfig(level=logging.INFO,filename=
"CompanyDb.log",filemode="a",format="%(asctime)s-%(levelname)s-%(message)s")
class MySqlConnector:
    def __init__(self,Connection,table):
        self.connection=Connection
        self.cursor=self.connection.cursor()
        self.table=table

    def read_data(self):
        query=f"select * from {self.table}"
        self.cursor.execute(query)
        xs=self.cursor.fetchall()
        for x in xs:
          print(f"Employee ID:{x[0]}")
          print(f"Employee Name:{x[1]}")
          print(f"Department:{x[2]}")
          print(f"Salary:{x[3]}")

          print("-"*20)
        logging.info(f"Fetched All Data from {self.table}")



    def insert_Values(self):
        print(f"Inserting into {self.table}")
        print("Welcome To inserting Values Into Table")
        emlist=[]
        finallist=[]
        try:
            x=int(input("Enter how many values you want to input"))
            while x>0:
                query=f"show columns from {self.table}"
                self.cursor.execute(query)
                xs=self.cursor.fetchall()
                for i in xs:
                    insertion=input(f"Enter {i[0]} Type={i[1]}")
                    emlist.append(insertion)
                finallist.append(tuple(emlist))
                emlist.clear()
                x-=1

            try:
                for i in finallist:
                    insertquery=f"insert into {self.table} values {i}"
                    self.cursor.execute(insertquery)
            except Exception as e:
                print(e)
                logging.error(e)
            else:
                self.connection.commit()
                print("Updated Sucessfully")
                logging.info(f"Updated New Data into {self.table}")
        except ValueError:
            print("Enter integer not float")
            logging.error("User Entered Wrong DataType")
        except Exception as e:
            print(e)
            logging.error(e)
    def closing_database(self):
        self.cursor.close()
        self.connection.close()
        logging.info("Closing Database")












if __name__ == "__main__":
        user=os.environ.get("user")
        password=os.environ.get("password")
        try:
            Connection=mysql.connector.connect(
                user=user,password=password,database="company_db",host="localhost"
            )
            table="employees"
            x = MySqlConnector(Connection, table)
            logging.info("Connection Secured Starting...")
            while True:
                print("Enter 1 for Reading Table")
                print("Enter 2 for Inserting DataInto Table")
                print("Enter 3 for exiting")
                try:
                    i=int(input("Enter the number"))
                    if i>3 or i<0:
                        raise ValueError
                except Exception as e:
                    print("Enter Number b/w 1-3 And Not String")
                    logging.error("User Entered Number b/w 1-3 OR String")
                else:
                    if i==1:
                        x.read_data()
                    elif i==2:
                        x.insert_Values()
                    elif i==3:
                        x.ClosingDatabase()
                        print("Thank you for using this Program")
                        break
        except Exception as e:
            print(e)
            logging.error(e)
        finally:
            Connection.close()