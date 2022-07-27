"""
公共方法:
    函数                  描述
    len()           计算容器中元素个数
    del 或 del()     删除
    max()           返回容器中元素最⼤值
    min()           返回容器中元素最⼩值
    range(start,end, step) ⽣成从start到end的数字，步⻓为 step，供for循环使⽤
    enumerate()     函数⽤于将⼀个可遍历的数据对象(如列表、元组或字符串)组合为⼀个索引序
            列，同时列出数据和数据下标，⼀般⽤在 for 循环当中

容器类型转换：
tuple() # 将序列转换为元组
list() # 将序列转换为元组
set() # 将序列转换成集合


"""
# len(可迭代对象) # 计算可迭代对象数据的长度.
# 可迭代对象: 字符串, 列表, 元组, 生成器

str1 = 'abcdef'
print(len(str1))  # 6

list1 = [10, 20, 30, 40, ]
print(len(list1))  # 4

# 元组:
t1 = (10, 20, 30, 40,)
print(len(t1))  # 4

# 集合:
s1 = {10, 20, 30}
print(len(s1))  # 3

# range()
print(range(10))  # range(0, 10) # range对象, 可迭代对象
print(type(range(10)))  # <class 'range'>

print(list(range(10)))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(range(1, 10))  # [1, 10), 不包含10
# 设置step
print(list(range(1, 10, 2)))  # [1, 3, 5, 7, 9]

# enumerate: 返回结果是元组, 元组第一个数据是原迭代对象的数据对应的下标, 元组第二个数据是原迭代对象的数据.
tuple1 = (10, 20, 30)
for ele in enumerate(tuple1):
    print(ele)  #
# (0, 10)
# (1, 20)
# (2, 30)

# 元组自动拆包:
for index, value in enumerate(tuple1):
    print(index, value)  #

# 0 10
# 1 20
# 2 30

print("--" * 20)

# 容器转换
list1 = [10, 20, 30, 40, 50, 20]
s1 = {100, 200, 30}
t1 = ('a', 'b', 'c', 'd')

# tuple(可迭代对象)将序列转换元组
# 元组有不可修改的性质, 因此我们需要不修改特性就是用tuple()
print(tuple(list1))  # (10, 20, 30, 40, 50)
print(tuple(s1))  # (200, 100, 30)

# list()将序列转换成为列表
# 列表可以修改, 如果我们需要修改一个序列, 我们就转换成list
print(list(s1))  # [200, 100, 30]
print(list(t1))  # ['a', 'b', 'c', 'd']

# set(): 将序列转换成集合
# 集合是有去重功能的, 如果我们想要给一个序列去重, 就是用set()
print(set(list1)) # 可见, list1中的重复元素已经去重了, 并且是无顺序的.
print(set(t1))