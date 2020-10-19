import mysql.connector

mydb = mysql.connector.connect(host="localhost", username="root", password="", db="db_test")

cursor = mydb.cursor()

sql = "DELETE FROM sites WHERE name = 'stackoverflow'"

cursor.execute(sql)
mydb.commit()

print(cursor.rowcount, " 条记录删除")


print("-----------------------------------------------")
# 注意：要慎重使用删除语句，删除语句要确保指定了 WHERE 条件语句，否则会导致整表数据被删除。
#
# 为了防止数据库查询发生 SQL 注入的攻击，我们可以使用 %s 占位符来转义删除语句的条件：
cursor = mydb.cursor()

sql = "DELETE FROM sites WHERE name = %s"
na = ("stackoverflow",)

cursor.execute(sql, na)

mydb.commit()

print(cursor.rowcount, " 条记录删除")

