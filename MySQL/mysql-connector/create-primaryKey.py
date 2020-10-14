"""
主键设置
创建表的时候我们一般都会设置一个主键（PRIMARY KEY），我们可以使用 "INT AUTO_INCREMENT PRIMARY KEY"
语句来创建一个主键，主键起始值为 1，逐步递增。

如果我们的表已经创建，我们需要使用 ALTER TABLE 来给表添加主键：
"""

import mysql.connector

mydb = mysql.connector.connect(host="localhost", username="root", password="", database="db_test")

cursor = mydb.cursor()

cursor.execute("ALTER TABLE sites ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

