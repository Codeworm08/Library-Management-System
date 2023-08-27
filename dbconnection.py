import pymysql.cursors
connection = pymysql.connect(host='localhost',
                            user='Leo',
                            password='StAr6hi#oR7',
                            database='LIBRARY',
                            cursorclass=pymysql.cursors.DictCursor)
