class Date:
    # 构造函数:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    # 实例方法
    def tomorrow(self):
        self.day += 1

    @staticmethod  # 如果我们需要函数, 但是不需要使用到类的时候, 就可以使用到静态方法.
    def valid_str(date_str: str):
        year, month, day = tuple(date_str.split('-'))
        if int(year) > 0:
            return True
        else:
            return False

    # 静态方法
    @staticmethod  # 跟普通的函数一摸一样.
    def parse_from_string(date_str: str):  # 不需要传递任何对象或者类
        year, month, day = tuple(date_str.split('-'))
        return Date(int(year), int(month), int(day))  # 采用硬编码的方式. 不会根据自己这个类改变而改变.
        # 所以就产生了另一种方法, 就是类方法.

    # 类方法.
    @classmethod
    def from_string(cls, date_str):  # cls是类本身, 类本身也是一个对象.
        year, month, day = tuple(date_str.split('-'))
        return cls(int(year), int(month), int(day))

    def __str__(self):
        return f"{self.year}/{self.month}/{self.day}"


class User:
    def __init__(self, birthday: Date):
        self.__birthday = birthday  # 相当于private

    def get_age(self):
        return 2022 - self.__birthday.year


def main() -> None:
    user = User(Date(1990, 2, 1))
    # user.__birthday # 变量被隐藏, 实际上是变形了.
    # 变成: _class__attribute, Python并没有作到绝对安全. 
    print(user._User__birthday)  # 1990/2/1
    print(user.get_age())  # 32.


if __name__ == '__main__':
    main()
