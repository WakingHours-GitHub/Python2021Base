class Date:
    # 构造函数:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    # 实例方法
    def tomorrow(self):
        self.day += 1

    @staticmethod # 如果我们需要函数, 但是不需要使用到类的时候, 就可以使用到静态方法.
    def valid_str(date_str:str):
        year, month, day = tuple(date_str.split('-'))
        if int(year) > 0:
            return True
        else:
            return False

    # 静态方法
    @staticmethod  # 跟普通的函数一摸一样.
    def parse_from_string(date_str: str): # 不需要传递任何对象或者类
        year, month, day = tuple(date_str.split('-'))
        return Date(int(year), int(month), int(day)) # 采用硬编码的方式. 不会根据自己这个类改变而改变.
            # 所以就产生了另一种方法, 就是类方法.


    # 类方法.
    @classmethod
    def from_string(cls, date_str): # cls是类本身, 类本身也是一个对象.
        year, month, day = tuple(date_str.split('-'))
        return cls(int(year), int(month), int(day))

    # 当然上面的self, cls都是一种名称而已, 只是我们约定而已.





    def __str__(self):
        return f"{self.year}/{self.month}/{self.day}"


def test() -> None:
    new_day = Date(2018, 12, 31)
    new_day.tomorrow()  # 自动将这个对象传入进去:
    # tomorrow(new_day)
    print(new_day)

    # 现在我有一个需求, 就是从字符串解析出来一个date对象.
    date = "2020-10-20"
    year, month, day = tuple(date.split('-'))
    new_day = Date(int(year), int(month), int(day))
    print(new_day)



    # 用staticmethod完成初始化
    new_day = Date.parse_from_string(date)
    print(new_day)

    # 用classmethod完成初始化
    new_day = Date.from_string(date)
    print(new_day)


if __name__ == '__main__':
    test()
