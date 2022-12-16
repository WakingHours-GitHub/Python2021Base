"""
@property装饰器

@property装饰器.
    只是用来访问, 用来放在get这种函数前面.
    然后函数名改成原来兼容性的名字.


@property_name.setter 装饰器.
    名字要一致



"""


class Student:
    def __init__(self, name: str, age: int):
        self.name = name
        self.__age = age  # 一种解决方法, 我们可以设置为私有的. # 但是我们又想改变这个值那么我们怎么办


    # 对外. 觉得你有什么.
    @property  # 用来访问的. 必须定义为property的装饰器, 然后下面才能定义setter.
    def age(self):  # 加上property装饰器, 这个函数, 就会变成属性.
        # 对外, 就是有一个属性, 叫做age.
        return self.__age

    @age.setter  # 这边的age要和下面的age一致, 因为这是set函数
    def age(self, age: int):  # 增加判断语句.
        if age < 0 or age > 200:
            raise Exception(f'Age is {age} is not valid')
        self.__age = age  #

    def __str__(self) -> str:
        return f"{self.name}, {self.__age}"


def main():
    student = Student("Jack", 18)
    student.age = -3 #
    print(student.age)  # 修改成功

    print(student)


if __name__ == '__main__':
    main()
