"""
很易于理解: 所谓函数调用和就是指函数里面又调用了另外一个函数.



"""


def testB():
    print("testB start")
    print("testB end")


def testA():
    print("testA start")
    testB()
    print("testA end")


testA()


# 函数调用案例:
# 函数嵌套调用, 实现多条横线的打印
def print_line():
    print('-' * 20)


def print_lines(num):
    for i in range(num):
        print_line()


print_lines(5)


# 函数计算:
# 求三个数之和
def sum(a, b, c):
    return a + b + c


result = sum(1, 2, 3)  # 函数有返回值, 因此使用变量接收函数的返回值.


# 求三个数平均值
def average(a, b, c):
    """求取三个数的平均值"""
    return sum(a, b, c) / 3


result = average(1, 2, 3)

print(result)
