"""
自省: 是通过一定的机制查询到对象的内部结构





"""


class Person:
    name = "user" # name属于Person这个类(对象)


class Student(Person):  # 继承.
    """
    文档, 在__doct__中的__doc__属性.

    """
    def __init__(self, school_name):
        self.school_name = school_name


def main() -> None:
    user = Student("离谱")
    # 通过__dict__来查询属性., python通过cpython实现的__dict__, 速度高校.
    print(user.__dict__)  # {'school_name': '离谱'}

    print(Person.__dict__) # {'__module__': '__main__', 'name': 'user', '__dict__': <attribute '__dict__' of 'Person' objects>, '__weakref__': <attribute '__weakref__' of 'Person' objects>, '__doc__': None}
    # 类对象属性更加丰富.
    print(user.name)  # user, 会向上查找. 根据mro(方法查找顺序)


    # 同样, 我们可以在__dict__里添加对象的属性, 然后直接调用就可以了
    user.__dict__["school_addr"] = "北京市"
    print(user.school_addr) # 北京市 # 可见, 同样可以取到

    # dir()列出对象中的所有属性, 比__dict__更加强大. 更加通用. 
    print(dir(user)) # ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'name', 'school_addr', 'school_name']



if __name__ == '__main__':
    main()
