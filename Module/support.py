# import 语句
# 想使用 Python 源文件，只需在另一个源文件里执行 import 语句，语法如下：
#
# import module1[, module2[,... moduleN]
# 当解释器遇到 import 语句，如果模块在当前的搜索路径就会被导入。
#
# 搜索路径是一个解释器会先进行搜索的所有目录的列表。如想要导入模块 support，需要把命令放在脚本的顶端：

#!/usr/bin/python3
# Filename: support.py

def print_func(par):
    print("Hello : ", par)
    return
