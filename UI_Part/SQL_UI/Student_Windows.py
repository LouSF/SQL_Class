# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic Student_Windows.ui -o ui_Student_Windows.py
from ui_Student_Windows import Ui_Students_Windows
from PySide6.QtCore import Signal

from SQL_Part.SQL import *
from State import *

class Students_Windows(QWidget):
    closed = Signal()
    def __init__(self, Message_ID, parent=None):
        super().__init__(parent)
        self.ui = Ui_Students_Windows()
        self.ui.setupUi(self)

        self.conn = SQL(connectionString)

        self.ui.UserName_label = Message_ID[0]



        self.ui.Rank_label.setText()

        self.ui.Logout_Button.clicked.connect(self.on_button_clicked_Logout_Button)


    def Rank_Query(self) -> str:


    def on_button_clicked_Logout_Button(self):
        self.close()

    def closeEvent(self, event):
        self.closed.emit()  # Emit the custom signal
        super().closeEvent(event)
