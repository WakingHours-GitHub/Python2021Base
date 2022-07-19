"""
元组: 可以存储多个数据, 但是元组内的数据是不能修改的.
语法: 使用()包裹数据.
    tuple = (ele, )
    # 如果是单个元素, 必须要有',', 否则元组则会自动拆包, 等于里面的数据
    tuple = tuple()
定义:
    元组定义使用(), 并且使用','隔开各个数据, 数据可以是不同的数据类型

元组方法:
    元组不支持修改, 如果试图修改元组, 则会报错, 但也并不是不能修改,
        例如当元组中存放可变数据类型时, 例如列表, 那么此时修改列表, 是可行的.
    因此只支持查找 查找方法:
    按照下标查找数据:
        index = tuple.index("数据", startindex, endindex):
        按照内容查找数据, 如果数据存在则返回对应位置的下标,
        如果没有找到数据, 则报错.

        int = tuple.count("数据", startindex, endindex)
        统计某个数据在当前元组中出现的次数.

        len(): 通用方法, 列表, 字符串, 元组通用, 求取长度.







"""

# 多个数据元组:
t1 = (10, 20, 30)
print(t1)
print(type(t1)) # <class 'tuple'>

# 单个数据元组: 注意','不可以省略.
t2 = (10, )
print(type(t2))

# 如果不加',', 则会自动拆包, 直接表示()中的数据
t3 = (10)
print(type(t3)) # <class 'int'>

t4 = ("str")
print(type(t4)) # <class 'str'>

t5 = ("str", )
print(type(t5)) # <class 'tuple'>


# 查找元组中的函数:
tuple1 = ('aa', 'bb', 'cc', 'dd')
print(tuple1[0]) #  通过索引进行取值.

print(tuple1.index("aa")) # 返回找到数据的索引
# 如果没有找到数据则会报错.
# print(tuple1.index("aaa")) #  ValueError: tuple.index(x): x not in tuple

print(tuple1.count("bb")) # 1
print(tuple1.count("aaa")) # 0

print(len(tuple1)) # 4 长度


# 修改元组;
tuple1 = ('aa', 'bb', 'cc', ['tom', 'rose'])
print(tuple1) # 输出完整列表.


# 如果修改元组中的内容则直接报错.
# tuple1[0] = 'eee' # TypeError: 'tuple' object does not support item assignment

# 但是可以修改元组中的列表元素
print(tuple1[-1]) #  ['tom', 'rose'] # 可见,找到的是最后袷离别奥
tuple1[-1][0] = "lipu"
print(tuple1) # ('aa', 'bb', 'cc', ['lipu', 'rose']) # 可见成功修改了.


tuple1[-1].append("tom")
print(tuple1) # ('aa', 'bb', 'cc', ['lipu', 'rose', 'tom'])


# 可见修改元组, 不可以修改元组中的值, 例如这里面的列表是一个指针
# 只要地址没有修改, 就不算修改元组


