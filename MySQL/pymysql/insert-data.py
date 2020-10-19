"""
数据库插入操作
以下实例使用执行 SQL INSERT 语句向表 EMPLOYEE 插入记录：
"""

import pymysql

# 打开数据库连接
db = pymysql.connect("localhost", "root", "", "TESTDB")

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 插入语句
sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('Mac', 'Mofan', 20, 'M', 2000)"""
try:
    # 执行sql语句
    cursor.execute(sql)
    # 提交到数据库执行
    db.commit()
except:
    # 如果发生错误则回滚
    db.rollback()

# 关闭数据库连接
db.close()

"""
以下代码使用变量向SQL语句中传递参数:

..................................
user_id = "test123"
password = "password"

con.execute('insert into Login values( %s,  %s)' % (user_id, password))
..................................
"""
