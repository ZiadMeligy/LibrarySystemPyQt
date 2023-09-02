from PyQt5 import QtGui
from main import Book,Section,Library
from PyQt5 import QtCore, QtGui, QtWidgets

class LibraryLogic:
    def __init__(self):
        self.MainLib = Library()
        self.TableWidget = None
        self.bookNoInstance = None
        self.SecNoInstance = None

        



    def populate_table(self):
     
        self.TableWidget.setRowCount(len(self.MainLib.booklist))
        row=0
        for book in self.MainLib.booklist:
            title = book.title
            Author= book.author
            Cost = book.cost
            Section = book.section.title
            self.TableWidget.setItem(row, 0,QtWidgets.QTableWidgetItem(title))
            self.TableWidget.setItem(row, 1,QtWidgets.QTableWidgetItem(Author))
            self.TableWidget.setItem(row, 2,QtWidgets.QTableWidgetItem(str(Cost)))
            self.TableWidget.setItem(row, 3,QtWidgets.QTableWidgetItem(Section))
            row = row+1
        

    def SearchCritera(self,searchedBooks):
        self.TableWidget.clearContents()   
        self.TableWidget.setRowCount(0)
        self.TableWidget.setRowCount(len(searchedBooks))
        row = 0 
        for book in searchedBooks:
            title = book.title
            Author= book.author
            Cost = book.cost
            Section = book.section.title
            self.TableWidget.setItem(row, 0,QtWidgets.QTableWidgetItem(title))
            self.TableWidget.setItem(row, 1,QtWidgets.QTableWidgetItem(Author))
            self.TableWidget.setItem(row, 2,QtWidgets.QTableWidgetItem(str(Cost)))
            self.TableWidget.setItem(row, 3,QtWidgets.QTableWidgetItem(Section))
            row = row+1

         





    # def load_data(self):
    #     print("Trying")
        

    #     for book in self.MainLib.booklist:
    #         title = book.title
    #         Author= book.author
    #         Cost = book.cost
    #         Section = book.section
            


    def SellBook(self):
        print("clicked")
        selected_row = self.TableWidget.currentRow()

        if selected_row >= 0:
           title = self.TableWidget.item(selected_row, 0).text()
           self.MainLib.sellBook(title)
           self.populate_table()
        else:
           print("No book selected.")


    def updateSectionsNumber(self):
        self.SecNoInstance.setText(f'Sections in store: {len(self.MainLib.sections)}')


    def updateBookNumber(self):
        self.bookNoInstance.setText(f'Books in Store: {len(self.MainLib.booklist)}')