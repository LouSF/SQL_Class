# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Admin_Add.ui'
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
    QPushButton, QSizePolicy, QTextBrowser, QVBoxLayout,
    QWidget)

class Ui_Admin_Add(object):
    def setupUi(self, Admin_Add):
        if not Admin_Add.objectName():
            Admin_Add.setObjectName(u"Admin_Add")
        Admin_Add.resize(400, 300)
        self.Admin_Add_Q_pushButton = QPushButton(Admin_Add)
        self.Admin_Add_Q_pushButton.setObjectName(u"Admin_Add_Q_pushButton")
        self.Admin_Add_Q_pushButton.setGeometry(QRect(50, 250, 100, 32))
        self.Admin_Add_pushButton = QPushButton(Admin_Add)
        self.Admin_Add_pushButton.setObjectName(u"Admin_Add_pushButton")
        self.Admin_Add_pushButton.setGeometry(QRect(210, 250, 100, 32))
        self.verticalLayoutWidget = QWidget(Admin_Add)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 160, 91))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.StuNum_lineEdit = QLineEdit(self.verticalLayoutWidget)
        self.StuNum_lineEdit.setObjectName(u"StuNum_lineEdit")

        self.horizontalLayout.addWidget(self.StuNum_lineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.CourseNo_label = QLabel(self.verticalLayoutWidget)
        self.CourseNo_label.setObjectName(u"CourseNo_label")

        self.horizontalLayout_2.addWidget(self.CourseNo_label)

        self.SourceNo_lineEdit = QLineEdit(self.verticalLayoutWidget)
        self.SourceNo_lineEdit.setObjectName(u"SourceNo_lineEdit")

        self.horizontalLayout_2.addWidget(self.SourceNo_lineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.Score_lineEdit = QLineEdit(self.verticalLayoutWidget)
        self.Score_lineEdit.setObjectName(u"Score_lineEdit")

        self.horizontalLayout_3.addWidget(self.Score_lineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.textBrowser = QTextBrowser(Admin_Add)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(190, 10, 201, 191))

        self.retranslateUi(Admin_Add)

        QMetaObject.connectSlotsByName(Admin_Add)
    # setupUi

    def retranslateUi(self, Admin_Add):
        Admin_Add.setWindowTitle(QCoreApplication.translate("Admin_Add", u"Form", None))
        self.Admin_Add_Q_pushButton.setText(QCoreApplication.translate("Admin_Add", u"Q", None))
        self.Admin_Add_pushButton.setText(QCoreApplication.translate("Admin_Add", u"Add", None))
        self.label.setText(QCoreApplication.translate("Admin_Add", u"\u5b66\u53f7", None))
        self.CourseNo_label.setText(QCoreApplication.translate("Admin_Add", u"\u8bfe\u7a0b\u53f7", None))
        self.label_2.setText(QCoreApplication.translate("Admin_Add", u"\u5206\u6570", None))
    # retranslateUi

