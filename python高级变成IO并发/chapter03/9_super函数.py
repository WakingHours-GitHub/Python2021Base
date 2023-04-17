"""
如果学过Python面向对象, 那么就应该知道super实际上就是调用父类的构造函数.




"""


class A:
    def __init__(self):
        print("A: __init__")


class B(A):
    def __init__(self):
        print("B: __init__")
        super().__init__()  # python3写法.
        # super(B, self).__init__() # python2的写法

from threading import Thread
class MyThread(Thread):
    def __init__(self, name, user):
        self.user = user
        super().__init__(name=name)

# 既然我们重写了B的构造函数, 那么我们为什么还需要去调用super?
#   复用代码. 有时候super函数是我们必须调用的.
# super到底执行顺序的是什么? mro算法.
class C(A):
    def __init__(self):
        print("C: __init__")
        super().__init__()
class D(B, C):
    def __init__(self):
        print("D: __init__")
        super().__init__()

def main() -> None:
    # b = B()
    d = D()
    print(D.__mro__) # (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
    # 所以, 注意. super()不是调用父类构造函数的意思, 而是调用mro顺序的下一个类的构造函数.
    """
    D: __init__
    B: __init__
    C: __init__
    A: __init__
    """

if __name__ == '__main__':
    main()
