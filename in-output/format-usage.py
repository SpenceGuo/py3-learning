# str.format() 的基本使用如下:
#
# >>> print('{}网址： "{}!"'.format('菜鸟教程', 'www.runoob.com'))
# 菜鸟教程网址： "www.runoob.com!"
# 括号及其里面的字符 (称作格式化字段) 将会被 format() 中的参数替换。
#
# 在括号中的数字用于指向传入对象在 format() 中的位置，如下所示：
#
# >>> print('{0} 和 {1}'.format('Google', 'Runoob'))
# Google 和 Runoob
# >>> print('{1} 和 {0}'.format('Google', 'Runoob'))
# Runoob 和 Google
# 如果在 format() 中使用了关键字参数, 那么它们的值会指向使用该名字的参数。
#
# >>> print('{name}网址： {site}'.format(name='菜鸟教程', site='www.runoob.com'))
# 菜鸟教程网址： www.runoob.com
# 位置及关键字参数可以任意的结合:
#
# >>> print('站点列表 {0}, {1}, 和 {other}。'.format('Google', 'Runoob', other='Taobao'))
# 站点列表 Google, Runoob, 和 Taobao。
# !a (使用 ascii()), !s (使用 str()) 和 !r (使用 repr()) 可以用于在格式化某个值之前对其进行转化:
#
# >>> import math
# >>> print('常量 PI 的值近似为： {}。'.format(math.pi))
# 常量 PI 的值近似为： 3.141592653589793。
# >>> print('常量 PI 的值近似为： {!r}。'.format(math.pi))
# 常量 PI 的值近似为： 3.141592653589793。
# 可选项 : 和格式标识符可以跟着字段名。 这就允许对值进行更好的格式化。 下面的例子将 Pi 保留到小数点后三位：
#
# >>> import math
# >>> print('常量 PI 的值近似为 {0:.3f}。'.format(math.pi))
# 常量 PI 的值近似为 3.142。
# 在 : 后传入一个整数, 可以保证该域至少有这么多的宽度。 用于美化表格时很有用。
#
# >>> table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
# >>> for name, number in table.items():
# ...     print('{0:10} ==> {1:10d}'.format(name, number))
# ...
# Google     ==>          1
# Runoob     ==>          2
# Taobao     ==>          3
# 如果你有一个很长的格式化字符串, 而你不想将它们分开, 那么在格式化时通过变量名而非位置会是很好的事情。
#
# 最简单的就是传入一个字典, 然后使用方括号 [] 来访问键值 :
#
# >>> table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
# >>> print('Runoob: {0[Runoob]:d}; Google: {0[Google]:d}; Taobao: {0[Taobao]:d}'.format(table))
# Runoob: 2; Google: 1; Taobao: 3
# 也可以通过在 table 变量前使用 ** 来实现相同的功能：
#
# >>> table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
# >>> print('Runoob: {Runoob:d}; Google: {Google:d}; Taobao: {Taobao:d}'.format(**table))
# Runoob: 2; Google: 1; Taobao: 3


# 旧式字符串格式化
# % 操作符也可以实现字符串格式化。 它将左边的参数作为类似 sprintf() 式的格式化字符串,
# 而将右边的代入, 然后返回格式化后的字符串. 例如:
#
# >>> import math
# >>> print('常量 PI 的值近似为：%5.3f。' % math.pi)
# 常量 PI 的值近似为：3.142。
# 因为 str.format() 是比较新的函数， 大多数的 Python 代码仍然使用 % 操作符。
# 但是因为这种旧式的格式化最终会从该语言中移除, 应该更多的使用 str.format().


# 读取键盘输入
# Python提供了 input() 内置函数从标准输入读入一行文本，默认的标准输入是键盘。
#
# input 可以接收一个Python表达式作为输入，并将运算结果返回。
#
# 实例:
str1 = input("请输入：");
print("你输入的内容是: ", str1)

