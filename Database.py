import pymysql.cursors
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