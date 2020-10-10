# f.write()
# f.write(string) 将 string 写入到文件中, 然后返回写入的字符数。
#
# 实例: 打开一个文件
f = open("input.txt", "w")

num = f.write("Python 是一个非常好的语言。\n是的，的确非常好!!\n")
print(num)
# 关闭打开的文件
f.close()


# 如果要写入一些不是字符串的东西, 那么将需要先进行转换:
# 打开一个文件
f = open("input.txt", "w")

value = ('www.runoob.com', 14)
s = str(value)
f.write(s)

# 关闭打开的文件
f.close()


"""
f.tell()
f.tell() 返回文件对象当前所处的位置, 它是从文件开头开始算起的字节数。

f.seek()
如果要改变文件当前的位置, 可以使用 f.seek(offset, from_what) 函数。

from_what 的值, 如果是 0 表示开头, 如果是 1 表示当前位置, 2 表示文件的结尾，例如：

seek(x,0) ： 从起始位置即文件首行首字符开始移动 x 个字符
seek(x,1) ： 表示从当前位置往后移动x个字符
seek(-x,2)：表示从文件的结尾往前移动x个字符

from_what 值为默认为0，即文件开头。下面给出一个完整的例子：
>>> f = open('input.txt', 'rb+')
>>> f.write(b'0123456789abcdef')
16
>>> f.seek(5)     # 移动到文件的第六个字节
5
>>> f.read(1)
b'5'
>>> f.seek(-3, 2) # 移动到文件的倒数第三字节
13
>>> f.read(1)
b'd'
"""

# f.close()
# 在文本文件中 (那些打开文件的模式下没有 b 的), 只会相对于文件起始位置进行定位。
#
# 当你处理完一个文件后, 调用 f.close() 来关闭文件并释放系统的资源，如果尝试再调用该文件，则会抛出异常。
#
# >>> f.close()
# >>> f.read()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in ?
# ValueError: I/O operation on closed file


# 当处理一个文件对象时, 使用 with 关键字是非常好的方式。
# 在结束后, 它会帮你正确的关闭文件。 而且写起来也比 try - finally 语句块要简短:
#
# >>> with open('/tmp/foo.txt', 'r') as f:
# ...     read_data = f.read()
# >>> f.closed
# True
# 文件对象还有其他方法, 如 isatty() 和 trucate(), 但这些通常比较少用。













