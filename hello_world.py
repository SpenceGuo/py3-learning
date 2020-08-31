import keyword

"""
这是
多行
注释
"""
# 而这时一个单行注释
print("hello world", end="\n")

# python保留的关键字
print(keyword.kwlist)

# 使用'\'来实现多行语句
item_one, item_two, item_three = 1, 1, 1
total = item_one + \
        item_two + \
        item_three
print(total)

# 在 [], {}, 或 () 中的多行语句，不需要使用反斜杠(\)，例如：
total = ['item_one', 'item_two', 'item_three',
        'item_four', 'item_five']
print("total:" + total.__str__())

"""
import 与 from...import
在 python 用 import 或者 from...import 来导入相应的模块。

将整个模块(somemodule)导入，格式为： import somemodule

从某个模块中导入某个函数,格式为： from somemodule import somefunction

从某个模块中导入多个函数,格式为： from somemodule import firstfunc, secondfunc, thirdfunc

将某个模块中的全部函数导入，格式为： from somemodule import *
"""


