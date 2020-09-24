"""
无限循环
我们可以通过设置条件表达式永远不为 false 来实现无限循环，实例如下：
"""

"""
# !/usr/bin/python3
var = 1
while var == 1:  # 表达式永远为 true
    num = int(input("输入一个数字: "))
    print("你输入的数字是: ", num)

print("Good bye!")
"""

# !/usr/bin/python3
count = 0
while count < 5:
    print(count, " 小于 5")
    count = count + 1
else:
    print(count, " 大于或等于 5")


# Python for循环可以遍历任何序列的项目，如一个列表或者一个字符串。
#
# for循环的一般格式如下：
#
# for <variable> in <sequence>:
#     <statements>
# else:
#     <statements>


# range()函数
# 如果你需要遍历数字序列，可以使用内置range()函数。它会生成数列，例如:
for i in range(5):
    print(i)

print("---------------------")
# 你也可以使用range指定区间的值：
for i in range(5, 9):
    print(i)

print("---------------------")
# 也可以使range以指定数字开始并指定不同的增量(甚至可以是负数，有时这也叫做'步长'):
for i in range(0, 13, 3):
    print(i)
print("---------------------")
for i in range(-10, -100, -30):
    print(i)

print("---------------------")
# 您可以结合range()和len()函数以遍历一个序列的索引,如下所示:
a = ['Google', 'Baidu', 'Runoob', 'Taobao', 'QQ']
for i in range(len(a)):
    print(i, a[i])

print("---------------------")
# 还可以使用range()函数来创建一个列表：
a = list(range(5))
print(a)

print("---------------------")
# pass 语句
# Python pass是空语句，是为了保持程序结构的完整性。
#
# pass 不做任何事情，一般用做占位语句，如下实例

# !/usr/bin/python3
for letter in 'Runoob':
    if letter == 'o':
        pass
        print('执行 pass 块')
    print('当前字母 :', letter)

print("Good bye!")


