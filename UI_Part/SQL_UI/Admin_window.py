# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QFileDialog, QInputDialog, QLineEdit
from PySide6.QtGui import QStandardItemModel, QStandardItem

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic Admin_Window.ui -o ui_Admin_Window.py
from ui_Admin_Window import Ui_Admin_Window
from PySide6.QtCore import Signal

from SQL_Part.SQL import *
from State import *
import pandas as pd
import enum

import re

class Admin_Windows(QWidget):
    closed = Signal()

    class Table_State_E(Enum):
        NONE = None
        Student_Info = 0
        Student_Sel = 1
        Course = 2
        Rank = 3


    def __init__(self, Message_ID, parent=None):
        super().__init__(parent)
        self.ui = Ui_Admin_Window()
        self.ui.setupUi(self)

        self.conn = SQL(connectionString)

        self.ui.UserName_label.setText(Message_ID[0])

        self.ui.Logout_Button.clicked.connect(self.on_button_clicked_Logout_Button)

        self.ui.Query_Button.clicked.connect(self.on_button_clicked_StuInfo_Query_Button) # StuInfo
        self.ui.Query_Course_Button.clicked.connect(self.on_button_clicked_Query_Course_Button)
        self.ui.Query_Score_Button.clicked.connect(self.on_button_clicked_Query_Score_Button) # StuScore
        self.ui.Query_Score_Rank_Button.clicked.connect(self.on_button_clicked_Query_Score_Rank_Button)
        self.ui.Output_Button.clicked.connect(self.on_button_clicked_Output_Button)


        self.ui.Add_Button.clicked.connect(self.on_button_clicked_Add_Button)
        self.ui.Finish_Input_Button.clicked.connect(self.on_button_clicked_Confirm_Add_Button)  # Finish Input
        self.ui.Del_Button.clicked.connect(self.on_button_clicked_Del_Button)
        self.ui.Change_Button.clicked.connect(self.on_button_clicked_Change_Button)


        self.state = self.Table_State_E.NONE

    def populate_table_view(self, df, table_view):
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(df.columns.tolist())

        for index, row in df.iterrows():
            items = [QStandardItem(str(item)) for item in row]
            model.appendRow(items)

        table_view.setModel(model)

    def selectSavePath(self):
        save_filename = QFileDialog.getSaveFileName(None, "设置保存路径", "", "All Files (*);;CSV Files (*.csv)")
        return save_filename[0]
    def on_button_clicked_Output_Button(self):
        try:
            save_path = self.selectSavePath()
            if save_path:
                self.df.to_csv(save_path, index=False, encoding='utf-8')
                QMessageBox.information(self, "Success", "文件已保存!")
            else:
                QMessageBox.warning(self, "Cancelled", "操作取消")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred while saving the file: {e}")

    def StudentNum_Judge(self, Num: str) -> bool:
        pattern = r'^\d{10}$'
        return bool(re.match(pattern, Num))

    def Gender_Judge(self, gender: str) -> bool:
        pattern = r'^(男|女)$'
        return bool(re.match(pattern, gender))

    def Score_Judge(self, Score: int) -> bool:
        return 0 <= Score <= 100

    def on_button_clicked_StuInfo_Query_Button(self):
        Target_Text = self.ui.StuNum_lineEdit.text()

        if (Target_Text == ''):
            QMessageBox.warning(self, "Warning", "留空默认以*规则搜索")
            InfoQ = self.conn.AdminPage_Admin_StuInfo_Query()
        else:
            Target_Text = '%' + Target_Text + '%'
            InfoQ = self.conn.AdminPage_Admin_StuInfo_Query(Target_Text, Target_Text, Target_Text, Target_Text, Target_Text)
        if InfoQ == False:
            QMessageBox.critical(self, "Error", "未找到")
        else:
            InfoQ = [list(elem) for elem in InfoQ]
            print(InfoQ)
            self.df = pd.DataFrame(InfoQ, columns=['学号', '姓名', '性别', '班级', '年龄'])
            self.populate_table_view(self.df, self.ui.tableView)
            self.state = self.Table_State_E.Student_Info


    def on_button_clicked_Query_Course_Button(self):
        Target_Text = self.ui.Course_lineEdit.text()
        if (Target_Text == ''):
            QMessageBox.warning(self, "Warning", "留空默认以*规则搜索")
            ACourseQ = self.conn.StuPage_Student_Course_Query()
        else:
            Target_Text = '%' + Target_Text + '%'
            ACourseQ = self.conn.StuPage_Student_Course_Query(Target_Text,Target_Text,Target_Text)
        if ACourseQ == False:
            QMessageBox.critical(self, "Error", "未找到")
        else:
            ACourseQ = [list(elem) for elem in ACourseQ]
            print(ACourseQ)
            self.df = pd.DataFrame(ACourseQ, columns=['课程代码', '课程名', '学分'])
            self.populate_table_view(self.df, self.ui.tableView)
            self.state = self.Table_State_E.Course


    def on_button_clicked_Query_Score_Button(self):
        Target_Text = self.ui.FindScore_lineEdit.text()
        if (Target_Text == ''):
            QMessageBox.warning(self, "Warning", "留空默认以*规则搜索")
            ScoreQ = self.conn.Admin_Student_Score_Query()
        else:
            Target_Text = '%' + Target_Text + '%'
            ScoreQ = self.conn.Admin_Student_Score_Query(Target_Text, Target_Text, Target_Text, Target_Text, Target_Text, Target_Text)

        if ScoreQ == False:
            QMessageBox.critical(self, "Error", "未找到")
        else:
            ScoreQ = [list(elem) for elem in ScoreQ]
            print(ScoreQ)
            self.df = pd.DataFrame(ScoreQ, columns=['学号', '姓名', '班级', '课程', '课程代码', '成绩'])
            self.populate_table_view(self.df, self.ui.tableView)
            self.state = self.Table_State_E.Student_Sel

    def on_button_clicked_Query_Score_Rank_Button(self):
        RankQ = self.conn.Admin_Student_Rank_Query()
        RankQ = [list(elem) for elem in RankQ]
        print(RankQ)
        self.df = pd.DataFrame(RankQ, columns=['学号', '姓名', '班级', '总分', '排名'])
        self.populate_table_view(self.df, self.ui.tableView)
        self.state = self.Table_State_E.Rank

    def on_button_clicked_Logout_Button(self):
        QMessageBox.information(self, "SUCCEED", "已登出")
        self.state = self.Table_State_E.NONE
        self.close()

    def _Rank_change_Warning(self):
        QMessageBox.critical(self, "Undefined Work", "Rank_Table不得修改，必须由TRIGGER生成！")

    def _Undef_change_Warning(self):
        QMessageBox.critical(self, "Undefined Work", "未定义表")

    def _UNABLE_change_Warning(self):
        QMessageBox.critical(self, "Error", "数据输入有误！")

    def _ASK(self, Rule: str):
        QMessage_result = QMessageBox.question(self, "Attation",
                                               Rule,
                                               QMessageBox.Yes | QMessageBox.No)
        return QMessage_result

    def on_button_clicked_Add_Button(self):
        if self.state == self.Table_State_E.NONE:
            self._Undef_change_Warning()
        elif self.state == self.Table_State_E.Rank:
            self._Rank_change_Warning()
        else:
            row_position = self.ui.tableView.model().rowCount()
            self.ui.tableView.model().insertRow(row_position)
            self.ui.tableView.selectRow(row_position)
            QMessageBox.information(self, "提示", "请在表格中输入新数据，然后点击确认按钮以保存到数据库。")
            if self.state == self.Table_State_E.Student_Sel:
                QMessageBox.information(self, "Attation", "只有‘学号’， ‘课程号’， ‘成绩’参与添加判断")

    def on_button_clicked_Confirm_Add_Button(self):
        if self.state == self.Table_State_E.NONE:
            self._Undef_change_Warning()
        elif self.state == self.Table_State_E.Rank:
            self._Rank_change_Warning()
        else:
            row_position = self.ui.tableView.selectionModel().currentIndex().row()
            if self.state == self.Table_State_E.Student_Sel:
                new_data = self.collect_data_from_row(row_position, ['学号', '姓名', '班级', '课程', '课程代码', '成绩'])
                print(new_data)
                if new_data:
                    StuNum, _, _, _, CourseNo, Score = new_data
                    if self.StudentNum_Judge(StuNum) == False:
                        QMessageBox.critical(self, "Error", "ID不是预期的格式：10位纯数字")
                    if self.Score_Judge(Score) == False:
                        QMessageBox.critical(self, "Error", "成绩需要介于[0, 100]")
                    else:
                        if self.conn.Admin_Add_StuSel(StuNum, CourseNo, Score):
                            QMessageBox.information(self, "Success", "添加成功")
                            self.on_button_clicked_Query_Score_Button()
                        else:
                            self._UNABLE_change_Warning()
            elif self.state == self.Table_State_E.Student_Info:
                new_data = self.collect_data_from_row(row_position, ["学号", "姓名", "性别", "班级", "年龄"])
                print(new_data)
                if new_data:
                    StuNum, StuName, StuSex, StuClass, StuAge = new_data
                    if self.StudentNum_Judge(StuNum) == False:
                        QMessageBox.critical(self, "Error", "ID不是预期的格式：10位纯数字")
                    elif self.Gender_Judge(StuSex) == False:
                        QMessageBox.critical(self, "Error", "性别输入错误")
                    else:
                        if self.conn.Admin_Add_Student(StuNum, StuName, StuSex, StuClass, StuAge):
                            QMessageBox.information(self, "Success", "添加成功")
                            self.on_button_clicked_StuInfo_Query_Button()
                        else:
                            self._UNABLE_change_Warning()
            elif self.state == self.Table_State_E.Course:
                new_data = self.collect_data_from_row(row_position, ["课程代码", "课程名", "学分"])
                print(new_data)
                if new_data:
                    CourseNo, CourseName, Credit = new_data

                    try:
                        Credit = int(Credit)
                    except ValueError:
                        QMessageBox.critical(self, "Error", "学分必须是Int")

                    if type(Credit) != int:
                        pass
                    else:
                        if self.conn.Admin_Add_Course(CourseNo, CourseName, Credit):
                            QMessageBox.information(self, "Success", "添加成功")
                            self.on_button_clicked_Query_Course_Button()
                        else:
                            self._UNABLE_change_Warning()

    def collect_data_from_row(self, row, column_names):
        model = self.ui.tableView.model()
        data = []
        for column_name in column_names:
            column = self.df.columns.get_loc(column_name)
            index = model.index(row, column)
            value = model.data(index)
            if value is None or value == "":
                QMessageBox.warning(self, "输入错误", f"请填写所有字段: {', '.join(column_names)}")
                return None
            data.append(value)
        return data

    def on_button_clicked_Del_Button(self):
        if self._ASK("确认执行删除？") == QMessageBox.Yes:
            if self.state == self.Table_State_E.NONE:
                self._Undef_change_Warning()
            elif self.state == self.Table_State_E.Rank:
                self._Rank_change_Warning()
            elif self.state == self.Table_State_E.Student_Sel:
                selected_indexes = self.ui.tableView.selectionModel().selectedRows()
                if not selected_indexes:
                    QMessageBox.warning(self, "Warning", "没有选中任何行")
                    return

                student_num_index = self.df.columns.get_loc("学号")
                student_sel_index = self.df.columns.get_loc("课程代码")

                for index in sorted(selected_indexes, reverse=True):
                    student_num = self.df.iloc[index.row(), student_num_index]
                    student_sel = self.df.iloc[index.row(), student_sel_index]
                    if self.conn.Admin_Del_StuSel(student_num, student_sel):
                        self.df = self.df.drop(index.row()).reset_index(drop=True)
                        QMessageBox.information(self, "SUCCEED", "操作成功")
                    else:
                        QMessageBox.critical(self, "Error", f"删除学生选课记录 {student_num}: {student_sel}失败")

                self.populate_table_view(self.df, self.ui.tableView)

            elif self.state == self.Table_State_E.Student_Info:
                selected_indexes = self.ui.tableView.selectionModel().selectedRows()
                if not selected_indexes:
                    QMessageBox.warning(self, "Warning", "没有选中任何行")
                    return

                student_num_index = self.df.columns.get_loc("学号")

                for index in sorted(selected_indexes, reverse=True):
                    student_num = self.df.iloc[index.row(), student_num_index]
                    if self.conn.Admin_Del_Student(student_num):
                        self.df = self.df.drop(index.row()).reset_index(drop=True)
                        QMessageBox.information(self, "SUCCEED", "操作成功")
                    else:
                        QMessageBox.critical(self, "Error", f"删除学生 {student_num} 失败")

                self.populate_table_view(self.df, self.ui.tableView)
            elif self.state == self.Table_State_E.Course:
                selected_indexes = self.ui.tableView.selectionModel().selectedRows()
                if not selected_indexes:
                    QMessageBox.warning(self, "Warning", "没有选中任何行")
                    return

                course_no_index = self.df.columns.get_loc("课程代码")

                for index in sorted(selected_indexes, reverse=True):
                    course_no = self.df.iloc[index.row(), course_no_index]
                    if self.conn.Admin_Del_Course(course_no):
                        self.df = self.df.drop(index.row()).reset_index(drop=True)
                        QMessageBox.information(self, "SUCCEED", "操作成功")
                    else:
                        QMessageBox.critical(self, "Error", f"删除课程 {course_no} 失败")

                self.populate_table_view(self.df, self.ui.tableView)

    def on_button_clicked_Change_Button(self):
        if self.state == self.Table_State_E.NONE:
            self._Undef_change_Warning()
        elif self.state == self.Table_State_E.Rank:
            self._Rank_change_Warning()
        elif self.state == self.Table_State_E.Student_Sel:
            pass
        elif self.state == self.Table_State_E.Student_Info:
            pass
        elif self.state == self.Table_State_E.Course:
            pass

        pass
    def closeEvent(self, event):
        self.closed.emit()  # Emit the custom signal
        super().closeEvent(event)


