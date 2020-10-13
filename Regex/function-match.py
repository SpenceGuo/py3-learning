"""
Python3 正则表达式
正则表达式是一个特殊的字符序列，它能帮助你方便的检查一个字符串是否与某种模式匹配。

Python 自1.5版本起增加了re 模块，它提供 Perl 风格的正则表达式模式。

re 模块使 Python 语言拥有全部的正则表达式功能。

compile 函数根据一个模式字符串和可选的标志参数生成一个正则表达式对象。该对象拥有一系列方法用于正则表达式匹配和替换。

re 模块也提供了与这些方法功能完全一致的函数，这些函数使用一个模式字符串做为它们的第一个参数。

本章节主要介绍 Python 中常用的正则表达式处理函数，如果你对正则表达式不了解，
可以点击链接 https://www.runoob.com/regexp/regexp-tutorial.html
"""

# re.match函数
# re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。
#
# 函数语法：
#
# re.match(pattern, string, flags=0)
# 函数参数说明：
# 参数	        描述
# pattern	    匹配的正则表达式
# string	    要匹配的字符串。
# flags	        标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。
#
# 匹配成功re.match方法返回一个匹配的对象，否则返回None。
#
# 我们可以使用group(num) 或 groups() 匹配对象函数来获取匹配表达式。

# 匹配对象方法	    描述
# group(num=0)	    匹配的整个表达式的字符串，group() 可以一次输入多个组号，
#                   在这种情况下它将返回一个包含那些组所对应值的元组。
# groups()	        返回一个包含所有小组字符串的元组，从 1 到 所含的小组号。

import re
print(re.match('www', 'www.runoob.com').span())  # 在起始位置匹配
print(re.match('com', 'www.runoob.com'))         # 不在起始位置匹配

line = "Cats are smarter than dogs"
# .* 表示任意匹配除换行符（\n、\r）之外的任何单个或多个字符
matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)

if matchObj:
    print("matchObj.group() : ", matchObj.group())
    print("matchObj.group(1) : ", matchObj.group(1))
    print("matchObj.group(2) : ", matchObj.group(2))
else:
    print("No match!!")


