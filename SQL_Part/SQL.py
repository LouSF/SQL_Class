import pyodbc
from SQL_String import *

class SQL:
    def SQL_Connect(self, ConnectString: str):
        try:
            self.conn = pyodbc.connect(ConnectString)
            self.cursor = self.conn.cursor()
            print("Connection successful")
        except pyodbc.Error as e:
            print(f"Error connecting to database: {e}")

    def DelConnect(self):
        self.conn.close()
        print(f"SQL connecting deleted")

    def __init__(self, String: str):
        self.SQL_Connect(String)

    def LoginPage_Login(self, UserName: str, Password: str):
        try:
            SQL_Login_Query = read_sql_file(SQLFiles_E.Login_Query)
            self.cursor.execute(SQL_Login_Query, (UserName, Password))
            result = self.cursor.fetchone()
            print(result)
            if result:
                print("Login successful")
                return result
            else:
                print("Invalid username or password")
                return None
        except pyodbc.Error as e:
            print(f"Error executing query: {e}")
            return None

    def LoginPage_Register(self, UserName: str, Password: str, admin: bool):
        try:
            SQL_Register_Check_Query = read_sql_file(SQLFiles_E.Register_Check_Query)
            self.cursor.execute(SQL_Register_Check_Query, (UserName,))
            result = self.cursor.fetchone()
            if result:
                print("Username already exists")
                return None
            else:
                SQL_Register_Insert = read_sql_file(SQLFiles_E.Register_Insert)
                self.cursor.execute(SQL_Register_Insert, (UserName, Password, admin))
                self.conn.commit()
                print("Registration successful")
                return True
        except pyodbc.Error as e:
            print(f"Error executing query: {e}")
            return None