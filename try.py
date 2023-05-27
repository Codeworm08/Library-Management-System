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


    def executeAdd_InstanceDialog(self):
        instance = Add_Instance()
        instance.exec_()    
    def executeAdd_BDialog(self):
        book = Add_B()
        book.exec_()
    def executeAddMemDialog(self):
        addMem = AddMem()
        addMem.exec_()
        
class Database:
    def __init__(self) -> None:
        self.connection = pymysql.connect(host='localhost',
                            user='Leo',
                            password='****3',
                            database='ASS1',
                            cursorclass=pymysql.cursors.DictCursor)
    def showDesigCode(self):
        with self.connection:
            with self.connection.cursor() as cursor:
                sql = "SELECT * FROM DESIGNATION"
                cursor.execute(sql)
                result = cursor.fetchall()
                return result
def main():
    app = QApplication(sys.argv)
    widget = MainWin()
    widget.show()
    sys.exit(app.exec_())
    

if __name__=='__main__':
    main()
