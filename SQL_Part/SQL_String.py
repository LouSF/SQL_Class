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
    Register_ID_Query = 'SQL_lib/Register_ID_Query.sql'
    Register_Check_Query = 'SQL_lib/Register_Check_Query.sql'
    Register_Insert = 'SQL_lib/Register_Insert.sql'
    Rank_Query = 'SQL_lib/Rank_Query.sql'
    Rank_Count_Query = 'SQL_lib/Rank_Count_Query.sql'
    Student_Score_Query = 'SQL_lib/Student_Score_Query.sql'
    Student_Course_Query = 'SQL_lib/Student_Course_Query.sql'
    Student_Rank_Query = 'SQL_lib/Student_Rank_Query.sql'
    Admin_Score_Query = 'SQL_lib/Admin_Score_Query.sql'
    Admin_StuInfo_Query = 'SQL_lib/Admin_StuInfo_Query.sql'
    Admin_Course_Query = 'SQL_lib/Admin_Course_Query.sql'

    Admin_Add_Course = 'SQL_lib/Admin_Add_Course.sql'
    Admin_Add_StuInfo = 'SQL_lib/Admin_Add_StuInfo.sql'
    Admin_Add_StuSel = 'SQL_lib/Admin_Add_StuSel.sql'

    Admin_Del_Course = 'SQL_lib/Admin_Del_Course.sql'
    Admin_Del_StuInfo = 'SQL_lib/Admin_Del_StuInfo.sql'
    Admin_Del_StuSel = 'SQL_lib/Admin_Del_StuSel.sql'

    Admin_Change_Course = 'SQL_lib/Admin_Change_Course.sql'
    Admin_Change_StuInfo = 'SQL_lib/Admin_Change_StuInfo.sql'
    Admin_Change_StuSel = 'SQL_lib/Admin_Change_StuSel.sql'

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
