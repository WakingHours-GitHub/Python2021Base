from collections import abc

"""
collections的abc类(基类)实现了大多数的容器的抽象基类.
但是我们更细化叫这种抽象基类为协议, 只要我们满足了协议所规定的函数, 那么我们这个类就是一个序列类.
可以查看Sequence和MutableSequence, 看看内部符号哪种协议.

"""
# 序列操作里面的三种操作: +, +=, extend的区别.


a: list = [1, 2]
# a:list = list()

# + 只能是同种类型..
c = a + [3, 4]  # 返回了一个新的列表.
print(c)  # [1, 2, 3, 4]

# += 原地操作. 可以是任何序列类型
# 通过__iadd__魔法函数实现. 原理就是调用__iadd__的逻辑.
# 通过源码我们可以看到, 就是self.extend(values). 所以传入可迭代的类型都是
a += (3, 4)
print(a)  # [1, 2, 3, 4]



a.extend(range(3)) # 只需要是iterable类型就都可以
# 但是这个函数没有返回值. 直接在a上进行修改.
# a = a.extend(),
print(a)


# a.append() # 是一次行添加元素
# a.extend() # 是迭代添加.
# 不要搞混.


