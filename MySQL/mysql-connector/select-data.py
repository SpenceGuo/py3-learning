"""
查询数据
查询数据使用 SELECT 语句：
"""

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="db_test"
)
cursor = mydb.cursor()


print("----------------------------------------------")
cursor.execute("SELECT * FROM sites")

result = cursor.fetchall()  # fetchall() 获取所有记录

for x in result:
    print(x)


print("----------------------------------------------")
# 也可以读取指定的字段数据(主要根据SQL语句来调整
# )：
cursor.execute("SELECT name, url FROM sites")

result = cursor.fetchall()

for x in result:
    print(x)


print("----------------------------------------------")
# 如果我们只想读取一条数据，可以使用 fetchone() 方法：
cursor.execute("SELECT * FROM sites")

result = cursor.fetchone()

print(result)


print("----------------------------------------------")
# 此处需执行 fetchall() 操作，否则程序执行时报了一个unread result found的异常
# 不管针对数据库的查询有没有返回结果，必须要进行fetchxxx()，
# 否则进行下一个其他的insert、create等待操作的时候就会报unread result found的异常了。
cursor.fetchall()

# where 条件语句
# 如果我们要读取指定条件的数据，可以使用 where 语句：
sql = r"SELECT * FROM sites WHERE name ='RUNOOB'"

cursor.execute(sql)

result = cursor.fetchall()

for x in result:
    print(x)


print("----------------------------------------------")
# 也可以使用通配符 %：
sql = "SELECT * FROM sites WHERE url LIKE '%oo%'"

cursor.execute(sql)

result = cursor.fetchall()

for x in result:
    print(x)


print("----------------------------------------------")
# 为了防止数据库查询发生 SQL 注入的攻击，我们可以使用 %s 占位符来转义查询的条件：
sql = "SELECT * FROM sites WHERE name = %s"
na = ("RUNOOB",)

cursor.execute(sql, na)

result = cursor.fetchall()

for x in result:
    print(x)


print("----------------------------------------------")
# 排序
# 查询结果排序可以使用 ORDER BY 语句，默认的排序方式为升序，关键字为 ASC，如果要设置降序排序，可以设置关键字 DESC。
sql = "SELECT * FROM sites ORDER BY name"

cursor.execute(sql)

result = cursor.fetchall()

for x in result:
    print(x)


print("----------------------------------------------")
# 降序排序实例：
sql = "SELECT * FROM sites ORDER BY name DESC"

cursor.execute(sql)

result = cursor.fetchall()

for x in result:
    print(x)


print("----------------------------------------------")
# Limit
# 如果我们要设置查询的数据量，可以通过 "LIMIT" 语句来指定
cursor.execute("SELECT * FROM sites LIMIT 5")

result = cursor.fetchall()

for x in result:
    print(x)


print("----------------------------------------------")
# 也可以指定起始位置，使用的关键字是 OFFSET：
cursor.execute("SELECT * FROM sites LIMIT 3 OFFSET 1")  # 0 为 第一条，1 为第二条，以此类推

result = cursor.fetchall()

for x in result:
    print(x)

