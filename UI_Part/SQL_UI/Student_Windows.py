# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic Student_Windows.ui -o ui_Student_Windows.py
#     pyside6-rcc src.qrc -o src_rc.py
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

        Message_ID[0] = str(Message_ID[0])
        NameQ, RankQ = self.conn.StuPage_Rank_Query(Message_ID[0])
        RCountQ = self.conn.StuPage_Rank_Count_Query()

        fini = self.conn.StuPage_Student_Score_Query(Message_ID[0])
        print(fini)
        self.ui.UserName_label.setText(str(NameQ))
        self.ui.Rank_label.setText(str(RankQ) + '/' + str(RCountQ[0]))



        self.ui.Logout_Button.clicked.connect(self.on_button_clicked_Logout_Button)



    def on_button_clicked_Logout_Button(self):
        self.close()

    def closeEvent(self, event):
        self.closed.emit()  # Emit the custom signal
        super().closeEvent(event)
