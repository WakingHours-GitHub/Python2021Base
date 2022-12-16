"""
如何防止实例变量被外部错误修改
编写setter和getter方法
引入property类.
因为一些场景而生

场景一: 我们如何防止外部变量篡改实例变量.
    我们可以通过setter或者getter方法来来实现访问和修改

场景二: 如何保留self.attr这种写法, 不做重构?
    引入property类.

"""


class Student:
    def __init__(self, name: str, age: int):
        self.name = name
        self.__age = age  # 一种解决方法, 我们可以设置为私有的. # 但是我们又想改变这个值那么我们怎么办

    def get_age(self):
        return self.__age

    def set_age(self, age: int):  # 增加判断语句.
        if age < 0 or age > 200:
            raise Exception(f'Age is {age} is not valid')
        self.__age = age  #

    def __str__(self) -> str:
        return f"{self.name}, {self.__age}"

    age = property(fget=get_age, fset=set_age) # 这是类变量.
    # age这个其实就是一个代理, 这个属性指向的是property的对象.
    # 如果是赋值, 那么就调用这个对象的fset方法.
    # 如果是打印, 就调用fget方法. 


def main():
    student = Student("Jack", 18)
    student.age = 22 # 错误值. age怎么可能是负数. # 调用这个对象的fse方法
    print(student.age) # 如果是
    # student.set_age(-2) # 报错了. 我们就可以通过set函数来去进行一些逻辑判断.
    student.get_age()  # Jack, 18

    print(student)  # Jack, -2


if __name__ == '__main__':
    main()
