"""
多层继承：
    就是多层继承。
    子类依然继承父类的所有方法.
    方法解析顺序, 依然按照就近原则. 去查找






"""

# 创建师傅类
class Master(object):
    def __init__(self):
        self.kongfu = '[古法煎饼果子配方]'
    def make_cake(self):
        print(f"使用{self.kongfu} 制作煎饼果子")

class School(object):
    def __init__(self):
        self.kongfu = '[黑马煎饼果子配方]'
    def make_cake(self):
        print(f"使用{self.kongfu} 制作煎饼果子")

# 徒弟类:
class Prentice(School, Master):
    def __init__(self):
        self.kongfu = '[独创煎饼果子配方]'
    def make_cake(self):
        self.__init__() # 这里不用传入self, 因为就是直接将self传入进去.
        print(f"使用{self.kongfu} 制作煎饼果子")

    def make_school_cake(self):
        School.__init__(self)
        School.make_cake(self)

    def make_Master_cake(self):
        Master.__init__(self)
        Master.make_cake(self)

# 创建徒孙类:
class Tusun(Prentice):
    pass

# 创建徒孙对象
tusun = Tusun()

# 打印方法解析顺序
print(Tusun.mro()) #
# [<class '__main__.Tusun'>, <class '__main__.Prentice'>, <class '__main__.School'>, <class '__main__.Master'>, <class 'object'>]
# 可见依然是遵循就近原则.

print(tusun.kongfu)
# tusun继承了Prentice类中的属性

tusun.make_cake() # 使用[独创煎饼果子配方] 制作煎饼果子

tusun.make_school_cake() # 使用[黑马煎饼果子配方] 制作煎饼果子

tusun.make_Master_cake() # 使用[古法煎饼果子配方] 制作煎饼果子





















