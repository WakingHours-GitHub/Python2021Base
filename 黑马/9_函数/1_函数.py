"""

函数的作用:
    实现代码复用, 模块化, 方便维护和调试
    函数就是将一段具有独立功能的代码块整合到一个整体并命名, 在需要的位置调用这个名称即可完成对应的需求.

定义函数: define
    def 函数名(参数列表):
        代码...
        
调用函数:
    函数名(参数列表)

    函数必须先定义后使用
    函数名必须满足标识符规则.

函数注意事项:
    函数先定义后调用, 如果先调用后定义则会报错
    函数定义不会被执行, 函数必须被调用时才会被执行.

参数的作用: 使函数更加灵活, 在调用时修改

函数的返回值的作用:
    需要将函数的处理结果继续使用, 此时就需要返回值了. 可以使用变量接收
    语法:
        return
    return的特点:
        return后就函数弹栈, 退出函数了, 因此return后面的语句不执行
        并且将返回值返回给调用处.

函数的说明文档。
    快速查找函数文档: help(函数名) # 注意, 仅仅是函数名不是函数名(), 不是调用函数
    help的作用就是快速打印函数的说明信息
    如何书写自定义函数的说明文档:
        def 函数名(参数列表):
            '''说明文档的位置''' # 第一行的多行注释, 就是函数的说明文档
            代码



"""

# 快速体验函数.

# 封装函数:
import numpy


def sel_func():
    print("显示余额")
    print('存款')
    print('取款')


print("恭喜您登录成功")

sel_func()

print("显示余额, 为100")

sel_func()

print("取了100元")

sel_func()


# 函数参数: 固定数 1, 2 的加法
def add_num1():
    result = 1 + 2
    print(result)
add_num1() # 3

# 使用参数
# 定义函数时定了占位符, 这种参数是形参, 满足命名规则, 建议做到见名知意
def add_num2(a, b):
    result = a + b
    print(result)

# 调用函数时, 传入真实的数据为实参
add_num2(1, 2)
add_num2(10, 20) # 30
# 使用起来更加灵活.

# add_num2(10) # TypeError: add_num2() missing 1 required positional argument: 'b'
# 注意, 形参和实参个数需要相等


# 函数的返回值.
def buy():
    return "烟"

goods = buy()
print(goods)


# 应用: -> 制作一个加法器
def sum(a, b): # a, b都是形参
     return a + b


print(sum(10, 20)) # 将结果直接打印.

# 函数的说明文档
def sum_num(a, b):
    """求和函数"""
    return a+b
help(sum_num)
# sum_num(a, b)
#     求和函数


# 函数的说明文档的高级使用 -> 需要开启功能. 
# 在函数体第一行, 使用多行注释并且
def sum_num1(a, b):
    """
    求和函数sum_num1
    :param a: 参数1
    :param b: 参数2
    :return: 返回值
    """
    return a+b

help(sum_num1) # 打印的信息比较全面
