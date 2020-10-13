"""
方法重写
如果你的父类方法的功能不能满足你的需求，你可以在子类重写你父类的方法，实例如下：
"""


class Parent:  # 定义父类
    def myMethod(self):
        print('调用父类方法')


class Child(Parent):  # 定义子类
    def myMethod(self):
        print('调用子类方法')


c = Child()  # 子类实例
c.myMethod()  # 子类调用重写方法
super(Child, c).myMethod()  # 用子类对象调用父类已被覆盖的方法


"""
Python super() 函数


描述
super() 函数是用于调用父类(超类)的一个方法。

super 是用来解决多重继承问题的，直接用类名调用父类方法在使用单继承的时候没问题，
但是如果使用多继承，会涉及到查找顺序（MRO）、重复调用（钻石继承）等种种问题。

MRO 就是类的方法解析顺序表, 其实也就是继承父类方法时的顺序表。

语法
以下是 super() 方法的语法:
super(type[, object-or-type])

参数
type -- 类。
object-or-type -- 类，一般是 self

Python3.x 和 Python2.x 的一个区别是: 
Python 3 可以使用直接使用 super().xxx 代替 super(Class, self).xxx :
"""


# Python3.x 实例：
class A:
     def add(self, x):
         y = x+1
         print(y)


class B(A):
    def add(self, x):
        super().add(x)


b = B()
b.add(2)  # 3


# --------------------------------------------------
# Python2.x 实例：
class A(object):  # Python2.x 记得继承 object
    def add(self, x):
        y = x + 1
        print(y)


class B(A):
    def add(self, x):
        super(B, self).add(x)


b = B()
b.add(2)  # 3


# 实例
# 以下展示了使用 super 函数的实例：
class FooParent(object):
    def __init__(self):
        self.parent = 'I\'m the parent.'
        print('Parent')

    def bar(self, message):
        print("%s from Parent" % message)


class FooChild(FooParent):
    def __init__(self):
        # super(FooChild,self) 首先找到 FooChild 的父类（就是类 FooParent），然后把类 FooChild 的对象转换为类 FooParent 的对象
        super(FooChild, self).__init__()
        print('Child')

    def bar(self, message):
        super(FooChild, self).bar(message)
        print('Child bar fuction')
        print(self.parent)


if __name__ == '__main__':
    fooChild = FooChild()
    fooChild.bar('HelloWorld')

