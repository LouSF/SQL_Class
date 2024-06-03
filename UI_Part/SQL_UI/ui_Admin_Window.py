# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Admin_Window.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTableView,
    QVBoxLayout, QWidget)
import src_rc

class Ui_Admin_Window(object):
    def setupUi(self, Admin_Window):
        if not Admin_Window.objectName():
            Admin_Window.setObjectName(u"Admin_Window")
        Admin_Window.resize(1005, 808)
        font = QFont()
        font.setFamilies([u".AppleSystemUIFont"])
        Admin_Window.setFont(font)
        self.horizontalLayoutWidget = QWidget(Admin_Window)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(310, 10, 681, 51))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.UserName_label = QLabel(self.horizontalLayoutWidget)
        self.UserName_label.setObjectName(u"UserName_label")
        self.UserName_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.UserName_label)

        self.label_3 = QLabel(self.horizontalLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.label = QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName(u"label")
        palette = QPalette()
        brush = QBrush(QColor(255, 38, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        self.label.setPalette(palette)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(False)

        self.horizontalLayout_2.addWidget(self.label)

        self.Logout_Button = QPushButton(self.horizontalLayoutWidget)
        self.Logout_Button.setObjectName(u"Logout_Button")

        self.horizontalLayout_2.addWidget(self.Logout_Button)

        self.label_2 = QLabel(Admin_Window)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 10, 191, 141))
        self.label_2.setPixmap(QPixmap(u":/new/prefix1/img/t_logo.png"))
        self.label_2.setAlignment(Qt.AlignCenter)
        self.horizontalLayoutWidget_2 = QWidget(Admin_Window)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(309, 90, 681, 51))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.Change_Button = QPushButton(self.horizontalLayoutWidget_2)
        self.Change_Button.setObjectName(u"Change_Button")

        self.horizontalLayout.addWidget(self.Change_Button)

        self.Add_Button = QPushButton(self.horizontalLayoutWidget_2)
        self.Add_Button.setObjectName(u"Add_Button")

        self.horizontalLayout.addWidget(self.Add_Button)

        self.Finish_Input_Button = QPushButton(self.horizontalLayoutWidget_2)
        self.Finish_Input_Button.setObjectName(u"Finish_Input_Button")

        self.horizontalLayout.addWidget(self.Finish_Input_Button)

        self.Del_Button = QPushButton(self.horizontalLayoutWidget_2)
        self.Del_Button.setObjectName(u"Del_Button")

        self.horizontalLayout.addWidget(self.Del_Button)

        self.Output_Button = QPushButton(self.horizontalLayoutWidget_2)
        self.Output_Button.setObjectName(u"Output_Button")

        self.horizontalLayout.addWidget(self.Output_Button)

        self.verticalLayoutWidget = QWidget(Admin_Window)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(180, 160, 811, 641))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.tableView = QTableView(self.verticalLayoutWidget)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout.addWidget(self.tableView)

        self.layoutWidget = QWidget(Admin_Window)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 160, 165, 159))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_5)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4)

        self.StuNum_lineEdit = QLineEdit(self.layoutWidget)
        self.StuNum_lineEdit.setObjectName(u"StuNum_lineEdit")

        self.horizontalLayout_3.addWidget(self.StuNum_lineEdit)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.Query_Button = QPushButton(self.layoutWidget)
        self.Query_Button.setObjectName(u"Query_Button")

        self.verticalLayout_3.addWidget(self.Query_Button)

        self.layoutWidget1 = QWidget(Admin_Window)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 330, 165, 159))
        self.verticalLayout_4 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.layoutWidget1)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_6)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_7 = QLabel(self.layoutWidget1)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_4.addWidget(self.label_7)

        self.Course_lineEdit = QLineEdit(self.layoutWidget1)
        self.Course_lineEdit.setObjectName(u"Course_lineEdit")

        self.horizontalLayout_4.addWidget(self.Course_lineEdit)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.Query_Course_Button = QPushButton(self.layoutWidget1)
        self.Query_Course_Button.setObjectName(u"Query_Course_Button")

        self.verticalLayout_4.addWidget(self.Query_Course_Button)

        self.layoutWidget_2 = QWidget(Admin_Window)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(10, 720, 165, 81))
        self.verticalLayout_5 = QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.Query_Score_Rank_Button = QPushButton(self.layoutWidget_2)
        self.Query_Score_Rank_Button.setObjectName(u"Query_Score_Rank_Button")

        self.verticalLayout_5.addWidget(self.Query_Score_Rank_Button)

        self.layoutWidget_3 = QWidget(Admin_Window)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(10, 500, 165, 159))
        self.verticalLayout_6 = QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.layoutWidget_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_8)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_9 = QLabel(self.layoutWidget_3)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_5.addWidget(self.label_9)

        self.FindScore_lineEdit = QLineEdit(self.layoutWidget_3)
        self.FindScore_lineEdit.setObjectName(u"FindScore_lineEdit")

        self.horizontalLayout_5.addWidget(self.FindScore_lineEdit)


        self.verticalLayout_6.addLayout(self.horizontalLayout_5)

        self.Query_Score_Button = QPushButton(self.layoutWidget_3)
        self.Query_Score_Button.setObjectName(u"Query_Score_Button")

        self.verticalLayout_6.addWidget(self.Query_Score_Button)


        self.retranslateUi(Admin_Window)

        QMetaObject.connectSlotsByName(Admin_Window)
    # setupUi

    def retranslateUi(self, Admin_Window):
        Admin_Window.setWindowTitle(QCoreApplication.translate("Admin_Window", u"ADMIN_Page", None))
        self.UserName_label.setText(QCoreApplication.translate("Admin_Window", u"None", None))
        self.label_3.setText(QCoreApplication.translate("Admin_Window", u"\u4f60\u597d\uff0c\u6b22\u8fce\u56de\u6765\u3002", None))
        self.label.setText(QCoreApplication.translate("Admin_Window", u"\u7ba1\u7406\u5458\u6a21\u5f0f", None))
        self.Logout_Button.setText(QCoreApplication.translate("Admin_Window", u"Logout", None))
        self.label_2.setText("")
        self.Change_Button.setText(QCoreApplication.translate("Admin_Window", u"\u4fee\u6539", None))
        self.Add_Button.setText(QCoreApplication.translate("Admin_Window", u"\u6dfb\u52a0", None))
        self.Finish_Input_Button.setText(QCoreApplication.translate("Admin_Window", u"\u5b8c\u6210\u6dfb\u52a0", None))
        self.Del_Button.setText(QCoreApplication.translate("Admin_Window", u"\u5220\u9664", None))
        self.Output_Button.setText(QCoreApplication.translate("Admin_Window", u"\u5bfc\u51fa\u5f53\u524d\u8868", None))
        self.label_5.setText(QCoreApplication.translate("Admin_Window", u"\u5b66\u751f\u4fe1\u606f\u67e5\u8be2", None))
        self.label_4.setText(QCoreApplication.translate("Admin_Window", u"\u6a21\u7cca\u641c\u7d22", None))
        self.Query_Button.setText(QCoreApplication.translate("Admin_Window", u"\u4fe1\u606f\u67e5\u8be2", None))
        self.label_6.setText(QCoreApplication.translate("Admin_Window", u"\u5f00\u8bfe\u4fe1\u606f\u67e5\u8be2", None))
        self.label_7.setText(QCoreApplication.translate("Admin_Window", u"\u6a21\u7cca\u641c\u7d22", None))
        self.Query_Course_Button.setText(QCoreApplication.translate("Admin_Window", u"\u5f00\u8bfe\u4fe1\u606f\u67e5\u8be2", None))
        self.Query_Score_Rank_Button.setText(QCoreApplication.translate("Admin_Window", u"\u6210\u7ee9\u6392\u540d\u67e5\u8be2", None))
        self.label_8.setText(QCoreApplication.translate("Admin_Window", u"\u6210\u7ee9\u4fe1\u606f\u67e5\u8be2", None))
        self.label_9.setText(QCoreApplication.translate("Admin_Window", u"\u6a21\u7cca\u641c\u7d22", None))
        self.Query_Score_Button.setText(QCoreApplication.translate("Admin_Window", u"\u6210\u7ee9\u67e5\u8be2", None))
    # retranslateUi

