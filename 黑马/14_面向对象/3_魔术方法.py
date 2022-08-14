"""
再python中, __xxx__()的函数叫做魔法方法, 是具有特殊功能的函数

__init__():
    初始化对象.
    __init__()方法, 在创建一个对象时, 默认被调用, 不需要手动调用
    __init__()中的self参数, 不需要开发者传递, python会将当前对象自动传入进入.

    __init__()同样可以带有参数.
    一个类可以创建对象, 可以通过__init__()传入参数, 为对象设置不同的初始化属性.

__str__():
    当print输出对象时, 默认打印对象的内存地址. 当如果类定义了__str__()魔术方法
    那么就会打印__str__() return的数据.
    print打印时, 默认调用的就是类的__str__方法, 所有类都继承自Object类. 因此当该类没有写__str__方法时, 默认找到父类的__str__方法,进行打印.
    print函数默认是这样的:
        print(object.__str__())
    书写__str__魔术方法, 可以更好的表达打印类的信息.

__del__():
    当删除对象时, python解释器默认会调用__del__()方法
    当程序结束时, 也会调用清理函数



"""

# 定义init方法, 设置初始化属性, 并且访问调用.
# 定义类:

class Washer():

    def __init__(self):
        # 添加实例属性
        self.width = 200
        self.height = 300


    def print_info(self):
        print("宽度", self.width)
        print("高度", self.height)

# 创建对象
haier = Washer()

haier.print_info()




# init函数传入参数
class Washer2():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def print_info(self):
        print("宽度", self.width)
        print("高度", self.height)

# 使用参数创建多个不同的对象
haier1 = Washer2(10, 20)
haier1.print_info()

haier2 = Washer2(300 ,400)
haier2.print_info()

# 宽度 10
# 高度 20
# 宽度 300
# 高度 400
# 可见, 我们可以通过传入init的参数来控制不同对象的实例属性.


# __str__()方法:
# 定义类
class Washer3():

    def __init__(self) -> None:
        self.width = 300

    def __str__(self) -> str:
        return "解释说明: 打印对象信息, 或者类的说明"

# 创建对象
haier = Washer3()
print(haier)
print(haier.__str__())
# 解释说明: 打印对象信息, 或者类的说明
# 解释说明: 打印对象信息, 或者类的说明
# 可见, 打印对象和打印对象.__str__()方法输出一样.
# 因此print函数默认底层就会调用对象的__str__()方法.


# __del__()方法
class Washer4():
    def __init__(self):
        self.width = 300
    def __del__(self):
        print("对象已经被删除")

haier = Washer4()
# 对象已经被删除
# 自动调用. 