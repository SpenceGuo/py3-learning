"""
Python MySQL - mysql-connector 驱动
MySQL 是最流行的关系型数据库管理系统

本章节我们为大家介绍使用 mysql-connector 来连接使用 MySQL， mysql-connector 是 MySQL 官方提供的驱动器。

我们可以使用 pip 或 conda(前提是你安装了Anaconda)命令来安装 mysql-connector：

pip install mysql-connector-python
或
conda install mysql-connector-python

使用以下代码测试 mysql-connector 是否安装成功：

demo_mysql_test.py:
import mysql.connector
执行以上代码，如果没有产生错误，表明安装成功。
"""

import mysql.connector

# 创建数据库连接
# 可以使用以下代码来连接数据库：
mydb = mysql.connector.connect(
    host="localhost",
    username="root",
    password=""
)

# 创建数据库
# 创建数据库使用 "CREATE DATABASE" 语句，以下创建一个名为 db_test 的数据库：
cursor = mydb.cursor()
cursor.execute("create database db_test")

# 创建数据库前我们也可以使用 "SHOW DATABASES" 语句来查看数据库是否存在：
#
# demo_mysql_test.py:
# 输出所有数据库列表：
# import mysql.connector
#
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   passwd="123456"
# )
#
# mycursor = mydb.cursor()
#
# mycursor.execute("SHOW DATABASES")
#
# for x in mycursor:
#   print(x)

# 或者我们可以直接连接数据库，如果数据库不存在，会输出错误信息：
#
# demo_mysql_test.py:
# import mysql.connector
#
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   passwd="123456",
#   database="runoob_db"
# )




