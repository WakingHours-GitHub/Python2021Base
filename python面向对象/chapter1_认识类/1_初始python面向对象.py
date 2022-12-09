"""
面向对象的概念解释
类的定义
对象的创建
isinstance()函数
Python中的类本身也是一个对象

面向对象的概念:
    类, 描述一类对象的特征集合. 一个抽象的概念, 不是一个具体的. intangible.
    对象, 符合类的定义特征的具体实例. tangible.
    属性, 分为类属性, 实例属性.    静态特征.
    方法, 分为类方法, 和实例方法.  动态特征

类的定义
    use 'class' key word
    使用大驼峰命名规范.

对象的创建
    对象 = 类().
    返回的对象, 其实就是一个变量, 指向真正存放对象的地址.

isinstance()函数:
    isinstance()函数用来判断一个对象是不是一个类的对象.

类本身再内存中是什么样子的?
    类本身也是一个对象, 他是一个什么类型的对象?
    是type的对象.
    Student = type() # 动态创造类. 是更高级的东西.




"""


# 类的定义:
class Student:
    # class body
    pass  # 占位符.


class Person:
    pass


def main():
    print(Student)  # <class '__main__.Student'> # 这就是一个类

    student_1 = Student()  # 返回的是存放对象的地址, new 一个新对象.

    print(student_1)  # <__main__.Student object at 0x0000021DC9579FD0>
    # 类 object at 内存地址. memory address.
    print(id(student_1))  # 取出唯一识别码, 实际上就是内存地址的十进制, 所以我们一般也称之为唯一识别码
    print(hex(id(student_1)))  # 转换成16进制后, 我们就能够知道这就是地址.

    # 地址一定是唯一的, 所以对象也肯定是唯一的.
    # 这个student_1中存放的其实就是地址, 也就是说student_1指向了真正存放的对象. 里面只是存放地址.
    print(isinstance(student_1, Student))  # student_1是不是Student的实例. 结果为True.
    print(isinstance(student_1, Person))  # False.

    print(type(Student))  # <class 'type'> # type类型?
    print(isinstance(Student, type))  # Ture


if __name__ == '__main__':
    main()
