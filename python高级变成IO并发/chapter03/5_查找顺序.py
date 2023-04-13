# Python的属性查找算法, C3算法.

# 新式类.
class D:
    pass

class C(D):
    pass

class B(D):
    pass

class A(B, C):
    pass


print(A.__mro__) # 查找属性的顺序, 会放到类的__mro__属性中
# (<class '__main__.A'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.D'>, <class 'object'>)