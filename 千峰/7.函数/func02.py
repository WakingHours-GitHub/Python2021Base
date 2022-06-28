# 函数的下一个部分: 带有参数的函数
# 就是在参数列表中声明参数
"""
def 函数名(参数列表):
    函数体

调用:
    pass
    函数名(参数...)

"""

# 产生随机数的函数, 产生的个数由参数决定
import random

# 定义函数
def generate_random(number): # 这里的参数是形式上的参数, 所以称为实参
    for i in range(number):
        ran = random.randint(1,20)
        print(ran)

# 调用函数, 一定要加(), 用以区别变量和函数
generate_random(10) # 产生十个随机数
generate_random(5) # 调用时传入的参数: 实参：即实际的参数，　具体的值

# 学习调试模式
# 断点, 程序执行到断点处就暂停了
# 调试: 也称为Debug

# 求加法的函数
# 传参数
def add(a,b):
    result = a + b
    print(result)
# 调用函数:
add(2,3)
add(1,2)

"""
练习:

定义一个登录函数, 参数是username, password
函数体:
判断参数传过来的username,password是否正确，如果正确则登陆成功，否则打印登陆失败
"""


# 


