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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QWidget)

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
        self.label = QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.UserName_label = QLabel(self.horizontalLayoutWidget)
        self.UserName_label.setObjectName(u"UserName_label")

        self.horizontalLayout.addWidget(self.UserName_label)

        self.label_2 = QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.Rank_label = QLabel(self.horizontalLayoutWidget)
        self.Rank_label.setObjectName(u"Rank_label")

        self.horizontalLayout.addWidget(self.Rank_label)

        self.Logout_Button = QPushButton(self.horizontalLayoutWidget)
        self.Logout_Button.setObjectName(u"Logout_Button")

        self.horizontalLayout.addWidget(self.Logout_Button)


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
    # retranslateUi

