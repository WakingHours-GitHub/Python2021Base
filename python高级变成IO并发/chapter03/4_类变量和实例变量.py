class A:
    aa = 1  # 类变量, 属于类.

    def __init__(self, x, y):
        # self: 是这个类的实例(对象), 所以self.都是实例变量.
        self.x = x
        self.y = y


a = A(2, 3)
print(a.x, a.y, a.aa)  # 2 3 1
"""首先先查询self自身的变量,  如果没有, 就查询类变量. 向上查找"""
print(A.aa)  # 1 这是类的变量, 我们应该通过类来去访问.
# A不能找到实例变量.


"""如果变量.属性=100, 如果这个属性在对象中没有, 那么就会创建一个, """
a.aa = 100
print(a.aa)  # 100, 新开辟出来一个实例对象, aa.
print(A.aa)  # 1
# 此时a.aa就是实例属性, 而A.aa还是类变量.
print(a.__class__.aa)

A.aa = 100
b = A(3, 5)
print(b.aa) # 100
# 这个类变量, 是属于类的. 所以是共享的.


# Python的属性查找算法, C3算法.
print(A.mro())