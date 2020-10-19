"""
删除表
删除表使用 "DROP TABLE" 语句， IF EXISTS 关键字是用于判断表是否存在，只有在存在的情况才删除：
"""

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="db_test"
)
mycursor = mydb.cursor()

sql = "DROP TABLE IF EXISTS sites"  # 删除数据表 sites

mycursor.execute(sql)
