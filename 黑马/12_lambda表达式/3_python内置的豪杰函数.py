"""
三个python内置的高阶函数: map, reduce, filter

map函数:
    map(func, *iterables):
        将传入的函数变量func作用到iterable中的每个元素, 返回处理后的结果(迭代器)

reduce函数:
    注意：Python3.x reduce() 已经被移到 functools 模块里，如果我们要使用，需要引入 functools 模块来调用 reduce() 函数：
    reduce(function, sequence, initial=_initial_missing)
    其中, func必须有两个参数, 每次func计算的结果继续和序列的下一个元素做累积运算
    就是对序列做累积操作, 具体是什么累积操作, 则需要定义再function中,
    因为是累积操作, 并且还需要定义计算, 所以必须是两个参数.

filter函数:
    filter(function_or_None, iterable)
    filter()函数用于过滤序列. 过滤掉不符合条件的元素, 返回一个filter对象(可迭代对象)
    function: 返回一个bool表达式, 表示是否满足表达式, 如果为True, 则保留, 反之不保留.

"""

from functools import reduce

# map()练习: 计算list1序列中各个数字的平方
list1 = [1, 2, 3, 4, 5]


# 二次方计算函数
def func(x):
    return x ** 2


result = map(func, list1)

print(result)  # <map object at 0x000001ADBA9ACFA0> # 返回一个map对象. 本质上是一个迭代器.
print(list(result))  # [1, 4, 9, 16, 25]

# 还记得lambda表达式吗, 是不是跟这个func很像, 只有一个参数, 并且返回一个表达式
# 那么我们在使用这种内置高阶函数, 可以结合上lambda表达式
print(list(map(lambda x: x ** 2, list1)))  # [1, 4, 9, 16, 25]

# reduce:
# 需求: 计算list1序列中各个数字的累加和
list1 = [1, 2, 3, 4, 5]


def func(a, b):
    return a + b  # 定义的a, b累加操作.


# 该函数 和下面的这个lambda表达式等效
result = reduce(lambda a, b: a + b, list1)

print(result)  # 15

# filter:
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = filter(lambda x: x%2==0, list1)
print(result) # <filter object at 0x0000025F0CC2AFD0> # 也是一个迭代器对象
print(list(result)) # [2, 4, 6, 8, 10]


