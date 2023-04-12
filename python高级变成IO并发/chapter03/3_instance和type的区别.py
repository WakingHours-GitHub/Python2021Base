"""
推荐使用isinstance(), 会检查我们的继承链


"""

class A:
    pass


class B(A):
    pass


b = B()
print(isinstance(b, B))
print(isinstance(b, A))
print(type(b)) # <class '__main__.B'>
print(type(b) is B)  # True 检查id是否相等。type返回的就是B, 是B吗,
print(type(b) is A)  # False.
