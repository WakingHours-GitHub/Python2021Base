"""
私有权限.
定义私有属性和方法:
    可以为实例属性和方法设置私有权限, 即设置某个实例属性或实例方法不继承给子类
    子类和类外 是无法访问到私有属性的.
    方法:
        在属性名和方法名前 加上两个下划线: '__'
    私有属性和方法访问范围:
        只有本类内可以访问到, 类外均访问不到.





"""
class Prentice(object):
    def __init__(self):
        # 公有权限
        self.kongfu = '[独创煎饼果子配方]'
        # 定义私有属性, 类外也无法访问.
        self.__money = 100

    def make_cake(self):
        print(self.__money)
        print(f"使用{self.kongfu} 制作煎饼果子")
        self.__make_secret_cake()

    # 定义私有属性
    def __make_secret_cake(self):
        print("秘密配方")



class Tusun(Prentice):
    pass


# 创建对象
prentice = Prentice()
# print(prentice.money) # 报错, 类外也访问不到
prentice.make_cake()
# 100
# 使用[独创煎饼果子配方] 制作煎饼果子
# 秘密配方



tusun = Tusun()
# print(tusun.money) # AttributeError: 'Tusun' object has no attribute 'money'







