"""
super()效用父类方法
    之前实现过调用父类的方法. 使用父类名.方法名()
    那么和super()方法有什么不一样呢?
    super方式:
    super(当前类名, self).函数()
    super().函数
    super()可以自动查找父类, 调用顺序遵循mro顺序, 比较适合单继承使用.




"""
# 首先书写多继承
class Master(object):
    def __init__(self):
        self.kongfu = "[古法煎饼果子配方]"
    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

class School(Master):
    def __init__(self):
        self.kongfu = '[黑马煎饼果子配方]'
    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子') #

        # use parameter super() form
        # super(School, self).__init__()
        # super(School, self).make_cake()

        # 使用无参数的super()形式
        # use parameter-free super() form
        super().__init__()
        super().make_cake()


class Prentice(School):
    def __init__(self):
        self.kongfu = '[独创煎饼果子技术]'
    def make_cake(self):
        self.__init__()
        self.kongfu = '[独创煎饼果子技术]'

    # 子类调用父类的同名方法， 将父类的同名属性和方法封装
    def make_master_cake(self):
        Master.__init__(self)
        Master.make_cake(self)

    def make_school_cake(self):
        School.__init__(self)
        School.make_cake(self)

    # 打印所有方法
    def print_all_method(self):
        super().__init__()
        super().make_cake() # 调用School的make_cake方法



# create a Peentice object
tudi = Prentice()

tudi.print_all_method() # 调试, 查看代码运行顺序.
# 运用[黑马煎饼果子配方]制作煎饼果子
# 运用[古法煎饼果子配方]制作煎饼果子

