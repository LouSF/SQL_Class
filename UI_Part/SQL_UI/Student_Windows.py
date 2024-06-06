# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QFileDialog
from PySide6.QtGui import QStandardItemModel, QStandardItem

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic Student_Windows.ui -o ui_Student_Windows.py
#     pyside6-rcc src.qrc -o src_rc.py
from ui_Student_Windows import Ui_Students_Windows
from PySide6.QtCore import Signal

from SQL_Part.SQL import *
from State import *
import pandas as pd
import ast

class Students_Windows(QWidget):
    closed = Signal()
    def __init__(self, Message_ID, parent=None):
        super().__init__(parent)
        self.ui = Ui_Students_Windows()
        self.ui.setupUi(self)

        self.conn = SQL(connectionString)

        Message_ID[0] = str(Message_ID[0])
        RegisterQ = self.conn.LoginPage_Register_Query(Message_ID[0])

        if RegisterQ != False:
            NameQ, RankQ = self.conn.StuPage_Rank_Query(Message_ID[0])
            RCountQ = self.conn.StuPage_Rank_Count_Query()

            ScoreQ = self.conn.StuPage_Student_Score_Query(Message_ID[0])
            ScoreQ = [list(elem) for elem in ScoreQ]
            print(ScoreQ)
            self.df_ScoreQ = pd.DataFrame(ScoreQ, columns= ['学号', '姓名', '班级', '课程', '课程代码', '成绩'])
            self.populate_table_view(self.df_ScoreQ, self.ui.Score_tableView)

            CourseQ = self.conn.StuPage_Student_Course_Query()
            CourseQ = [list(elem) for elem in CourseQ]
            print(CourseQ)
            self.df_CourseQ = pd.DataFrame(CourseQ, columns= ['课程代码', '课程名', '学分'])
            self.populate_table_view(self.df_CourseQ, self.ui.Course_tableView)

            self.ui.Rank_label.setText(str(RankQ) + '/' + str(RCountQ[0]))
            self.ui.UserName_label.setText(str(NameQ))

        else:
            QMessageBox.information(self, "INFO", "此账号未绑定实际用户")
            self.ui.Rank_label.setText('X')
            self.ui.UserName_label.setText(Message_ID[0])



        self.ui.Course_Output_Button.clicked.connect(self.on_button_clicked_Course_Output_Button)
        self.ui.Score_Output_Button.clicked.connect(self.on_button_clicked_Score_Output_Button)
        self.ui.Logout_Button.clicked.connect(self.on_button_clicked_Logout_Button)
        self.ui.User_Help.clicked.connect(self.on_button_Help_Button)

    def populate_table_view(self, df, table_view):
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(df.columns.tolist())

        for index, row in df.iterrows():
            items = [QStandardItem(str(item)) for item in row]
            model.appendRow(items)

        table_view.setModel(model)

    def on_button_clicked_Logout_Button(self):
        QMessageBox.information(self, "SUCCEED", "已登出")
        self.close()

    def selectSavePath(self):
        save_filename = QFileDialog.getSaveFileName(None, "设置保存路径", "", "All Files (*);;CSV Files (*.csv)")
        return save_filename[0]

    def on_button_clicked_Course_Output_Button(self):
        try:
            save_path = self.selectSavePath()
            if save_path:
                self.df_CourseQ.to_csv(save_path, index=False, encoding='utf-8')
                QMessageBox.information(self, "Success", "文件已保存!")
            else:
                QMessageBox.warning(self, "Cancelled", "操作取消")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred while saving the file: {e}")

    def on_button_clicked_Score_Output_Button(self):
        try:
            save_path = self.selectSavePath()
            if save_path:
                self.df_ScoreQ.to_csv(save_path, index=False, encoding='utf-8')
                QMessageBox.information(self, "Success", "文件已保存!")
            else:
                QMessageBox.warning(self, "Cancelled", "操作取消")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred while saving the file: {e}")
    def closeEvent(self, event):
        self.closed.emit()  # Emit the custom signal
        super().closeEvent(event)


    def on_button_Help_Button(self):
        QMessage_result = QMessageBox.question(self, "Help",
                                               "有我在你不需要Help",
                                               QMessageBox.Yes | QMessageBox.No)
        if QMessage_result == QMessageBox.No:
            QMessageBox.information(self, "Help", "目前在学生界面\n学生界面不允许修改任何记录，但是可以进行导出操作")
