"""
面向对象基础:
    理解面向对象
    类和对象
    添加和获取对象属性
    魔术方法

理解面向对象
    面向对象是一种抽象化的编程思想.
    面向对象就是将编程当作一个事务, 对于外界来说, 事务是直接使用的, 不用去管它内部的情况.
    而编程就是定义事物能够做什么.

    理解洗衣机. 创造洗衣机, 然后使用洗衣机洗衣服.
    图纸 -> 洗衣机 -> 洗衣服
    类   -> 对象


类和对象:
    类和对象的关系: 用类去创建对象, 用类实例化一个对象.
    创建, 就是实例化.

    类: 是对一系列具有相同特征和行为的事物的统称, 是一个抽象的概念, 不是真实存在的事务.
        是一个抽象的概念.
        特征 -> 属性
        行为 -> 方法

    对象: 对象是类创建出来的实例. 是存在的. 具体的. 具象化的.

面向对象实现方法:
    定义类:
        语法:
            class 类名([继承类, ...]):
                属性
                方法

            类的名字遵循大驼明明规范.
    创建对象:
        语法:
            对象 = 类名() # 实例化

    self:
        self就是调用处的对象. 以引用的方式传值.
        self就是对象本身.






"""



# 需求: 洗衣机, 功能: 洗衣服
# 1. 定义洗衣机类
class Washer():

    # 行为 -> 方法
    def wash(self):
        # 这个self就是对象本身.
        print("洗衣服")
        print("self", self)


# 2. 创建对象
washer = Washer() # 实例化对象.

# 3. 使用对象调用函数
print(washer) # <__main__.Washer object at 0x0000022E7FD5AFD0>

# 使用wash方法 -> 实例方法/对象方法, 使用'.'成员运算符, 调用函数.
washer.wash() # 使用功能



# self.
haier = Washer()
# 用类创建对象, 则这个对象拥有该类所有的属性和方法
haier.wash()
print("haier", haier)
# 洗衣服
# self <__main__.Washer object at 0x000001DAB0E39F10>
# haier <__main__.Washer object at 0x000001DAB0E39F10>
# 可见, 打印self和haier的内存地址一摸一样
# 因此self就是调用的那个对象. 传入回self了. self就是对象本身的意思!


# 一个类可以创建多个对象
# 多个对象调用函数时, 看self的地址.

haier1 = Washer()
haier1.wash()

haier2 = Washer()
haier2.wash()
# 洗衣服
# self <__main__.Washer object at 0x0000025F53AD9F10>
# 洗衣服
# self <__main__.Washer object at 0x0000025F53AD9EE0>
# 可见, 一个类是可以创建多个对象, 并且创建的对象不相同. 内存地址不同.

