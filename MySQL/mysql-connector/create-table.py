"""
创建数据表
创建数据表使用 "CREATE TABLE" 语句，创建数据表前，需要确保数据库已存在，以下创建一个名为 sites 的数据表：
"""
import mysql.connector

mydb = mysql.connector.connect(host="localhost", username="root", password="", database="db_test")

cursor = mydb.cursor()

cursor.execute(r"CREATE TABLE sites (name VARCHAR(255), url VARCHAR(255))")

# 我们也可以使用 "SHOW TABLES" 语句来查看数据表是否已存在：
# demo_mysql_test.py:
# import mysql.connector
#
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   passwd="123456",
#   database="db_test"
# )
# mycursor = mydb.cursor()
#
# mycursor.execute("SHOW TABLES")
#
# for x in mycursor:
#   print(x)





