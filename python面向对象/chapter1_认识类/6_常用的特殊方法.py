"""
常用的特殊方法.
__str__
__repr__
__eq__
__hash__
__bool__
__del__
魔法方法. 双下划线开头和结尾.

__str__:
    __str__方法用于返回一个描述对象本身的字符串, 该描述主要面向用户.

__repr__:
    represent: 呈现.
    __repr__方法用于返回一个描述对象本身的字符串, 该描述的主要目标是机器或者开发者.
    也是返回字符串. 区别: 目的不一样. 设计的目的不一样.
    增加调试信息, 我们就可以使用repr

__eq__:
    __eq__方法, 用来实现比较两个实例相等的逻辑.
    在==符号时候, 默认调用__eq__方法.

__hash__:
    __hash__方法用于实现根据对象生成hash值的逻辑.
    set, dict, 数据结构中, 就是根据散列值来进行存放的.
    性能是非常高的. 直接根据hash值找到你的位置.
    我们可以自己定义hast值的生成, 或者使用默认, object提供的也可以.
    hash的目的就是生成不同的数值.

__bool__:
    __bool__方法用于在对象被bool函数求解的时候返回一个布尔值.
    如果没有实现, 那么__len__将会被用户求解布尔值. 就是返回调用__len__函数.
    当bool(对象)调用的时候就会默认调用该函数.

__del__:
    __del__方法在对象被垃圾回收前调用
    因为对象合适被回收, 不知道, 所以不要依赖于这个方法去做一些重要的事情.
"""


class MyDate:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        print("str is called")
        return f"{self.year}-{self.month}-{self.day}"  # 写描述信息.

    def __repr__(self):
        """信息更多, 我们要看程序是不是正常执行的. """
        return f"MyDate: {self}"

    def __eq__(self, other):
        if not isinstance(other, self.__class__): # 这里我们要传入class. 所以我们使用self.__class__
            return False
        else:
            return self.year == other.year and self.month == other.month and self.day == other.day

    def __hash__(self):
        print("__hash__ is called")
        return hash(self.year+self.month*101+self.day*101) # 直接使用hash进行出来.
        # 当你将这个对象放到set, dict中, 他都会调用该对象的__hash__方法.

    def __bool__(self):
        return self.year > 2014


    def __del__(self):
        print(f"{id(self)} is deleted")


def main() -> None:
    mydate_1 = MyDate("2022", "11", "3")
    mydate_2 = MyDate("2022", "11", "3")
    mydate_3 = mydate_1


    print(MyDate("2022", "11", "3"))  # 2022-11-3
    # print的时候, 就会默认调用该类的__str__方法. 这就是为什么任何实例都可以被print.
    print(str(MyDate("2022", "11", "3")))  # 2022-11-3
    # 同理, str()方法, 默认也是会调用实例的__str__方法.

    print(repr(MyDate("2022", "11", "3")))  # 调用repr方法.

    print(mydate_1 == mydate_1) # 比较是不是同一个对象.?  但是比较不出来. 实际上就是调用我们的__eq__方法进行比较
    # 本质上等于mydate_1.__eq__(mydate_2), 但是我们还没有重写__eq__所以我们返回None.
    # 重写__eq__后, 我们使用==比较符号, 此时就是调用__eq__魔术方法.

    print(mydate_1 is mydate_3) # True. 用于比较是不是同一个对象. 比较所存储的地址.
    # is是比较对象, 引用是不是指向同一个对象.

    print(bool(mydate_1)) # True


    set().add(mydate_1) # __hash__ is called


    mydate_2 = None # 指向空.


if __name__ == '__main__':
    main()
