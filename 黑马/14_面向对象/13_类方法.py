"""

类方法和静态方法:
    类方法:
        类方法特点:
            需要使用装饰器@classmethod来表示为类方法, 对于类方法, 第一个参数必须是类对象, 一般以cls作为第一个参数.
            标记为类方法的函数, 第一个参数默认为cls.
        类方法的使用场景:
            当方法中需要使用类对象时(如访问私有类属性时)定义类方法.
            类方法一般和类属性配合使用.

    静态方法:
        静态发方法特点:
            需要使用装饰器@staticmethod进行装饰, 静态方法既不需要传递类对象需要传递实例对象.(形参没有cls, self)
            静态方法也能够通过实例对象和类对象去访问.

        静态方法使用场景:
            当方法中既不需要使用实例对象(属性和对象), 也不需要使用类对象(类属性, 方法)时, 静态定义方法
            取消不需要的参数传递, 有利于减少不必要的内存占用和性能消耗.
            静态方法, 不需要参数传递, 有利于减少不必要的内存占用和性能消耗.

        静态方法可以通过类或者对象调用.

"""
class Dog():
    __tooth = 10

    @classmethod
    def get_tooth(cls):
        # cls就是本类
        return cls.__tooth

# 创建对象
# 对象可以调用类方法
wangcai = Dog()

print(wangcai.get_tooth()) # 10


# 静态方法:
class Dog(object):
    @staticmethod
    def print_info():
        print("这是dog类别")


# 创建对象
wangcai = Dog()
wangcai.print_info()

Dog.print_info()

# 静态方法, 可以通过类和对象去调用.









