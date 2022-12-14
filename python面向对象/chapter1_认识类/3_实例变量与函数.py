"""
实例函数的定义.
认识__init__函数.
定义实例变量.
实例函数中访问实例变量.
外部访问实例变量与函数.


实例函数的定义.
    实例函数, 就是隶属于实例的函数. 实例函数属于对象.
    实例函数其实就是实例属性. 实际上, 保存的都是句柄.
    class :
        def function(self, parameter list):
        # 必须有一个参数:　self. 这才是实例属性.
            pass

认识__init__函数:
    __init__()函数是用于初始化对象的实例函数.
    Python中每个类都默认有这样一个函数.
    __XXX__这种格式称之为魔法函数.

"""


class Student:
    def __init__(self, name: str):
        # 初始化函数. 用途: 定义实例属性, 这些属性隶属于对象. 只有在对象被创建的时候, init中的变量在被初始化.
        self.name = name  # 定义实例属性. 都必须隶属于对象.
        # 这里的self就是传入的对象.

        pass

    def say_hello(self, message: str):  # 定义了一个实例函数
        # 在实例函数中通过self访问实例变量, 因为都是一个self(同一个对象)
        print(f"hello {message}, {self.name}") # self就是传入的对象, 每个对象都有不同的name值.


def main():
    # 一定要说执行那个对象的say_hello
    # 1. create a physical object
    # 2. call __init__() to initialize this object
    s1 = Student("Jack")  # 实际上这里已经定义了__init__函数了.这里默认就是调用了这个init方法.
    s2 = Student("Tom")  # type类中, 定义了__call__?

    s1.say_hello("hahaha")  # 定义的时候是两个参数, 传参数的时候只有一个参数.
    # 这就是实例函数和普通函数的区别.
    # 其实这个self已经传参数了, 就是调用对象本身 -> self.
    # s1.say_hello(s1, "hahaha") # s1 -> self, "hahaha" -> message

    print(type(Student))  # <class 'type'>

    # Python是一个动态语言:
    s1.gender = "Male"
    print(s1.gender) # 在运行过程中, 给第一个对象加了一个属性.


if __name__ == '__main__':
    main()
