"""
lambda表达式的引用场景:
    如果一个函数只有一个返回值, 并且只有一句代码, 可以使用lambda简化
    一句话, lambda就是简化代码用的.

lambda语法:
    lambda 参数列表: return表达式(必须是要有返回值的)

注意:
    lambda表达式的参数可有可无, 函数的参数在lambda表达式中完全使用
    lambda表达式能够接收任何数量的参数但只能返回一个表达式的值.

lambda参数形式:
无参数:
    lambda : 表达式 # 直接返回表达式
一个参数:
    lambda a : 表达式
默认参数:
    lambda a, b=value: 表达式.

可变位置参数: *args
    lambda *args: args

可变关键字参数: **kwargs
    lambda **kwargs: kwargs

参数的调用和函数的写法, 与规则相同

lambda的应用:
带有判断的lambda
    lambda 参数列表: 三木运算符(表达式)




"""

# lambda快速入门:
import gc


def fn1():
    return 200 # 直接返回200.


print(fn1) # <function fn1 at 0x000001C718C4F040>, 返回函数的句柄
print(fn1()) # 调用函数
# 函数名只是一个地址, 指向函数入口, 只有加上()才是待用函数



# lambda: 匿名函数, 也就是一次性函数.
fn2 = lambda : 100 # 保留函数句柄
print(fn2) # <function <lambda> at 0x000002560E064940> # 其实也就是lambda的函数地址.
print(fn2()) # 100 # 函数名()就是调用函数.
# 当函数调用时, 才能获得返回值.



# lambda计算a+b并返回结果

# 使用函数实现:
def add(a, b):
    return a + b

result = add(1, 2)
print(result)

# lambda实现
print((lambda a, b: a + b)(1, 2)) # 3

gc.collect()


# lambda参数形式:
# 1. 无参数
fn1 = lambda :100
print(fn1()) # 100

# 一个参数
fn1 = lambda a: a # 输入什么, 就返回什么
print(fn1(1)) # 1 #

# 默认参数: 写法与使用和在函数当中相同.
fn1 = lambda a, b, c=100: a + b + c
print(fn1(10, 20)) # 130
print(fn1(10, 20, 200)) # 230


# 可变参数: 和函数使用一样.
fn1 = lambda *args: args
print(fn1(10, 20, 30)) # (10, 20, 30) # 自动装箱.
# args就是一个元组类型, *args就是散列的数据.

# 可变关键字参数 和函数中使用一样
fn1 = lambda **kwargs: kwargs #
print(fn1(name='python', age=20)) # {'name': 'python', 'age': 20}
# kwargs是一个字典, kwargs是关键字的散列数据.


# lambda的应用
# 三木运算符
fn1 = lambda a, b: a if a > b else b
print(fn1(2, 3)) # 3

# 列表数据按照字典key的值排序.
students = [
    {'name': 'tom', 'age': 20},
    {'name': 'rose', 'age': 19},
    {'name': 'jack', 'age': 32},
    {'name': 'join', 'age': 23},
]

students.sort(key=lambda x: x['name']) # key就是指定按照什么进行排序.
# 就是按照key进行排序.
# x就是列表中单独的元素, 使用lambda就是按照x['name']进行排序.

students.sort(key=lambda x: x['age'], reverse=True) # 按照age降序派去
print(students) #


























