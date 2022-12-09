"""
什么是类变量
定义类变量
取得类变量的值
设置类变量的值
删除类变量
类变量的存储


类变量:
    CLass Valuable
    属于类本身的这个对象属性. 类本身是一个type的对象, 所以这里类变量是属于这个类对象的.
    所有该类的对象都共享类变量. 共享同一个类变量.
    类似于Java中的静态变量. 就是类变量, 随着类的定义而定义.
定义类变量:
    直接再类中定义.
    不需要创建具体实例, 我们就可以访问类变量.
取得值:
    直接类.类变量,
    或者使用getattr(类: object, "类变量名": str, None)函数
    如果getattr()没有找到类变量, 那么我们可以返回default也就是默认值.

设置类变量的值
    直接类.类变量 = 赋值
    或者使用setattr(类, "类变量", value)
    # 类似于Java中的反射机制.
    如果不存在, 我们可以在运行时, 直接增加这个类变量.

删除类变量
    既然可以动态的增加, 那么我们就可以删除.
    使用del操作符, 或者delattr()函数'

类变量的存储
    类变量为什么能够动态存储:
    __dict__这是一个特殊的类变量. 这是一个字典.
    类变量全部存放在类变量__dict__这个字典中, 但是不是直接修改__dict__的内容.
    可以浏览, 但是不要修改.

"""

from pprint import pprint

class Student:
    # 定义变量:
    student_count = 0
    pass


def main():
    # __name__继承自Object类, 默认打印当前类的名字.;
    print(Student.__name__)  # Student

    print(Student.student_count)  # 直接这样写. 类本身也是一个变量
    print(getattr(Student, "student_count"))  # 0. # 就是
    # print(Student.unknown) # AttributeError: type object 'Student' has no attribute 'unknown'
    print(getattr(Student, "unknown", "10"))  # 动态.

    # 改变类变量的值
    Student.student_count = 90
    print(Student.student_count)  #
    setattr(Student, "student_count", 100)  # 使用编程的方式动态修改类变量.
    print(Student.student_count)  # 100

    Student.unknow = "test"  # 动态的加上一个属性
    print(Student.unknow) # test

    # del Student.unknow
    # delattr(Student, "unknow")

    # print(Student.unknow) # 报错


    # 类变量的存储:
    # 类变量是根据类来存储的. 类也是一个对象, 当然存储在类中.
    s1 = Student()
    s2 = Student()

    s1.student_count = 4
    print(s1.student_count) # 4
    print(s2.student_count) # 4
    # 类和对象都共享这个变量.

    pprint(Student.__dict__ ) # {'__module__': '__main__', 'student_count': 100, '__dict__': <attribute '__dict__' of 'Student' objects>, '__weakref__': <attribute '__weakref__' of 'Student' objects>, '__doc__': None, 'unknow': 'test'}
    """ # 使用pprint: 
    mappingproxy({'__dict__': <attribute '__dict__' of 'Student' objects>,
              '__doc__': None,
              '__module__': '__main__',
              '__weakref__': <attribute '__weakref__' of 'Student' objects>,
              'student_count': 100,
              'unknow': 'test'})
        """

if __name__ == '__main__':
    main()
