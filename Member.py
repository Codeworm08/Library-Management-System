import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import pymysql.cursors
import dbconnection
class AddMem(QDialog):
    def __init__(self):
        super(AddMem, self).__init__()
        uic.loadUi("AddMember.ui",self)
        self.show()
        self.buttonBox.accepted.connect(self.getData)
    def getData(self):
        mid=self.MemID.text()
        street=self.Street.text()
        city=self.City.text()
        first_name=self.FName.text()
        last_name=self.LName.text()
        state = self.State.text()
        pin = self.PinCode.text()
        connection = pymysql.connect(host='localhost',
                            user='Leo',
                            password='StAr6hi#oR7',
                            database='LIBRARY',
                            cursorclass=pymysql.cursors.DictCursor)
        with connection:
            with connection.cursor() as cursor:
                sql = "INSERT INTO members (`memberid`,`street`,`city`,`state`,`pin_code`,`first_name`,`last_name`) VALUES (%s,%s,%s,%s,%s,%s,%s)"
                cursor.execute(sql,(mid,street,city,state,pin,first_name,last_name))
                connection.commit()
class ShowMems(QDialog):
    def __init__(self):
        super(ShowMems, self).__init__()
        uic.loadUi("TableMember.ui",self)
        self.show()
        self.load.clicked.connect(self.loadData)
    def loadData(self):
        print("Hello")
        connection = pymysql.connect(host='localhost',
                            user='Leo',
                            password='StAr6hi#oR7',
                            database='LIBRARY',
                            cursorclass=pymysql.cursors.DictCursor)
        cursor=connection.cursor()
        cursor.execute("SELECT * FROM members")
        result=cursor.fetchall()
        print(result)
        self.tableWidget.setRowCount(0)
        for row in result:
            row_number = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row_number)
            for cn,data in enumerate(row):
                print(row_number,cn,row[data])
                self.tableWidget.setItem(row_number,cn,QTableWidgetItem(str(row[data])))
        
        
        

