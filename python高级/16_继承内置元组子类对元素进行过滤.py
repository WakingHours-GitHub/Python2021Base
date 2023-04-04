# 实现继承内置元组子类型对元素的过滤功能

class IntTuple:
    def __init__(self, iterable):
        self.result = tuple([x for x in iterable if isinstance(x, int) and x > 0])

    """
    两个问题: IntTuple不是内置元组子类
    另外, 想要print(对象)直接返回结果.
        想要将治理对象的值组成一个元组 -> 重写__new__方法, 创建一个类的实例对象. 
    
    
    """
class IntTuple2(tuple):
    def __new__(cls, iterable): # __new__是一个静态方法, 是一个类对象,
        result = (x for x in iterable if isinstance(x, int) and x > 0)

        return super().__new__(cls, result)
        # 再new方法中进行过滤, 并且使用父类中的new方法对结果进行处理.
        # 这是一个元组子类. 然后直接打印实例对象就是元组. 

res = IntTuple2([1, -2, 3, 'x', 'y'])
print(res) # (1, 3)
# 直接返回元组.






