from enum import Enum
import os

CurrectPath = os.path.dirname(os.path.realpath(__file__))

SERVER = 'localhost,1433'
DATABASE = 'Big_HW'
USERNAME = 'sa'
PASSWORD = '<YourStrong@Passw0rd>'

connectionString = (f'DRIVER={{ODBC Driver 18 for SQL Server}};'
                    f'SERVER={SERVER};'
                    f'DATABASE={DATABASE};'
                    f'UID={USERNAME};'
                    f'PWD={PASSWORD};'
                    'Encrypt=no;'
                    'TrustServerCertificate=no;')

class SQLFiles_E(Enum):
    Login_Query = 'SQL_lib/Login_Query.sql'
    Register_Check_Query = 'SQL_lib/Register_Check_Query.sql'
    Register_Insert = 'SQL_lib/Register_Insert.sql'
    NONE = None

def read_sql_file(file_enum: SQLFiles_E):
    file_path = os.path.join(CurrectPath, file_enum.value)
    try:
        with open(file_path, 'r') as file:
            print("Read SQL file successful")
            return file.read()
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except IOError as e:
        print(f"Error reading file {file_path}: {e}")
