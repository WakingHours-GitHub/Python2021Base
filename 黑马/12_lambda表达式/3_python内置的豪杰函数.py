"""
三个python内置的高阶函数: map, reduce, filter

map函数:
    map(func, *iterables):
        将传入的函数变量func作用到iterable中的每个元素, 返回处理后的结果(迭代器)

reduce函数:
    注意：Python3.x reduce() 已经被移到 functools 模块里，如果我们要使用，需要引入 functools 模块来调用 reduce() 函数：
    reduce(function, sequence, initial=_initial_missing)
    其中, func必须有两个参数, 每次func计算的结果继续和序列的下一个元素做累加运算

"""

from functools import reduce

# map()练习: 计算list1序列中各个数字的平方
list1 = [1, 2, 3, 4, 5]

# 二次方计算函数
def func(x):
    return x ** 2

result = map(func, list1)

print(result) #  <map object at 0x000001ADBA9ACFA0> # 返回一个map对象. 本质上是一个迭代器.
print(list(result)) # [1, 4, 9, 16, 25]

# 还记得lambda表达式吗, 是不是跟这个func很像, 只有一个参数, 并且返回一个表达式
# 那么我们在使用这种内置高阶函数, 可以结合上lambda表达式
print(list(map(lambda x: x ** 2, list1))) # [1, 4, 9, 16, 25]


reduce()