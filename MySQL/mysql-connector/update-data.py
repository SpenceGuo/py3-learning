import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="db_test"
)
mycursor = mydb.cursor()

sql = "UPDATE sites SET name = 'ZH' WHERE name = 'Zhihu'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, " 条记录被修改")


print("-------------------------------------------")
# 注意：UPDATE 语句要确保指定了 WHERE 条件语句，否则会导致整表数据被更新。
#
# 为了防止数据库查询发生 SQL 注入的攻击，我们可以使用 %s 占位符来转义更新语句的条件：
sql = "UPDATE sites SET name = %s WHERE name = %s"
val = ("Zhihu", "ZH")

mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, " 条记录被修改")














