
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_IntroWindow(object):
    def setupUi(self, IntroWindow):
        IntroWindow.setObjectName("IntroWindow")
        IntroWindow.resize(596, 203)
        IntroWindow.setStyleSheet("background: #181818;")
        self.centralwidget = QtWidgets.QWidget(IntroWindow)
        self.centralwidget.setStyleSheet("background:")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("color:white")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setStyleSheet("background:white")
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget,)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton2.sizePolicy().hasHeightForWidth())
        self.pushButton2.setSizePolicy(sizePolicy)
        self.pushButton2.setMinimumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton2.setFont(font)
        self.pushButton2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton2.setStyleSheet("color:black;\n"
"background-color: #03D8F1;\n"
"border-radius:8px;")
        self.pushButton2.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout.addLayout(self.verticalLayout)
        IntroWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(IntroWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 596, 21))
        self.menubar.setObjectName("menubar")
        IntroWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(IntroWindow)
        self.statusbar.setObjectName("statusbar")
        IntroWindow.setStatusBar(self.statusbar)

        self.retranslateUi(IntroWindow)
        QtCore.QMetaObject.connectSlotsByName(IntroWindow)

    def retranslateUi(self, IntroWindow):
        _translate = QtCore.QCoreApplication.translate
        IntroWindow.setWindowTitle(_translate("IntroWindow", "MainWindow"))
        self.label.setText(_translate("IntroWindow", "Hello There, Please type out your Library Name."))
        self.pushButton2.setText(_translate("IntroWindow", "SUBMIT"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    IntroWindow = QtWidgets.QMainWindow()
    ui = Ui_IntroWindow()
    ui.setupUi(IntroWindow)
    IntroWindow.show()
    sys.exit(app.exec_())
