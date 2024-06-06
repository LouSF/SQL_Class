# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QFileDialog
from PySide6.QtGui import QStandardItemModel, QStandardItem

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic Admin_Add.ui -o ui_Admin_Add.py

from ui_Admin_Add import Ui_Admin_Add
from PySide6.QtCore import Signal

from SQL_Part.SQL import *
from State import *
import re
import pandas as pd
import ast

class AdminPage_Admin_Add(QWidget):
    def __init__(self, conn, parent=None):
        super().__init__(parent=None)
        self.ui = Ui_Admin_Add()
        self.ui.setupUi(self)

        self.conn = conn

        self.State = False

        self.ui.Admin_Add_Q_pushButton.clicked.connect(self.on_button_clicked_Add_Q_pushButton)

        self.ui.Admin_Add_pushButton.clicked.connect(self.on_button_clicked_Add_pushButton)


    def StudentNum_Judge(self, Num: str) -> bool:
        pattern = r'^\d{10}$'
        return bool(re.match(pattern, Num))

    def Score_Judge(self, Score: int) -> bool:
        return 0 <= Score <= 100

    def on_button_clicked_Add_Q_pushButton(self):
        self.ADD_STUID = self.ui.StuNum_lineEdit.text()
        self.ADD_COURSE = self.ui.SourceNo_lineEdit.text()
        self.ADD_SCORE = self.ui.Score_lineEdit.text()
        self.ADD_SCORE = int(self.ADD_SCORE)

        if self.StudentNum_Judge(self.ADD_STUID) == False:
            QMessageBox.critical(self, "ERROR", "学号格式不正确！")
        elif self.Score_Judge(self.ADD_SCORE) == False:
            QMessageBox.critical(self, "ERROR", "成绩输入不正确！")
        else:
            ScoreQ = self.conn.AdminPage_Admin_Add_Score_Query(self.ADD_STUID, self.ADD_COURSE)
            if ScoreQ != None:
                print(ScoreQ)
                stuid = ScoreQ[0]
                stuname = ScoreQ[1]
                stuclass = ScoreQ[2]
                stucourse = ScoreQ[3]
                stucoursecode = ScoreQ[4]
                stuscore = ScoreQ[5]

                text = f"--原纪录--\n学号：{stuid}\n姓名：{stuname}\n班级：{stuclass}\n课程：{stucourse}\n课程代码：{stucoursecode}\n成绩：{stuscore}\n"

                self.State = True
                QMessageBox.information(self, "SUCCEED", "查询成功！")

                self.ui.textBrowser.setText(text)

            else:
                QMessageBox.critical(self, "ERROR", "无记录！")

    def on_button_clicked_Add_pushButton(self):

        # if self.State != True:
        #     QMessageBox.critical(self, "ERROR", "必须先查询！")
        # else:
        #     if self.conn.Admin_Add_StuSel(self.ADD_STUID, self.ADD_COURSE, self.ADD_SCORE):
        #         QMessageBox.information(self, "Success", "添加成功")
        #         self.close()
        #     else:
        #         QMessageBox.critical(self, "Error", "数据输入有误！")
        # self.State = False

        self.ADD_STUID = self.ui.StuNum_lineEdit.text()
        self.ADD_COURSE = self.ui.SourceNo_lineEdit.text()
        self.ADD_SCORE = self.ui.Score_lineEdit.text()
        self.ADD_SCORE = int(self.ADD_SCORE)

        if self.StudentNum_Judge(self.ADD_STUID) == False:
            QMessageBox.critical(self, "ERROR", "学号格式不正确！")
        elif self.Score_Judge(self.ADD_SCORE) == False:
            QMessageBox.critical(self, "ERROR", "成绩输入不正确！")
        else:
            if self.conn.Admin_Add_StuSel(self.ADD_STUID, self.ADD_COURSE, self.ADD_SCORE):
                QMessageBox.information(self, "Success", "添加成功")
                self.close()
            else:
                QMessageBox.critical(self, "Error", "数据输入有误！")