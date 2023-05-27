import pymysql.cursors
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from Member import *
class MainWin(QMainWindow):
    def __init__(self):
        super(MainWin, self).__init__()
        uic.loadUi("MainWindow.ui", self)
        self.AddMember.clicked.connect(self.executeAddMemDialog)
    def executeAddMemDialog(self):
        addMem = AddMem()
        addMem.exec_()
class Database:
    def __init__(self) -> None:
        self.connection = pymysql.connect(host='localhost',
                            user='Leo',
                            password='StAr6hi#oR7',
                            database='LIBRARY',
                            cursorclass=pymysql.cursors.DictCursor)
    def getMems(self):
        with self.connection:
            with self.connection.cursor() as cursor:
                sql = "SELECT * FROM members"
                cursor.execute(sql)
                result = cursor.fetchall()
                print(result)
                return result
    def addMem(self,mid,street,city,state,pin_code,first_name,last_name):
        with self.connection:
            with self.connection.cursor() as cursor:
                sql = "INSERT INTO members (`memberid`,`street`,`city`,`state`,`pin_code`,`first_name`,`last_name`) VALUES (%s,%s,%s,%s,%s,%s,%s)"
                cursor.execute(sql,(mid,street,city,state,pin_code,first_name,last_name))
            self.connection.commit()
def main():
    app = QApplication(sys.argv)
    widget = MainWin()
    widget.show()
    sys.exit(app.exec_())
    

if __name__=='__main__':
    main()
