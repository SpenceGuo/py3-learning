"""
执行sql语句查询后,MySQLCursorBuffered游标标从服务器获取整个结果集并将他们放在缓冲区中。

Buffered游标适用于多个小结果集的查询,且多个结果集之间的数据需要一起使用。

使用buffered游标执行查询语句时 ,取行方法（如fetchone()，fechcall()等）返回的是缓冲区中的行。
nonbuffered游标不从服务器获取数据,直到调用了某个获取数据行的方法, 在使用nonbuffered游标时,
必须确保取出的结果是结果集中的所有行，才能再用同一连接执行其他语句,
否则会报错InternalError(Unread result found)。

解决方法：
1.创建buffered游标，设置buffered 参数为"True" -->实例：Line 23
2.多执行一次 fetchall() 操作将结果集中的所有行全部取出 -->实例： Line4 0
"""

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="db_test",
    # buffered=True
)
cursor = mydb.cursor()


print("----------------------------------------------")
# 如果我们只想读取一条数据，可以使用 fetchone() 方法：
cursor.execute("SELECT * FROM sites")

result = cursor.fetchone()

print(result)


print("----------------------------------------------")
# 此处需执行 fetchall() 操作，否则程序执行时报了一个unread result found的异常
# 不管针对数据库的查询有没有返回结果，必须要进行fetchxxx()
# cursor.fetchall()

# where 条件语句
# 如果我们要读取指定条件的数据，可以使用 where 语句：
sql = r"SELECT * FROM sites WHERE name ='RUNOOB'"

cursor.execute(sql)

result = cursor.fetchall()

for x in result:
    print(x)


