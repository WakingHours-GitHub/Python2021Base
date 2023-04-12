"""
深入理解类和对象:
    鸭子类型和多态.
    当你看见一只鸟走起来像鸭子,叫起来也像鸭子,那么这只鸟就可以被称之为鸭子.

    Python的多态非常灵活.
    Python的多态, 依赖于同一个方法. 不像Java, 需要子类继承父类, 同时重写方法.
    这也就是我们在使用Python的时候, 要转变的思想. 就是不要局限于类型.
    因为有多态, 例如iterable,可迭代对象, 可以是list, tuple, set, 甚至是generator等.
    不要局限于数据类型, 因为有多态的存在.
    iterable对象, 需要类去实现, __iter__方法, 或者退化为__getitem__()方法
    所以, 我们在python中更关注于是什么什么类型(类别). 而不是什么什么特定数据类型.
    P








"""

class Cat(object):
    def sya(self):
        print("i'm a cat")















