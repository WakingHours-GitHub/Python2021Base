"""
权限问题:
java中, 定义权限, 是有一套标识符的, 例如public, private, protect
但是在python中, 私有属性, 完全依赖命名.

私有属性与函数的用途
如何定义私有属性和函数
如何访问私有属性与函数

私有属性与函数的用途:
    在面向对象的封装中, 私有的属性与函数其根本目的是防止它们在类的外部被使用.
    在Python中并没有严格的权限限定符去进行限制
    主要通过命名来进行区分.

    但是也不是完全不能访问到, 我们会留下接口, 通过get, set函数进行访问与赋值.

如何定义私有属性和函数:
    通过给属性或函数名添加_或者__前缀, 注意, 我们只关心前缀.
    _ : protect保护类型, 在外部可以用, 但是要小心
    __: private私有的. 在外部无法访问.
    但是python没那么严格, 我们只需要注意, 最好不要在外面调用即可.






"""


class Student:
    def __init__(self, name: str):
        self._name = name
        self.__name1 = name+"name1"

    def _say_hello(self, msg: str):
        print(f"hello: {msg}, {self._name}")

    def __say_hello1(self, msg: str):
        print(f"hello: {msg}, {self._name}")

def main() -> None:
    s1 = Student("Jack")
    print(s1._name) # 原则上不能访问, 单其实是不能阻止的.

    # print(s1.__name1) # AttributeError: 'Student' object has no attribute '__name1'
    # __, 原则上无法访问, 但其实我们还是有方法进行访问:
    print(s1._Student__name1) #  Jackname1 # 可见, 我们仍然可以访问__变量.
    # 使用_类名字__属性名字, 就可以访问__这个私有属性.
    print(s1._say_hello("hahaha"))

    print(s1._Student__say_hello1("haha1"))




if __name__ == '__main__':
    main()
