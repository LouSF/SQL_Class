# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Student_Windows.ui'
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
    QPushButton, QSizePolicy, QSpacerItem, QTableView,
    QVBoxLayout, QWidget)
import src_rc

class Ui_Students_Windows(object):
    def setupUi(self, Students_Windows):
        if not Students_Windows.objectName():
            Students_Windows.setObjectName(u"Students_Windows")
        Students_Windows.resize(1000, 700)
        self.horizontalLayoutWidget = QWidget(Students_Windows)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(310, 10, 681, 51))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label = QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.UserName_label = QLabel(self.horizontalLayoutWidget)
        self.UserName_label.setObjectName(u"UserName_label")

        self.horizontalLayout.addWidget(self.UserName_label)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.label_2 = QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.Rank_label = QLabel(self.horizontalLayoutWidget)
        self.Rank_label.setObjectName(u"Rank_label")

        self.horizontalLayout.addWidget(self.Rank_label)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.Logout_Button = QPushButton(self.horizontalLayoutWidget)
        self.Logout_Button.setObjectName(u"Logout_Button")

        self.horizontalLayout.addWidget(self.Logout_Button)

        self.label_img = QLabel(Students_Windows)
        self.label_img.setObjectName(u"label_img")
        self.label_img.setGeometry(QRect(70, -10, 181, 161))
        self.label_img.setPixmap(QPixmap(u":/new/prefix1/img/t_logo.png"))
        self.label_img.setAlignment(Qt.AlignCenter)
        self.horizontalLayoutWidget_2 = QWidget(Students_Windows)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(310, 70, 681, 80))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.Course_Output_Button = QPushButton(self.horizontalLayoutWidget_2)
        self.Course_Output_Button.setObjectName(u"Course_Output_Button")

        self.horizontalLayout_3.addWidget(self.Course_Output_Button)

        self.Score_Output_Button = QPushButton(self.horizontalLayoutWidget_2)
        self.Score_Output_Button.setObjectName(u"Score_Output_Button")

        self.horizontalLayout_3.addWidget(self.Score_Output_Button)

        self.verticalLayoutWidget = QWidget(Students_Windows)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 160, 481, 531))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_5)

        self.Score_tableView = QTableView(self.verticalLayoutWidget)
        self.Score_tableView.setObjectName(u"Score_tableView")

        self.verticalLayout.addWidget(self.Score_tableView)

        self.verticalLayoutWidget_2 = QWidget(Students_Windows)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(510, 160, 481, 531))
        self.verticalLayout_4 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.verticalLayoutWidget_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_8)

        self.Course_tableView = QTableView(self.verticalLayoutWidget_2)
        self.Course_tableView.setObjectName(u"Course_tableView")

        self.verticalLayout_4.addWidget(self.Course_tableView)

        self.User_Help = QPushButton(Students_Windows)
        self.User_Help.setObjectName(u"User_Help")
        self.User_Help.setGeometry(QRect(10, 0, 21, 31))

        self.retranslateUi(Students_Windows)

        QMetaObject.connectSlotsByName(Students_Windows)
    # setupUi

    def retranslateUi(self, Students_Windows):
        Students_Windows.setWindowTitle(QCoreApplication.translate("Students_Windows", u"STUDENT_Page", None))
        self.label.setText(QCoreApplication.translate("Students_Windows", u"\u4f60\u597d\uff0c", None))
        self.UserName_label.setText(QCoreApplication.translate("Students_Windows", u"None", None))
        self.label_2.setText(QCoreApplication.translate("Students_Windows", u"\u4f60\u7684\u6392\u540d\u4e3a\uff1a", None))
        self.Rank_label.setText(QCoreApplication.translate("Students_Windows", u"None", None))
        self.Logout_Button.setText(QCoreApplication.translate("Students_Windows", u"Logout", None))
        self.label_img.setText("")
        self.Course_Output_Button.setText(QCoreApplication.translate("Students_Windows", u"\u5bfc\u51fa\u5f00\u8bfe\u60c5\u51b5", None))
        self.Score_Output_Button.setText(QCoreApplication.translate("Students_Windows", u"\u5bfc\u51fa\u6210\u7ee9\u60c5\u51b5", None))
        self.label_5.setText(QCoreApplication.translate("Students_Windows", u"\u6210\u7ee9\u60c5\u51b5", None))
        self.label_8.setText(QCoreApplication.translate("Students_Windows", u"\u5f00\u8bfe\u60c5\u51b5", None))
        self.User_Help.setText(QCoreApplication.translate("Students_Windows", u"?", None))
    # retranslateUi

