"""

各种数据类型:
    数值:
        int: 整形
        float: 浮点型
    布尔型: bool

    str: 字符串
    list: 列表
    tuple: 元组
    set: 集合
    dict: 字典

检测数据类型: type(检测的数据) -> 返回该数据的数据类型




"""


num1 = 1
num2 = 1.1

print(type(num1)) # <class 'int'> 整形
print(type(num2)) # <class 'float'> 浮点型

# str -> 字符串, 用""or''括起来的都是字符串类型.
a = "Hello World"
print(type(a)) # <class 'str'> 字符串

# bool -> 布尔型, 通常判断使用, 有两个取值True和False
b = True
print(type(b)) # <class 'bool'>


# 认识其他几种复合类型:
# list -> 列表
c = [10, 20, 30]
print(type(c))

# tuple -> 元组
d = (10, 20, 30)
print(type(d))


# set -> 集合
e = {10, 20, 30}
print(type(e))

# dict -> 字典. 以键值对方式存储的.
f = {"name":"Tom", "age": 18}
print(type(f))












