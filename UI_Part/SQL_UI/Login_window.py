# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic Login_window.ui -o ui_Login_window.py, or
#     pyside2-uic Login_window.ui -o ui_Login_window.py
from ui_Login_window import Ui_Login_windows

from SQL_Part.SQL import *
from Student_Windows import *
from Admin_window import *
from State import *
import re




class Login_Window(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Login_windows()
        self.ui.setupUi(self)

        self.conn = SQL(connectionString)

        self.ui.Login_Button.clicked.connect(self.on_button_clicked_Login_Button)
        self.ui.Register_Button.clicked.connect(self.on_button_clicked_Register_Button)

    def OpenWindows(self, Message_ID):
        if Message_ID[2] == False:
            self.Swindows = Students_Windows(Message_ID)
            self.Swindows.show()
            self.Swindows.closed.connect(self.show_login_window)  # Connect the close signal to show_login_window

        else:
            self.Awindows = Admin_Windows(Message_ID)
            self.Awindows.show()
            self.Awindows.closed.connect(self.show_login_window)  # Connect the close signal to show_login_window

    def show_login_window(self):
        self.show()

    def Password_Judge(self, password) -> bool:
        if len(password) < 6:
            QMessageBox.critical(self, "ERROR", "密码长度必须不小于6位！")
            return False
        # 检查密码复杂性
        if not re.search(r"[A-Z]", password):
            QMessageBox.critical(self, "ERROR", "密码必须包含至少一个大写字母！")
            return False
        if not re.search(r"[a-z]", password):
            QMessageBox.critical(self, "ERROR", "密码必须包含至少一个小写字母！")
            return False
        if not re.search(r"\d", password):
            QMessageBox.critical(self, "ERROR", "密码必须包含至少一个数字！")
            return False
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            QMessageBox.critical(self, "ERROR", "密码必须包含至少一个特殊字符！")
            return False
        return True

    def on_button_clicked_Register_Button(self):
        username = self.ui.User_lineEdit.text()
        password = self.ui.Password_lineEdit.text()

        if self.Password_Judge(password) == True:
            RegisterQ = self.conn.LoginPage_Register_Query(username)
            if RegisterQ == False:
                QMessage_result = QMessageBox.question(self, "Attation", "在DB中不存在该项记录，完成注册后将不能访问任何数据，是否继续？",
                                              QMessageBox.Yes | QMessageBox.No)

            if RegisterQ == True or QMessage_result == QMessageBox.Yes:
                RegisterR = self.conn.LoginPage_Register(username, password, False)

                if RegisterR is None:
                    QMessageBox.critical(self, "ERROR", "已存在账号！")
                else:
                    QMessageBox.information(self, "SUCCEED", "成功注册！")

    def on_button_clicked_Login_Button(self):
        username = self.ui.User_lineEdit.text()
        password = self.ui.Password_lineEdit.text()
        LoginR = self.conn.LoginPage_Login(username, password)

        if LoginR is None:
            QMessageBox.critical(self, "ERROR", "账号或密码错误！")
        else:
            QMessageBox.information(self, "SUCCEED", "登录成功！")
            self.hide()
            self.OpenWindows(LoginR)