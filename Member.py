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
        connection = dbconnection.connection
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
        connection = dbconnection.connection
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
class UpdateMems(QDialog):
    def __init__(self):
        super(UpdateMems, self).__init__()
        uic.loadUi("UpdateMember.ui",self)
        self.show()
        self.buttonBox.accepted.connect(self.getData)
        self.loadIds()

    def loadIds(self):
        connection = dbconnection.connection
        memIds = []
        with connection:
            with connection.cursor() as cursor:
                sql = "SELECT `memberid` FROM members"
                cursor.execute(sql)
                result = cursor.fetchall()
                for row in result:
                    memIds.append(row['memberid'])
        print(memIds)
        self.memIDBox.addItems(map(str,memIds))
    def getData(self):
        mid=self.MemID.text()
        street=self.Street.text()
        city=self.City.text()
        first_name=self.FName.text()
        last_name=self.LName.text()
        state = self.State.text()
        pin = self.PinCode.text()
        connection = dbconnection.connection
        with connection:
            with connection.cursor() as cursor:
                sql = "UPDATE members SET `street`=%s,`city`=%s,`state`=%s,`pin_code`=%s,`first_name`=%s,`last_name`=%s WHERE `memberid`=%s"
                cursor.execute(sql,(street,city,state,pin,first_name,last_name,mid))
                connection.commit()
        
        

