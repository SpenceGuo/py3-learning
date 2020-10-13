"""
compile 函数
compile 函数用于编译正则表达式，生成一个正则表达式（ Pattern ）对象，供 match() 和 search() 这两个函数使用。

语法格式为：
re.compile(pattern[, flags])

参数：
pattern : 一个字符串形式的正则表达式
flags 可选，表示匹配模式，比如忽略大小写，多行模式等，具体参数为：
        re.I 忽略大小写
        re.L 表示特殊字符集 \w, \W, \b, \B, \s, \S 依赖于当前环境
        re.M 多行模式
        re.S 即为' . '并且包括换行符在内的任意字符（' . '不包括换行符）
        re.U 表示特殊字符集 \w, \W, \b, \B, \d, \D, \s, \S 依赖于 Unicode 字符属性数据库
        re.X 为了增加可读性，忽略空格和' # '后面的注释
"""
# 实例
# >>>import re
# >>> pattern = re.compile(r'\d+')                    # 用于匹配至少一个数字
# >>> m = pattern.match('one12twothree34four')        # 查找头部，没有匹配
# >>> print( m )
# None
# >>> m = pattern.match('one12twothree34four', 2, 10) # 从'e'的位置开始匹配，没有匹配
# >>> print( m )
# None
# >>> m = pattern.match('one12twothree34four', 3, 10) # 从'1'的位置开始匹配，正好匹配
# >>> print( m )                                        # 返回一个 Match 对象
# <_sre.SRE_Match object at 0x10a42aac0>
# >>> m.group(0)   # 可省略 0
# '12'
# >>> m.start(0)   # 可省略 0
# 3
# >>> m.end(0)     # 可省略 0
# 5
# >>> m.span(0)    # 可省略 0
# (3, 5)

"""
在上面，当匹配成功时返回一个 Match 对象，其中：
    group([group1, …]) 方法用于获得一个或多个分组匹配的字符串，当要获得整个匹配的子串时，可直接使用 group() 或 group(0)；
    start([group]) 方法用于获取分组匹配的子串在整个字符串中的起始位置（子串第一个字符的索引），参数默认值为 0；
    end([group]) 方法用于获取分组匹配的子串在整个字符串中的结束位置（子串最后一个字符的索引+1），参数默认值为 0；
    span([group]) 方法返回 (start(group), end(group))。
"""

import re

pattern = re.compile(r'\d+')                    # 用于匹配至少一个数字
m = pattern.match('one12twothree34four')        # 查找头部，没有匹配
print(m)

m = pattern.match('one12twothree34four', 2, 10) # 从'e'的位置开始匹配，没有匹配
print(m)

m = pattern.match('one12twothree34four', 3, 10) # 从'1'的位置开始匹配，正好匹配
print(m)                                        # 返回一个 Match 对象

# >>> m.group(0)   # 可省略 0
# '12'
# >>> m.start(0)   # 可省略 0
# 3
# >>> m.end(0)     # 可省略 0
# 5
# >>> m.span(0)    # 可省略 0
# (3, 5)

# 在上面，当匹配成功时返回一个 Match 对象，其中：
#
# group([group1, …]) 方法用于获得一个或多个分组匹配的字符串，当要获得整个匹配的子串时，可直接使用 group() 或 group(0)；
# start([group]) 方法用于获取分组匹配的子串在整个字符串中的起始位置（子串第一个字符的索引），参数默认值为 0；
# end([group]) 方法用于获取分组匹配的子串在整个字符串中的结束位置（子串最后一个字符的索引+1），参数默认值为 0；
# span([group]) 方法返回 (start(group), end(group))。


# 再看看一个例子：
#
# 实例
# >>>import re
# >>> pattern = re.compile(r'([a-z]+) ([a-z]+)', re.I)   # re.I 表示忽略大小写
# >>> m = pattern.match('Hello World Wide Web')
# >>> print( m )                            # 匹配成功，返回一个 Match 对象
# <_sre.SRE_Match object at 0x10bea83e8>
# >>> m.group(0)                            # 返回匹配成功的整个子串
# 'Hello World'
# >>> m.span(0)                             # 返回匹配成功的整个子串的索引
# (0, 11)
# >>> m.group(1)                            # 返回第一个分组匹配成功的子串
# 'Hello'
# >>> m.span(1)                             # 返回第一个分组匹配成功的子串的索引
# (0, 5)
# >>> m.group(2)                            # 返回第二个分组匹配成功的子串
# 'World'
# >>> m.span(2)                             # 返回第二个分组匹配成功的子串索引
# (6, 11)
# >>> m.groups()                            # 等价于 (m.group(1), m.group(2), ...)
# ('Hello', 'World')
# >>> m.group(3)                            # 不存在第三个分组
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# IndexError: no such group


# findall
# 在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果没有找到匹配的，则返回空列表。
#
# 注意： match 和 search 是匹配一次 findall 匹配所有。
#
# 语法格式为：
#
# re.findall(pattern, string, flags=0)
# 或
# pattern.findall(string[, pos[, endpos]])
# 参数：
#
# pattern 匹配模式。
# string 待匹配的字符串。
# pos 可选参数，指定字符串的起始位置，默认为 0。
# endpos 可选参数，指定字符串的结束位置，默认为字符串的长度。


"""
查找字符串中的所有数字：

实例
import re
 
result1 = re.findall(r'\d+','runoob 123 google 456')
 
pattern = re.compile(r'\d+')   # 查找数字
result2 = pattern.findall('runoob 123 google 456')
result3 = pattern.findall('run88oob123google456', 0, 10)
 
print(result1)
print(result2)
print(result3)
输出结果：

['123', '456']
['123', '456']
['88', '12']
"""


"""
re.finditer
和 findall 类似，在字符串中找到正则表达式所匹配的所有子串，并把它们作为一个迭代器返回。

re.finditer(pattern, string, flags=0)
参数：

参数	        描述
pattern	    匹配的正则表达式
string	    要匹配的字符串。
flags	    标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。

实例

import re
 
it = re.finditer(r"\d+", "12a32bc43jf3") 
for match in it: 
    print (match.group() )
输出结果：

12 
32 
43 
3
"""

# ---------------------------------------------------------

"""
re.split
split 方法按照能够匹配的子串将字符串分割后返回列表，它的使用形式如下：

re.split(pattern, string[, maxsplit=0, flags=0])
参数：

参数	描述
pattern	匹配的正则表达式
string	要匹配的字符串。
maxsplit	分隔次数，maxsplit=1 分隔一次，默认为 0，不限制次数。
flags	标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。参见：正则表达式修饰符 - 可选标志
实例
>>>import re
>>> re.split('\W+', 'runoob, runoob, runoob.')
['runoob', 'runoob', 'runoob', '']
>>> re.split('(\W+)', ' runoob, runoob, runoob.') 
['', ' ', 'runoob', ', ', 'runoob', ', ', 'runoob', '.', '']
>>> re.split('\W+', ' runoob, runoob, runoob.', 1) 
['', 'runoob, runoob, runoob.']
 
>>> re.split('a*', 'hello world')   # 对于一个找不到匹配的字符串而言，split 不会对其作出分割
['hello world']
"""

