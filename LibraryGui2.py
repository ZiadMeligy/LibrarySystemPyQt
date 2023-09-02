from main import Book, Section, Library
from PyQt5 import QtCore, QtGui, QtWidgets
from LibraryLogic import LibraryLogic
from AddBookWindow import Ui_Diagloooog
import tkinter
from tkinter import filedialog
import settings



LibraryInstance = LibraryLogic()


class Ui_LibrarySystem(object):
    
    def setupUi(self, LibrarySystem):
        
        
        self.logic = LibraryInstance
        self.logic.MainLib.setName(settings.LibraryName)
        LibrarySystem.setObjectName("LibrarySystem")
        LibrarySystem.resize(1100, 700)
        LibrarySystem.setStyleSheet("table {\n"
"  border-collapse: collapse;\n"
"}\n"
" th {\n"
"  background: #ccc;\n"
"}\n"
"\n"
"th, td {\n"
"  border: 1px solid #ccc;\n"
"  padding: 8px;\n"
"}\n"
"\n"
"tr:nth-child(even) {\n"
"  background: #efefef;\n"
"}\n"
"\n"
"tr:hover {\n"
"  background: #d1d1d1;\n"
"}")
        LibrarySystem.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(LibrarySystem)
        self.centralwidget.setStyleSheet("background: #181818;")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:white")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.profitlabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(22)
        self.profitlabel.setFont(font)
        self.profitlabel.setStyleSheet("color:white")
        self.profitlabel.setObjectName("profitlabel")
        self.verticalLayout_2.addWidget(self.profitlabel)
        self.noBooks = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(22)
        self.noBooks.setFont(font)
        self.noBooks.setStyleSheet("color:white")
        self.noBooks.setObjectName("noBooks")
        self.verticalLayout_2.addWidget(self.noBooks)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setStyleSheet("color:white")
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.noSections = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(22)
        self.noSections.setFont(font)
        self.noSections.setStyleSheet("color:white")
        self.noSections.setObjectName("noSections")
        self.verticalLayout_2.addWidget(self.noSections)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.AddBookBtn = QtWidgets.QPushButton(self.centralwidget,clicked= lambda: self.OpenAddWindow())
        self.AddBookBtn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        self.AddBookBtn.setFont(font)
        self.AddBookBtn.setStyleSheet("color:black;\n"
"background-color: #03D8F1;\n"
"border-radius:8px;")
        self.AddBookBtn.setObjectName("AddBookBtn")
        self.horizontalLayout_6.addWidget(self.AddBookBtn)
        self.AddSectionBtn = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.OpenWindowsExplorer())
        self.AddSectionBtn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        self.AddSectionBtn.setFont(font)
        self.AddSectionBtn.setStyleSheet("color:black;\n"
"background-color: #03D8F1;\n"
"border-radius:8px;")
        self.AddSectionBtn.setObjectName("AddSectionBtn")
        self.horizontalLayout_6.addWidget(self.AddSectionBtn)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.ExportDataBtn = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.sell_book() )
        self.ExportDataBtn.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.ExportDataBtn.setFont(font)
        self.ExportDataBtn.setStyleSheet("color:black;\n"
"background-color: #03D8F1;\n"
"border-radius:8px;")
        self.ExportDataBtn.setObjectName("ExportDataBtn")
        self.horizontalLayout_2.addWidget(self.ExportDataBtn)
        self.ImportDataBtn = QtWidgets.QPushButton(self.centralwidget, clicked=self.import_data_clicked)
        self.ImportDataBtn.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.ImportDataBtn.setFont(font)
        self.ImportDataBtn.setStyleSheet("color:black;\n"
"background-color: #03D8F1;\n"
"border-radius:8px;")
        self.ImportDataBtn.setObjectName("ImportDataBtn")
        self.horizontalLayout_2.addWidget(self.ImportDataBtn)
        self.SellBookBtn = QtWidgets.QPushButton(self.centralwidget,clicked= lambda: self.searchButton())
        self.SellBookBtn.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.SellBookBtn.setFont(font)
        self.SellBookBtn.setStyleSheet("color:black;\n"
"background-color: #03D8F1;\n"
"border-radius:8px;")
        self.SellBookBtn.setObjectName("SellBookBtn")
        self.horizontalLayout_2.addWidget(self.SellBookBtn)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.tableWidget.setFont(font)
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setStyleSheet("QTableView::item:selected {\n"
"color:white;\n"
"background: #000000;\n"
"font-weight:900;\n"
"\n"
"}\n"
"QTableView{\n"
"color:white;"
"}"
"QHeaderView::section {\n"
"color:white;\n"
"background-color:#232326;\n"
"\n"
"}")
        self.tableWidget.setShowGrid(False)
        self.tableWidget.setCornerButtonEnabled(False)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("color: black;\n"
                                    "background-color: white;\n"
                                    "border-radius: 8px;")
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)  # Add the line edit to the layout

        self.horizontalLayout_3.addWidget(self.tableWidget)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        LibrarySystem.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(LibrarySystem)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 826, 21))
        self.menubar.setObjectName("menubar")
        LibrarySystem.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(LibrarySystem)
        self.statusbar.setObjectName("statusbar")
        LibrarySystem.setStatusBar(self.statusbar)
        
        


        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        print(settings.LibraryName)
        self.logic.TableWidget = self.tableWidget
        self.logic.bookNoInstance=self.label
        self.logic.SecNoInstance=self.noSections



        self.retranslateUi(LibrarySystem)
        QtCore.QMetaObject.connectSlotsByName(LibrarySystem)


    def searchButton(self):
        if self.SellBookBtn.text()=="Reset Search":
            self.SellBookBtn.setText("Search")
            self.logic.populate_table()
            return
        searchedBooks=[]
        title = self.lineEdit.text()
        searchedBooks = self.logic.MainLib.searchBookByTitle(title)
        if len(searchedBooks)==0:
            searchedBooks=self.logic.MainLib.searchBookByAuthor(title)
            if(len(searchedBooks)==0):
                print("No results found :)")
        self.logic.SearchCritera(searchedBooks)
        self.SellBookBtn.setText("Reset Search")

            


    def import_data_clicked(self):
        tkinter.Tk().withdraw()
        file_path = filedialog.askopenfilename()
        self.logic.MainLib.lOAD_DATA(pathFile = file_path)
        self.logic.populate_table()    
        self.logic.updateBookNumber()
        self.logic.updateSectionsNumber()

#     def populate_table(self):
#         # Clear the existing table
#         self.tableWidget.setRowCount(len(self.logic.MainLib.booklist))
#         row=0
#         for book in self.logic.MainLib.booklist:
#             title = book.title
#             Author= book.author
#             Cost = book.cost
#             Section = book.section.title
#             self.tableWidget.setItem(row, 0,QtWidgets.QTableWidgetItem(title))
#             self.tableWidget.setItem(row, 1,QtWidgets.QTableWidgetItem(Author))
#             self.tableWidget.setItem(row, 2,QtWidgets.QTableWidgetItem(str(Cost)))
#             self.tableWidget.setItem(row, 3,QtWidgets.QTableWidgetItem(Section))
#             row = row+1



    def sell_book(self):
        self.logic.SellBook()
        self.updateProfitLabel(self.logic.MainLib.profit)
        self.updateItemsSoldNumberLabel(self.logic.MainLib.itemsSold)
        self.logic.updateBookNumber()
        self.logic.updateSectionsNumber()

    def OpenAddWindow(self):
        print("clicked")
        self.add_dialog = QtWidgets.QDialog()
        self.add_ui = Ui_Diagloooog()
        self.add_ui.logic = self.logic  
        self.add_ui.setupUi(self.add_dialog)
        self.add_dialog.show()
        
    def updateItemsSoldNumberLabel(self,newnumber):
        self.noBooks.setText(f'No. of Books Sold: {newnumber}')


    def updateSectionsNumber(self):
        self.noSections.setText(f'Books in Store: {len(self.logic.MainLib.sections)}')


    def updateProfitLabel(self,newProfit):
        self.profitlabel.setText(f'Total Profit: ${newProfit}')


    def OpenWindowsExplorer(self):
        
        self.logic.MainLib.ExportLibData()
   
        

    def retranslateUi(self, LibrarySystem):
        _translate = QtCore.QCoreApplication.translate
        LibrarySystem.setWindowTitle(_translate("LibrarySystem", "MainWindow"))
        self.label_2.setText(_translate("LibrarySystem", f"Library Name: {self.logic.MainLib.title}"))
        self.profitlabel.setText(_translate("LibrarySystem", f"Total Profit:"))
        self.noBooks.setText(_translate("LibrarySystem", "No. of Books Sold:"))
        self.label.setText(_translate("LibrarySystem", "Books in Store:"))
        self.noSections.setText(_translate("LibrarySystem", "No. of Sections:"))
        self.AddBookBtn.setText(_translate("LibrarySystem", "ADD BOOK"))
        self.AddSectionBtn.setText(_translate("LibrarySystem", "SAVE DATA"))
        self.ExportDataBtn.setText(_translate("LibrarySystem", "SELL BOOK"))
        self.ImportDataBtn.setText(_translate("LibrarySystem", "IMPORT DATA"))
        self.SellBookBtn.setText(_translate("LibrarySystem", "Search"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("LibrarySystem", "Title"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("LibrarySystem", "Author"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("LibrarySystem", "Cost"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("LibrarySystem", "Section"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LibrarySystem = QtWidgets.QMainWindow()
    ui = Ui_LibrarySystem()
    ui.setupUi(LibrarySystem)
    LibrarySystem.show()
    sys.exit(app.exec_())
