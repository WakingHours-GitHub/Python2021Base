"""
类方法, 与类属性一样, 隶属于类本身.
因此可以不创建对象, 而直接使用类本身去调用.

类方法:
    类方法需要使用@classmethod装饰器来定义,
    类方法的第一个参数是类本身.
    @classmethod
    def get_instance(cls): # 这里的cls是python自己传进去的. 就是类本身.
        return cls() # 相当于返回cls的实例. 也就是该类本身的对象

    我们可以不生成该类的对象, 而直接使用类来去调用类方法.
    类方法一般是干什么? :
        上面那个例子就是, 我们可以使用类本身来创建对象

静态方法:
    静态方法使用@staticmethod装饰器来定义.
    静态方法只是定义在类的范围内的一个函数而已.
    跟这个类没关系, 就是一个函数, 只是定义到了类里面而已.
    调用: 类.函数名
    一般定义工具类的时候, 使用静态方法. 也就是我们不需要使用实例的东西.
    因此如果我们没使用self, 我们就可以定义为静态方法.




"""


class Student:
    school = "shenzhen university"  # 类变量.

    @classmethod
    def hello(cls):
        print(f"hello{cls.__name__}")

    @classmethod  # 注解, 装饰器.
    def get_instance(cls):
        return Student()  # 返回该类的实例.

    @staticmethod
    def out():  # 没有任何参数.
        print(f"hells {Student.school}")

    def speak(self):  # 实例方法.
        self.out()  # 可以
        Student.out()  # 可以.


def main() -> None:
    # print("Main:")
    Student.hello()  # Student.hello(Student) #  python默认会将该类传入进去
    print(Student.__name__)

    Student.out()  # hells shenzhen university


if __name__ == '__main__':
    main()
