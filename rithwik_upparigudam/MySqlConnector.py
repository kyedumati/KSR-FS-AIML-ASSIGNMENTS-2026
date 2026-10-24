import mysql.connector
import os
import logging
logging.basicConfig(filename="MySqlLogger",filemode="a",level=logging.INFO,format=
                    "%(asctime)s-%(levelname)s-%(message)s")
class MySql:
    def __init__(self,connection):
        self.Connection=connection
        self.cursor=connection.cursor(dictionary=True)

    def readDataBase(self,tablename):
        logging.info("User Choose to Reading Data In Tables")
        try:
            print("Fecthing DataBase DataBase..")
            j=int(input("Enter 1 for FetchAll Or Enter 2 For fetchOne"))
            if j==1:
                self.cursor.execute(f"select * from {tablename}")
                x=self.cursor.fetchall()
                for i in x:
                    print(i)
            elif j==2:
                query=f"select * from {tablename} limit 1"
                self.cursor.execute(query)
                x=self.cursor.fetchall()
                print(x)
            else:
                print("You Are Entering Wrong Number Please Try Again Later")
        except ValueError:
            print("Enter A Vaild Number")
        except Exception:
            logging.warning(f"User entered {tablename} Which is not in database")
            print("Invaild Table Name Please Enter Correct Table Name")
    def addingData(self,tablex,prompt):
        logging.info("User Choose to Inserting Data Into Tables")
        try:
            for i in prompt:
                self.cursor.execute(f"insert into {tablex} values {(i)}")
        except Exception as e:
            logging.error(e)
            print(e)
        else:
            logging.info(f" {prompt}Values Added SucessFully")
            print("Value Added Sucessfully")
            self.Connection.commit()



    def customprompt(self,prompt):
        logging.info("User choose Custom Prompt")
        try:
            self.cursor.execute(prompt)
            x=self.cursor.fetchall()
            for i in x:
                print(i)
            logging.info("Custom Prompt printed Sucessfully")
        except Exception as e:
            logging.error(f"{e} Error")
            print("Prompt is wrong please check if table name and querty is correct")

    def updatetable(self,query):
        logging.info("User Choose to update table")
        try:
            self.cursor.execute(query)
        except Exception as e:
            print(e)
            logging.error(f"{e} Error")
        else:
            print("Table Updated Successfully")
            logging.warning(f"{query} Updated Suceessfully")
            self.Connection.commit()

    def deletecloumstable(self,table,where):
        logging.warning("User choose to delect row From Table")
        try:
            query=f"select * from {table} limit 0"
            self.cursor.execute(query)
            xs=self.cursor.fetchall()
        except Exception as e:
            print("𝑾𝒓𝒐𝒏𝒈 𝒕𝒂𝒃𝒍𝒆 𝒏𝒂𝒎𝒆 𝒆𝒏𝒕𝒆𝒓𝒆𝒅")
            logging.error(f"{e} Error Occured")
        else:
            try:
                query1=f"delete from {table} where {where}"
                self.cursor.execute(query1)
            except Exception as e:
                print(e)
                logging.error(f"{e} error Occured")
            else:
                logging.warning(f"{table} where {where},Row Deleted Successfully")
                self.Connection.commit()
                print("𝑺𝒖𝒄𝒄𝒆𝒔𝒔𝒇𝒖𝒍𝒍𝒚 𝑫𝒆𝒍𝒆𝒕𝒆𝒅")

    def renamingdatabase(self,table,newname):
        logging.warning("User Choose to rename table")
        try:
            self.cursor.execute(f"Select * from {table} limit 0")
            xs=self.cursor.fetchall()
        except Exception as e:
            print(e)
            logging.error(f"{e} error Occured")
        else:
            self.cursor.execute(f"alter table {table} rename to {newname}")
            logging.warning(f"Table Name {table} changed to {newname}")
            self.Connection.commit()
            print("𝑹𝒆𝒏𝒂𝒎𝒆 𝑺𝒖𝒄𝒄𝒆𝒔𝒔𝑭𝒖𝒍")
    def connectionclose(self):
        logging.info("Closing Off Connections")
        print("Closing Connections...")
        self.cursor.close()
        self.Connection.close()






if __name__ =="__main__":
    try:
        print("Welcome to my Sql Connector")
        logging.info("Opened MySqlConnector")
        passx=input("Enter your password to enter")
        x = os.environ.get("Password")
        user = os.environ.get("user")
        if passx==x:
            logging.info("Password Entered Connected to DataBase")
            database=input("Enter the database you want to work on")
            logging.info(f"user choose database {database}")
            try:
                mydb = mysql.connector.connect(host="localhost", port=3306,
                user=user, password=x, database=database)
            except Exception:
                logging.warning(f"Wrong Database Entered = {database}")
                print("Wrong Database Name Entered")
            else:
                cursor=mydb.cursor()
                classx=MySql(mydb)
                logging.info("MySqlConnectorPython Opened")
                try:
                    while True:
                        print("Welcome To MySql Server Connector")
                        print("Enter 1 for Viewing the Table")
                        print("Enter 2 for adding Data into table")
                        print("Enter 3 for viewing table with specific condition")
                        print("Enter 4 for updating a table")
                        print("Enter 5 for deleting columns in table")
                        print("Enter 6 for Renaming Table")
                        print("Enter 7 for exiting the program")
                        try:
                            i=int(input("Enter Your Choice"))
                        except Exception as e:
                            logging.info("User Didn't enter Given Options")
                            print("Please Enter Digits Properly")
                        else:
                            if i==1:
                                logging.info("User Chooce To ViewTables")
                                tablename=input("Enter the table name").strip()
                                logging.info(f"User Selected Option1 To view Table{tablename}")
                                classx.readDataBase(tablename)
                            elif i==2:
                                try:

                                    print("Please Select the table you want to add your values into")
                                    condition = False
                                    tablex=input("Enter the table").strip()
                                    values=int(input("Enter how many data's you want to enter"))
                                    test=f"select * from {tablex} limit 0"
                                    try:
                                        cursor.execute(test)
                                        x=cursor.fetchall()
                                        condition=True
                                    except Exception:
                                        print("Wrong Table Name Please ReEnter Proper TableName")
                                        condition=False
                                    else:
                                        if condition==True:
                                            emlist=[]
                                            query=f"show columns from {tablex}"
                                            cursor.execute(query)
                                            x=cursor.fetchall()
                                            while values>0:
                                                xs = []
                                                for i in x:
                                                    print(f"Enter {i[0]},Type={i[1]}")
                                                    inpx=input("Enter Here")
                                                    xs.append(inpx)
                                                emlist.append(tuple(xs))
                                                values-=1
                                            classx.addingData(tablex, emlist)

                                except Exception as e:
                                    print(e,"Something went wrong please try again later")
                            elif i==3:
                                print("Please follow exact syntax as how you follow in mysql")
                                prompt=input("Enter the condition").strip()
                                classx.customprompt(prompt)
                            elif i==4:
                                print("Welcome to updating a table")
                                query=input("enter the table name / where condition to update").strip()
                                classx.updatetable(query)
                            elif i==5:
                                print("Welcome To Deleting A Table Row")
                                tablex=input("Enter the table name where you want to delete the row").strip()
                                where=input("Where/It is must!").strip()
                                classx.deletecloumstable(tablex,where)
                            elif i==6:
                                print("Welcome to renaming table")
                                tablex=input("Enter Table Name").strip()
                                RenamedTableName=input("Enter Renamed Table Name")
                                classx.renamingdatabase(tablex,RenamedTableName)
                            elif i==7:
                                print("Thank you for using this program")
                                cursor.close()
                                mydb.close()
                                classx.connectionclose()
                                break
                except Exception as e:
                    print("Something went wrong")
                    logging.error(e)
        else:
                    print("WRONG PASSWORD ENTERED!")
                    logging.warning("Wrong Password Entered")

    except Exception as e:
        print(f"{e} Error Occured")
        logging.error(f"{e} Error CameUp")







