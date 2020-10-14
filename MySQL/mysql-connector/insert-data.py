"""
插入数据
插入数据使用 "INSERT INTO" 语句：
"""

import mysql.connector

mydb = mysql.connector.connect(host="localhost", username="root", password="", database="db_test")

cursor = mydb.cursor()

sql = "INSERT INTO sites (name, url) VALUES (%s, %s)"
val = ("RUNOOB", "https://www.runoob.com")
cursor.execute(sql, val)

mydb.commit()  # 数据表内容有更新，必须使用到该语句

print(cursor.rowcount, "记录插入成功。")


# 批量插入
# 批量插入使用 executemany() 方法，该方法的第二个参数是一个元组列表，包含了我们要插入的数据：
sql = "INSERT INTO sites (name, url) VALUES (%s, %s)"
val = [
    ('Google', 'https://www.google.com'),
    ('Github', 'https://www.github.com'),
    ('Taobao', 'https://www.taobao.com'),
    ('stackoverflow', 'https://www.stackoverflow.com/')
]

cursor.executemany(sql, val)

mydb.commit()  # 数据表内容有更新，必须使用到该语句

print(cursor.rowcount, "记录插入成功。")


# 如果我们想在数据记录插入后，获取该记录的 ID ，可以使用以下代码：
sql = "INSERT INTO sites (name, url) VALUES (%s, %s)"
val = ("Zhihu", "https://www.zhihu.com")
cursor.execute(sql, val)

mydb.commit()

print("1 条记录已插入, ID:", cursor.lastrowid)

