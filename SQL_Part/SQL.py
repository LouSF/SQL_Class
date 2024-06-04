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

    def LoginPage_Register_Query(self, UserName: str):
        try:
            SQL_Register_Check_Query = read_sql_file(SQLFiles_E.Register_ID_Query)
            self.cursor.execute(SQL_Register_Check_Query, UserName)
            result = self.cursor.fetchone()
            if result:
                print("ID in StuInfo")
                return True
            else:
                print("Not find ID in StuInfo")
                return False
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

    def StuPage_Rank_Query(self, UserName: str):
        try:
            SQL_Rank_Query = read_sql_file(SQLFiles_E.Rank_Query)
            self.cursor.execute(SQL_Rank_Query, UserName)
            result = self.cursor.fetchone()
            if result:
                print("Rank Query Succeed")
                return result
            else:
                print("Cannot find Rank")
                return False
        except pyodbc.Error as e:
            print(f"Error executing query: {e}")
            return None

    def StuPage_Rank_Count_Query(self):
        try:
            SQL_Rank_Count_Query = read_sql_file(SQLFiles_E.Rank_Count_Query)
            self.cursor.execute(SQL_Rank_Count_Query)
            result = self.cursor.fetchone()
            if result:
                print("Rank Count Query Succeed")
                return result
            else:
                print("Unknown Error happen")
                return False
        except pyodbc.Error as e:
            print(f"Error executing query: {e}")
            return None

    def StuPage_Student_Score_Query(self, UserID: str):
        try:
            SQL_Student_Score_Query = read_sql_file(SQLFiles_E.Student_Score_Query)
            self.cursor.execute(SQL_Student_Score_Query, UserID)
            result = self.cursor.fetchall()
            if result:
                print("Score Query Succeed")
                return result
            else:
                print("Unknown Error happen")
                return False
        except pyodbc.Error as e:
            print(f"Error executing query: {e}")
            return None

    def StuPage_Student_Course_Query(self, CourseNo: str = '%', CourseName: str = '%', Score: str = '%'):
        try:
            SQL_Student_Course_Query = read_sql_file(SQLFiles_E.Student_Course_Query)
            print((CourseNo, CourseName, Score))
            self.cursor.execute(SQL_Student_Course_Query, (CourseNo, CourseName, Score))

            print(self.cursor)
            result = self.cursor.fetchall()
            print(result)
            if result:
                print("Course Query Succeed")
                return result
            else:
                print("Unknown Error happen")
                return False
        except pyodbc.Error as e:
            print(f"Error executing query: {e}")
            return None

    def AdminPage_Student_Course_Query(self, CourseNo: str = '%'):
        try:
            SQL_Admin_Course_Query = read_sql_file(SQLFiles_E.Admin_Course_Query)
            print((CourseNo))
            self.cursor.execute(SQL_Admin_Course_Query, CourseNo)

            print(self.cursor)
            result = self.cursor.fetchall()
            print(result)
            if result:
                print("Course Query Succeed")
                return result
            else:
                print("Unknown Error happen")
                return False
        except pyodbc.Error as e:
            print(f"Error executing query: {e}")
            return None

    def AdminPage_Admin_StuInfo_Query(self, StuNum: str = '%', StuName: str = '%', StuSex: str = '%', StuClass: str = '%', StuAge: str = '%'):
        try:
            SQL_Student_Course_Query = read_sql_file(SQLFiles_E.Admin_StuInfo_Query)
            print((StuNum, StuName, StuSex, StuClass, StuAge))
            self.cursor.execute(SQL_Student_Course_Query, (StuNum, StuName, StuSex, StuClass, StuAge))

            print(self.cursor)
            result = self.cursor.fetchall()
            print(result)
            if result:
                print("Course Query Succeed")
                return result
            else:
                print("Unknown Error happen")
                return False
        except pyodbc.Error as e:
            print(f"Error executing query: {e}")
            return None
    def Admin_Student_Score_Query(self, StuNum: str = '%', StuName: str = '%', StuClass: str = '%', CourseName: str = '%', CourseNo: str = '%', StuScoreS: str = '%'):
        try:
            SQL_Score_Query = read_sql_file(SQLFiles_E.Admin_Score_Query)
            self.cursor.execute(SQL_Score_Query, (StuNum, StuName, StuClass, CourseName, CourseNo, StuScoreS))
            result = self.cursor.fetchall()
            if result:
                print("Score Query Succeed")
                return result
            else:
                print("Unknown Error happen")
                return False
        except pyodbc.Error as e:
            print(f"Error executing query: {e}")
            return None

    def Admin_Student_Rank_Query(self):
        try:
            SQL_Student_Rank_Query = read_sql_file(SQLFiles_E.Student_Rank_Query)
            self.cursor.execute(SQL_Student_Rank_Query)
            result = self.cursor.fetchall()
            if result:
                print("Score Query Succeed")
                return result
            else:
                print("Unknown Error happen")
                return False
        except pyodbc.Error as e:
            print(f"Error executing query: {e}")
            return None

    def Admin_Add_Course(self, CourseNo: str, CourseName: str, Score: int):
        try:
            SQL_Add_Course = read_sql_file(SQLFiles_E.Admin_Add_Course)
            self.cursor.execute(SQL_Add_Course, (CourseNo, CourseName, Score))
            self.conn.commit()
            print("Course added successfully")
            return True
        except pyodbc.Error as e:
            print(f"Error adding course: {e}")
            return None

    def Admin_Add_Student(self, StuNum: str, StuName: str, StuSex: str, StuClass: str, StuAge: str):
        try:
            SQL_Add_Student = read_sql_file(SQLFiles_E.Admin_Add_StuInfo)
            self.cursor.execute(SQL_Add_Student, (StuNum, StuName, StuSex, StuClass, StuAge))
            self.conn.commit()
            print("Student added successfully")
            return True
        except pyodbc.Error as e:
            print(f"Error adding student: {e}")
            return None

    def Admin_Add_StuSel(self, StuNum: str, CourseNo: str, Score: int):
        try:
            SQL_Add_StuSel = read_sql_file(SQLFiles_E.Admin_Add_StuSel)
            self.cursor.execute(SQL_Add_StuSel, (StuNum, CourseNo, Score))
            self.conn.commit()
            print("Student selection added successfully")
            return True
        except pyodbc.Error as e:
            print(f"Error adding student selection: {e}")
            return None

    def Admin_Del_Course(self, CourseNo: str):
        try:
            SQL_Del_Course = read_sql_file(SQLFiles_E.Admin_Del_Course)
            self.cursor.execute(SQL_Del_Course, CourseNo)
            self.conn.commit()
            print("Course deleted successfully")
            return True
        except pyodbc.Error as e:
            print(f"Error deleting course: {e}")
            return None

    def Admin_Del_Student(self, StuNum: str):
        try:
            SQL_Del_Student = read_sql_file(SQLFiles_E.Admin_Del_StuInfo)
            self.cursor.execute(SQL_Del_Student, StuNum)
            self.conn.commit()
            print("Student deleted successfully")
            return True
        except pyodbc.Error as e:
            print(f"Error deleting student: {e}")
            return None

    def Admin_Del_StuSel(self, StuNum: str, CourseNo: str):
        try:
            SQL_Del_StuSel = read_sql_file(SQLFiles_E.Admin_Del_StuSel)
            self.cursor.execute(SQL_Del_StuSel, (StuNum, CourseNo))
            self.conn.commit()
            print("Student selection deleted successfully")
            return True
        except pyodbc.Error as e:
            print(f"Error deleting student selection: {e}")
            return None

    def Admin_Change_Course(self, CourseNo: str, NewCourseName: str, NewScore: int):
        try:
            SQL_Change_Course = read_sql_file(SQLFiles_E.Admin_Change_Course)
            self.cursor.execute(SQL_Change_Course, (NewCourseName, NewScore, CourseNo))
            self.conn.commit()
            print("Course changed successfully")
            return True
        except pyodbc.Error as e:
            print(f"Error changing course: {e}")
            return None

    def Admin_Change_Student(self, StuNum: str, StuName: str, StuSex: str, StuClass: str, StuAge: str):
        try:
            SQL_Change_Student = read_sql_file(SQLFiles_E.Admin_Change_StuInfo)
            self.cursor.execute(SQL_Change_Student, (StuName, StuSex, StuClass, StuAge, StuNum))
            self.conn.commit()
            print("Student changed successfully")
            return True
        except pyodbc.Error as e:
            print(f"Error changing student: {e}")
            return None

    def Admin_Change_StuSel(self, StuNum: str, CourseNo: str, NewScore: int):
        try:
            SQL_Change_StuSel = read_sql_file(SQLFiles_E.Admin_Change_StuSel)
            self.cursor.execute(SQL_Change_StuSel, (NewScore, StuNum, CourseNo))
            self.conn.commit()
            print("Student selection changed successfully")
            return True
        except pyodbc.Error as e:
            print(f"Error changing student selection: {e}")
            return None
