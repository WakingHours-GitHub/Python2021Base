"""
__dict__变量
这个属性是我们类变量, 以及实例对象都拥有的一个属性. 这
这个属性的作用: 手机类对象或实例对象的属性方法以及对应的值, 封装返回一个字典.
"""


class A(object):
    a = 0  # 类属性

    def __init__(self):
        self.b = 1  # 对象属性(实例属性)


aa = A()  # 创建对象
# 返回类内部所有属性和方法对应的字典.
print(A.__dict__)
# {'__module__': '__main__', 'a': 0, '__init__': <function A.__init__ at 0x000001E3E0844550>, '__dict__': <attribute '__dict__' of 'A' objects>, '__weakref__': <attribute '__weakref__' of 'A' objects>, '__doc__': None}
# 打印的就是类的属性.
# 包括__module__, a, ...
# 及其对应的值.
# 返回的结果都是一个字典.

# 返回实例属性和值组成的字典.
print(aa.__dict__)
# {'b': 1}
# 打印的就是对象的属性.
