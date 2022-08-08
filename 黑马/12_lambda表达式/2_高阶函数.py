"""
高阶函数, 把函数作为参数传入, 这样的函数称之为高阶函数,
高阶函数是函数式编程的体现, 函数式编程就是指这种高度抽象的编程范式.


在python中
    abs(x): 取绝对值
    round(x): 对数字进行四舍五入



"""


# 体验高阶函数:

# 提前了解这两个函数
# abs(): 取绝对值
print(abs(-10)) # 10 # 取绝对值操作


# round(x): 取四舍五入
print(round(9.5)) # 10
print(round(9.4)) # 9


# 需求: 任意两个数字, 按照指定要求整理数字后再进行求和计算.
def add_num(a, b, f): # 可以根据f传入的函数, 来对a,b 进行操作, 从而提高灵活性.
    return f(a) + f(b)

result = add_num(-1, 2, abs) # 注意, 这里的abs是没有()的, 因为是传入句柄, 不是调用
print(result)

# 函数式编程大量使用函数, 减少了代码的重复, 因此程序会更加简洁, 函数更加灵活.
# 这种方式, 就是函数式接口. # 也就是预留一个函数位置, 当作参数, 根据传入的函数, 做相应的操作
# 以此称为: 函数式接口


# 练习:
# 任意两个数字, 陷阱行数字处理, (绝对值或者四舍五入)再就和计算
def add_num1(a, b): #  不够灵活, 无法更换函数
    return abs(a) + abs(b)

result = add_num1(-1.1, 1.9)
print(result)

# 函数式编程
def sum_num2(a, b, f):
    """

    :param a:
    :param b:
    :param f: 是一个函数类
    :return:
    """
    return f(a) + f(b)


result = sum_num2(-1, 5, abs) # 注意, 这里是函数入口, 不是调用abs函数'
print(result) # 6


result = sum_num2(1.2, 3.5, round)
print(result) #  5

# 使用函数式编程更加灵活.
# 将函数本身, 作为另外一个参数传入函数进行操作.




