import pymysql.cursors
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
class MyGUI(QDialog):
    def __init__(self):
        super(MyGUI, self).__init__()
        uic.loadUi("AddMember.ui",self)
        self.show()

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
    app = QApplication([])
    dialog = MyGUI()
    app.exec_()

if __name__=='__main__':
    main()
