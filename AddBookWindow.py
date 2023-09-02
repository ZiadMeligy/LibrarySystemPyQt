
from main import Book,Section,Library



from PyQt5 import QtCore, QtGui, QtWidgets

tableWidgetInstance=None

class Ui_Diagloooog(object):
    def setupUi(self, Diagloooog):
        self.dialog=Diagloooog 
        Diagloooog.setObjectName("Diagloooog")
        Diagloooog.resize(300, 233)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Diagloooog.sizePolicy().hasHeightForWidth())
        Diagloooog.setSizePolicy(sizePolicy)
        Diagloooog.setMaximumSize(QtCore.QSize(300, 233))
        Diagloooog.setStyleSheet("color:white;\n"
"background:#141414\n"
"")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Diagloooog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label = QtWidgets.QLabel(Diagloooog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_6.addWidget(self.label)
        self.verticalLayout.addLayout(self.verticalLayout_6)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.TitleLabel = QtWidgets.QLabel(Diagloooog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TitleLabel.sizePolicy().hasHeightForWidth())
        self.TitleLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.TitleLabel.setFont(font)
        self.TitleLabel.setObjectName("TitleLabel")
        self.verticalLayout_4.addWidget(self.TitleLabel)
        self.AuthorLabel = QtWidgets.QLabel(Diagloooog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AuthorLabel.sizePolicy().hasHeightForWidth())
        self.AuthorLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.AuthorLabel.setFont(font)
        self.AuthorLabel.setObjectName("AuthorLabel")
        self.verticalLayout_4.addWidget(self.AuthorLabel)
        self.CostLabel = QtWidgets.QLabel(Diagloooog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CostLabel.sizePolicy().hasHeightForWidth())
        self.CostLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.CostLabel.setFont(font)
        self.CostLabel.setObjectName("CostLabel")
        self.verticalLayout_4.addWidget(self.CostLabel)
        self.SectionLabel = QtWidgets.QLabel(Diagloooog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SectionLabel.sizePolicy().hasHeightForWidth())
        self.SectionLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.SectionLabel.setFont(font)
        self.SectionLabel.setObjectName("SectionLabel")
        self.verticalLayout_4.addWidget(self.SectionLabel)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.AddTitleText = QtWidgets.QLineEdit(Diagloooog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AddTitleText.sizePolicy().hasHeightForWidth())
        self.AddTitleText.setSizePolicy(sizePolicy)
        self.AddTitleText.setObjectName("AddTitleText")
        self.verticalLayout_5.addWidget(self.AddTitleText)
        self.AddAuthorText = QtWidgets.QLineEdit(Diagloooog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AddAuthorText.sizePolicy().hasHeightForWidth())
        self.AddAuthorText.setSizePolicy(sizePolicy)
        self.AddAuthorText.setObjectName("AddAuthorText")
        self.verticalLayout_5.addWidget(self.AddAuthorText)
        self.AddCostText = QtWidgets.QLineEdit(Diagloooog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AddCostText.sizePolicy().hasHeightForWidth())
        self.AddCostText.setSizePolicy(sizePolicy)
        self.AddCostText.setObjectName("AddCostText")
        self.verticalLayout_5.addWidget(self.AddCostText)
        self.AddSectionText = QtWidgets.QLineEdit(Diagloooog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AddSectionText.sizePolicy().hasHeightForWidth())
        self.AddSectionText.setSizePolicy(sizePolicy)
        self.AddSectionText.setObjectName("AddSectionText")
        self.verticalLayout_5.addWidget(self.AddSectionText)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.SubmitAddBtn = QtWidgets.QPushButton(Diagloooog, clicked= lambda:self.AddBook())
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SubmitAddBtn.sizePolicy().hasHeightForWidth())
        self.SubmitAddBtn.setSizePolicy(sizePolicy)
        self.SubmitAddBtn.setMinimumSize(QtCore.QSize(160, 40))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.SubmitAddBtn.setFont(font)
        self.SubmitAddBtn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.SubmitAddBtn.setStyleSheet("background:white;\n"
"color: black;\n"
"border-radius:5px\n"
"")
        self.SubmitAddBtn.setObjectName("SubmitAddBtn")
        self.horizontalLayout_2.addWidget(self.SubmitAddBtn)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Diagloooog)
        QtCore.QMetaObject.connectSlotsByName(Diagloooog)

    def retranslateUi(self, Diagloooog):
        _translate = QtCore.QCoreApplication.translate
        Diagloooog.setWindowTitle(_translate("Diagloooog", "Dialog"))
        self.label.setText(_translate("Diagloooog", "Please Add your Book "))
        self.TitleLabel.setText(_translate("Diagloooog", "Book Title"))
        self.AuthorLabel.setText(_translate("Diagloooog", "Author"))
        self.CostLabel.setText(_translate("Diagloooog", "Book Cost"))
        self.SectionLabel.setText(_translate("Diagloooog", "Section"))
        self.SubmitAddBtn.setText(_translate("Diagloooog", "Submit"))

    def AddBook(self):
        from LibraryGui2 import LibraryInstance

        Booktitle = self.AddTitleText.text()
        BookAuthor = self.AddAuthorText.text()
        BookCostText = self.AddCostText.text()
        BookSection = self.AddSectionText.text()

        if BookAuthor == "" or Booktitle == "" or BookCostText == "" or BookSection == "":
            print("All Fields Are Required. Please Fill them and try again")
            return
        else:
            try:
                BookCost = int(BookCostText)  # Convert to integer here
            except ValueError:
                print(f"Invalid input for cost: '{BookCostText}'. Cost must be an integer.")
                self.AddCostText.clear()
                return

            new_book = Book(title=Booktitle, author= BookAuthor, cost= BookCost, section= BookSection)
            section = None
            for libSection in LibraryInstance.MainLib.sections:
                if BookSection == libSection.title:
                    section = libSection
                    break
            
            if section is None:
                section = Section(BookSection) 
                LibraryInstance.MainLib.addSection(section)   

            section.addBook(new_book)
            new_book.section = section
            LibraryInstance.MainLib.booklist.append(new_book)
            LibraryInstance.populate_table()
            LibraryInstance.updateBookNumber()
            LibraryInstance.updateSectionsNumber()

            self.dialog.close()

            
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Diagloooog = QtWidgets.QDialog()
    ui = Ui_Diagloooog()
    ui.setupUi(Diagloooog)
    ui.dialog= Diagloooog
    Diagloooog.show()
    sys.exit(app.exec_())
