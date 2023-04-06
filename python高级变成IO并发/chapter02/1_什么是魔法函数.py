from typing import List


# 魔法函数: 以__开头和结尾. 这些就是魔法函数,
# 通过这些个魔法函数, 可以定制这些类的特性. 每一种魔法函数对应着一种功能. 往往是隐式的调用.
# 通过这些方法, 可以影响我们的对象, 以及python的内置函数. 例如len()
# len()首先会调用__len__()方法, 如果没有则尝试getitem()方法. 这个len方法并不简单.
# str()方法,就会调用__str__().
# 开发模式: 调用__repr__模式. 在notebook中输出的时候.

"""
魔法函数分为两类: 一种是非数学运算另一种是数学运算.


"""

class Company(object):
    def __init__(self, employee_list: List):
        self.employee = employee_list

    # 魔法函数: 以__开头和结尾. 这些就是魔法函数,
    # 通过这些个魔法函数, 可以定制这些类的特性.
    def __getitem__(self, item):  # 就是直接索引对象。返回相应结果。
        return self.employee[item]

    # def __iter__(self): # 迭代器, 需要实现这个方法.


    def __len__(self):
        return len(self.employee)

    def __str__(self):
        return ".".join(self.employee)


company = Company(["tom", "bbb", "jane"])
# 实现了__getitem__函数, 可以使用切片了.
company1 = company[: 2]  # 我们实现了所谓的魔法函数, 实际上是增强了这个对象的一些功能
# 这里是隐式调用.

print(len(company)) # 3
# 底层也是会先调用__len__()方法, 这个过程是隐式的.
# list, set, dict等内置的数据类型, 实际上都是由cpython实现的.
# 在使用len方法时, 是在底层c语言直接取到的, 所以速度非常快.


print(str(company)) # tom.bbb.jane


for em in company:  # for实际上是拿到这个对象的迭代器. 如果拿不到迭代器则尝试getitem方法. 直到报异常.
    print(em)
