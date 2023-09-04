import pymysql.cursors
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from Member import *
from book import *
from instance import * 

class MainWin(QMainWindow):
    def __init__(self):
        super(MainWin, self).__init__()
        uic.loadUi("MainWindow.ui", self)
        self.AddMember.clicked.connect(self.executeAddMemDialog)
        self.AddBook.clicked.connect(self.executeAdd_BDialog)
        self.AddInstance.clicked.connect(self.executeAdd_InstanceDialog)
        self.ViewMembers.clicked.connect(self.executeViewMemDialog)
        self.UpdateMember.clicked.connect(self.executeUpdateMemDialog)

    def executeAdd_InstanceDialog(self):
        instance = Add_Instance()
        instance.exec_()    
    def executeAdd_BDialog(self):
        book = Add_B()
        book.exec_()
    def executeAddMemDialog(self):
        addMem = AddMem()
        addMem.exec_()
    def executeViewMemDialog(self):
        viewMem = ShowMems()
        viewMem.exec_()
    def executeUpdateMemDialog(self):
        updateMem =UpdateMems()
        updateMem.exec_()

def main():
    app = QApplication(sys.argv)
    widget = MainWin()
    widget.show()
    sys.exit(app.exec_())
    

if __name__=='__main__':
    main()
