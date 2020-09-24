
"""
集合（set）是由一个或数个形态各异的大小整体组成的，构成集合的事物或对象称作元素或是成员。
基本功能是进行成员关系测试和删除重复元素。
可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
创建格式：
parame = {value01,value02,...}
或者
set(value)
"""
print("-----------------------------集合的定义-------------------------------")
sites = {'Taobao', 'Google', 'Taobao', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu'}
print(sites)   # 输出集合，重复的元素被自动去掉

# 成员测试
if 'Runoob' in sites:
    print('Runoob 在集合中')
else :
    print('Runoob 不在集合中')

# set可以进行集合运算
a = set('abracadabra')


b = set('alacazam')

print(a)
print(a - b)     # a 和 b 的差集
print(a | b)     # a 和 b 的并集
print(a & b)     # a 和 b 的交集
print(a ^ b)     # a 和 b 中不同时存在的元素


print("-----------------------------集合的基本操作-------------------------------")
# 添加元素

# 语法格式如下：s.add( x )
thisset = set(("Google", "Runoob", "Taobao"))
thisset.add("Facebook")
print(thisset)

# 还有一个方法，也可以添加元素，且参数可以是列表，元组，字典等，语法格式如下：
# s.update( x )
thisset = set(("Google", "Runoob", "Taobao"))
thisset.update({1, 3})
print(thisset)
thisset.update([1, 4], [5, 6])
print(thisset)

print("-----------------------------移除元素-------------------------------")
# 移除元素
# 语法格式如下： s.remove( x )
# 将元素 x 从集合 s 中移除，如果元素不存在，则会发生错误
thisset = set(("Google", "Runoob", "Taobao"))
thisset.remove("Taobao")
print(thisset)

# 此外还有一个方法也是移除集合中的元素，且如果元素不存在，不会发生错误。格式如下所示：
# s.discard( x )
thisset = set(("Google", "Runoob", "Taobao"))
thisset.discard("Facebook")  # 不存在不会发生错误
print(thisset)

print("-----------------------------计算集合元素个数-------------------------------")
# 计算集合元素个数
# 语法格式如下：len(s)
thisset = set(("Google", "Runoob", "Taobao"))
print(len(thisset))

print("-----------------------------清空集合-------------------------------")
# 清空集合
# 语法格式如下：s.clear()
# 清空集合 s

thisset = set(("Google", "Runoob", "Taobao"))
thisset.clear()
print(thisset)

print("-----------------------------判断元素是否在集合中存在-------------------------------")
# 判断元素是否在集合中存在
# 语法格式如下： x in s
# 判断元素 x 是否在集合 s 中，存在返回 True，不存在返回 False
thisset = set(("Google", "Runoob", "Taobao"))
print("Runoob" in thisset)
print("Facebook" in thisset)

# 集合内置方法完整列表
"""
add()	                       为集合添加元素
clear()	                       移除集合中的所有元素
copy()	                       拷贝一个集合
difference()	               返回多个集合的差集
difference_update()	           移除集合中的元素，该元素在指定的集合也存在。
discard()	                   删除集合中指定的元素
intersection()	               返回集合的交集
intersection_update()	       返回集合的交集。
isdisjoint()	               判断两个集合是否包含相同的元素，如果没有返回 True，否则返回 False。
issubset()	                   判断指定集合是否为该方法参数集合的子集。
issuperset()	               判断该方法的参数集合是否为指定集合的子集
pop()	                       随机移除元素
remove()	                   移除指定元素
symmetric_difference()	       返回两个集合中不重复的元素集合。
symmetric_difference_update()  移除当前集合中在另外一个指定集合相同的元素，并将另外一个指定集合中不同的元素插入到当前集合中。
union()	                       返回两个集合的并集
update()	                   给集合添加元素
"""
