# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Login_window.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Login_windows(object):
    def setupUi(self, Login_windows):
        if not Login_windows.objectName():
            Login_windows.setObjectName(u"Login_windows")
        Login_windows.resize(465, 218)
        self.verticalLayoutWidget = QWidget(Login_windows)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(160, 120, 160, 80))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Login_Button = QPushButton(self.verticalLayoutWidget)
        self.Login_Button.setObjectName(u"Login_Button")

        self.verticalLayout.addWidget(self.Login_Button)

        self.Register_Button = QPushButton(self.verticalLayoutWidget)
        self.Register_Button.setObjectName(u"Register_Button")

        self.verticalLayout.addWidget(self.Register_Button)

        self.horizontalLayoutWidget = QWidget(Login_windows)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(20, 20, 431, 80))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)

        self.label_3 = QLabel(self.horizontalLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_3)


        self.horizontalLayout_3.addLayout(self.verticalLayout_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.User_lineEdit = QLineEdit(self.horizontalLayoutWidget)
        self.User_lineEdit.setObjectName(u"User_lineEdit")

        self.verticalLayout_2.addWidget(self.User_lineEdit)

        self.Password_lineEdit = QLineEdit(self.horizontalLayoutWidget)
        self.Password_lineEdit.setObjectName(u"Password_lineEdit")

        self.verticalLayout_2.addWidget(self.Password_lineEdit)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)


        self.retranslateUi(Login_windows)

        QMetaObject.connectSlotsByName(Login_windows)
    # setupUi

    def retranslateUi(self, Login_windows):
        Login_windows.setWindowTitle(QCoreApplication.translate("Login_windows", u"Login_SQL_LSF", None))
        self.Login_Button.setText(QCoreApplication.translate("Login_windows", u"Login", None))
        self.Register_Button.setText(QCoreApplication.translate("Login_windows", u"\u6ce8\u518c", None))
        self.label.setText(QCoreApplication.translate("Login_windows", u"\u7528\u6237\u540d", None))
        self.label_3.setText(QCoreApplication.translate("Login_windows", u"Password", None))
    # retranslateUi

