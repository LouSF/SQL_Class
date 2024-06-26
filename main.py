import sys
import os
from PyQt6.QtWidgets import QWidget, QApplication

sys.path.append(os.path.join(os.path.dirname(__file__), 'SQL_Part'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'UI_Part/SQL_UI'))

from UI_Part.SQL_UI.Login_window import *
from UI_Part.SQL_UI.Student_Windows import *
from SQL_Part.SQL import *


if __name__ == "__main__":
    app = QApplication(sys.argv)
    Lwindows = Login_Window()
    Lwindows.show()
    sys.exit(app.exec())