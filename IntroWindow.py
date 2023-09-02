from PyQt5 import QtCore, QtGui, QtWidgets
from LibraryGui2 import Ui_LibrarySystem
from IntroWindow_ui import Ui_IntroWindow
import settings

class MyIntroWindow(QtWidgets.QMainWindow,Ui_IntroWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton2.clicked.connect(self.OpenLibrary)
        

    def OpenLibrary(self):
        settings.LibraryName = self.lineEdit.text()
        print(settings.LibraryName)
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_LibrarySystem()
        self.ui.setupUi(self.window)
        self.window.show()
        self.window.activateWindow()
        intro_window.close()
        
       





    def OpenIntroagainlol(self):
        print("Open Introagain lol button clicked")


        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    intro_window = MyIntroWindow()  # Use your custom class
    intro_window.show()
    
    sys.exit(app.exec_())
