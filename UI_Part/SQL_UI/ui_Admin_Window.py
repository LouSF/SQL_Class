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
        self.StudentInfoM_Button = QPushButton(self.horizontalLayoutWidget_2)
        self.StudentInfoM_Button.setObjectName(u"StudentInfoM_Button")

        self.horizontalLayout.addWidget(self.StudentInfoM_Button)

        self.StudentScoreM_Button = QPushButton(self.horizontalLayoutWidget_2)
        self.StudentScoreM_Button.setObjectName(u"StudentScoreM_Button")

        self.horizontalLayout.addWidget(self.StudentScoreM_Button)

        self.Advance_Button = QPushButton(self.horizontalLayoutWidget_2)
        self.Advance_Button.setObjectName(u"Advance_Button")

        self.horizontalLayout.addWidget(self.Advance_Button)

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

        self.widget = QWidget(Admin_Window)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 160, 165, 159))
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_5)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4)

        self.StuNum_lineEdit = QLineEdit(self.widget)
        self.StuNum_lineEdit.setObjectName(u"StuNum_lineEdit")

        self.horizontalLayout_3.addWidget(self.StuNum_lineEdit)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.Query_Button = QPushButton(self.widget)
        self.Query_Button.setObjectName(u"Query_Button")

        self.verticalLayout_3.addWidget(self.Query_Button)

        self.layoutWidget = QWidget(Admin_Window)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 330, 165, 159))
        self.verticalLayout_4 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_6)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_7 = QLabel(self.layoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_4.addWidget(self.label_7)

        self.Course_lineEdit = QLineEdit(self.layoutWidget)
        self.Course_lineEdit.setObjectName(u"Course_lineEdit")

        self.horizontalLayout_4.addWidget(self.Course_lineEdit)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.Query_Course_Button = QPushButton(self.layoutWidget)
        self.Query_Course_Button.setObjectName(u"Query_Course_Button")

        self.verticalLayout_4.addWidget(self.Query_Course_Button)

        self.layoutWidget_2 = QWidget(Admin_Window)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(10, 500, 165, 81))
        self.verticalLayout_5 = QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.Query_Score_Button = QPushButton(self.layoutWidget_2)
        self.Query_Score_Button.setObjectName(u"Query_Score_Button")

        self.verticalLayout_5.addWidget(self.Query_Score_Button)

        self.Query_Score_Rank_Button = QPushButton(self.layoutWidget_2)
        self.Query_Score_Rank_Button.setObjectName(u"Query_Score_Rank_Button")

        self.verticalLayout_5.addWidget(self.Query_Score_Rank_Button)


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
        self.StudentInfoM_Button.setText(QCoreApplication.translate("Admin_Window", u"\u5b66\u751f\u4fe1\u606f\u7ba1\u7406", None))
        self.StudentScoreM_Button.setText(QCoreApplication.translate("Admin_Window", u"\u5b66\u751f\u6210\u7ee9\u7ba1\u7406", None))
        self.Advance_Button.setText(QCoreApplication.translate("Admin_Window", u"\u9ad8\u7ea7\u6a21\u5f0f", None))
        self.Output_Button.setText(QCoreApplication.translate("Admin_Window", u"\u5bfc\u51fa\u5f53\u524d\u8868", None))
        self.label_5.setText(QCoreApplication.translate("Admin_Window", u"\u5b66\u751f\u6210\u7ee9\u4fe1\u606f\u67e5\u8be2", None))
        self.label_4.setText(QCoreApplication.translate("Admin_Window", u"\u5b66\u53f7", None))
        self.Query_Button.setText(QCoreApplication.translate("Admin_Window", u"\u4fe1\u606f\u67e5\u8be2", None))
        self.label_6.setText(QCoreApplication.translate("Admin_Window", u"\u5f00\u8bfe\u4fe1\u606f\u67e5\u8be2", None))
        self.label_7.setText(QCoreApplication.translate("Admin_Window", u"\u8bfe\u7a0b\u6a21\u7cca\u641c\u7d22", None))
        self.Query_Course_Button.setText(QCoreApplication.translate("Admin_Window", u"\u5f00\u8bfe\u4fe1\u606f\u67e5\u8be2", None))
        self.Query_Score_Button.setText(QCoreApplication.translate("Admin_Window", u"\u6210\u7ee9\u603b\u8868\u67e5\u8be2", None))
        self.Query_Score_Rank_Button.setText(QCoreApplication.translate("Admin_Window", u"\u6210\u7ee9\u6392\u540d\u67e5\u8be2", None))
    # retranslateUi

