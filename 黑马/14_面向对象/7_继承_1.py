"""
继承:
    继承的概念
    单继承
    多继承
    子类重写父类的同名属性和方法
    子类调用父类的同名属性和方法
    多层继承
    super()
    私有属性和私有方法

继承的概念:
    子类继承父类的属性和方法.

经典类和新式类:
    经典类: python 2.0
    class 类名:
        代码
    新式类: python 3.0
    class 类名(Object):
        代码
    ()中, 写入该类继承的父类, 可以填写多个父类, 用','分隔
    Object类是顶级类(基类), 所有类默认都继承Object类

单继承:
    就是一个子类 继承一个父类

多继承:
    一个子类, 继承多个父类
    ()中, 放入多个父类. 当一个类有多个父类时候, 默认使用第一个父类的同名属性和方法.

子类重写父类同名方法和属性
    python是没有重载的, 因为python有可变位置参数, 和可变关键字参数.

MRO -> method resolution order -> 方法解析顺序
print(Class.__mro__) # 查看类的层级关系.
print(Class.mro())


子类调用父类的同名方法和属性.
    如果方法解析顺序我们可以通过mro这个函数查看,
    默认是遵循就近原则, 那么我们如何访问父类的属性和方法呢.







"""

# 体验继承
# 子类默认继承父类的所有属性和方法.
class A(object):
    def __init__(self):
        self.num = 1
    def info_print(self):
        print(self.num)

# 定义子类, 并继承父类
class B(A):
    pass # 占位.

# 3. 创建对象,
b = B()
b.info_print() #  可见
# 可见, 子类默认继承父类的所有属性和方法,



# 单继承
# 师傅类
class Master(object):
    def __init__(self):
        self.kongfu = '[古法煎饼果子配方]'
    def make_cake(self):
        print(f'运用{self.kongfu} 制作煎饼果子')

# 徒弟类
class Prentice(Master):
    pass

# 创建对象
daqiu = Prentice()

print(daqiu.kongfu) # [古法煎饼果子配方]
# 访问成员属性
daqiu.make_cake() # 运用[古法煎饼果子配方] 制作煎饼果子


# 多继承.
# 为了验证多继承, 我们创建school类:
class School(object):
    def __init__(self):
        self.kongfu = '[黑马煎饼果子配方]'
    def make_cake(self):
        print(f'运用{self.kongfu} 制作煎饼果子')
# 属性名和方法名和Master类相同, 为了测试多继承特性.

# 定义徒弟类
class Prentice(School, Master):  # 这就是多继承的写法
    pass
# 一个类有多个类时, 默认使用第一个父类的同名属性和方法.

# 用徒弟类创建对象, 调用实例属性和方法.
daqiu = Prentice()
print(daqiu.kongfu) # [黑马煎饼果子配方]
daqiu.make_cake() # 运用[黑马煎饼果子配方] 制作煎饼果子
# 可见, 调用的是School中的属性和方法,
# 因此多继承, 再有同名方法和同名属性时, 优先继承最前面的父类.

# 子类, 重写父类方法.
# 定义徒弟类
class Prentice(School, Master):
    def __init__(self):
        self.kongfu = "[独创煎饼果子方法]"

    def make_cake(self):
        print(f'运用{self.kongfu} 制作煎饼果子')

# 创建对象, 并且调用其中方法
daqiu = Prentice()

print(daqiu.kongfu) # [独创煎饼果子方法]
daqiu.make_cake() # 运用[独创煎饼果子方法] 制作煎饼果子
# 如果是子类和父类同时拥有同名属性和方法, 默认是使用子类, 然后第一个父类, 由此类推
# 这遵循就近原则.


# 查看类的父类, 以及父类的层级关系
# .__mro__
print(Prentice.__mro__) #
# (<class '__main__.Prentice'>, <class '__main__.School'>, <class '__main__.Master'>, <class 'object'>)
# 按照这个属性, 查找属性和方法.
print(Prentice.mro()) #
# [<class '__main__.Prentice'>, <class '__main__.School'>, <class '__main__.Master'>, <class 'object'>]
# 输出这个类的mro属性.


# 子类, 访问父类的属性和方法.
# 这其中涉及到多态的概念.
# 重写徒弟类:
class Prentice(School, Master):
    def __init__(self):
        self.kongfu = "[独创煎饼果子技术]"
    def make_cake(self):
        self.__init__() # 重新加载自己类的方法

        # 不进行初始化, 当调用父类属性和方法时, 则会将原属性和方法覆盖掉, 因此我们需要执行self.__init__()方法
        print(f'运用{self.kongfu} 制作煎饼果子')

    # 子类调用父类同名方法和属性, 需要将父类的同名属性和方法再次封装.
    # 即需要调用父类的init方法, 将self自身的属性和方法(句柄)更新到父类的地址上去. 这样再调用时, 就是父类中的属性和方法了.
    def make_master_cake(self):
        # 并且我们还需要传入self, 需要指定是覆盖哪个对象.
        print("Master前"+type(self).__str__(self)) # Master前<__main__.Prentice object at 0x000001F4BCC00100>
        Master.__init__(self) # 重载父类的属性和方法, 此时self中的属性和方法就是Master中的属性和方法了
        print("Master后"+type(self).__str__(self)) # Master后<__main__.Prentice object at 0x000001F4BCC00100>

        # 然后我们调用make_cake方法, 此时调用的就是Master中的make_cake方法
        Master.make_cake(self) # 还需要将self传入进去, 此时这个self中的属性和方法, 就是Master中的属性和方法.

    # 同理, 对于school也是如此
    def make_school_cake(self):
        School.__init__(self) # 传入self, 将self.kongfu 赋值成为school对应的属性
        # 然后类.方法名, 将self传入
        School.make_cake(self)


# 创建对象
daqiu = Prentice()

daqiu.make_cake() # 运用[独创煎饼果子技术] 制作煎饼果子

daqiu.make_master_cake()
# 运用[古法煎饼果子配方] 制作煎饼果子
# 可见, 此时已经是

# 如果我们再调用make_cake()时, 此时self中的属性和方法就是Master中的属性和方法
daqiu.make_cake() # 运用[古法煎饼果子配方] 制作煎饼果子

# 因此需要在自己的make_cake中添加, self.__init__()重新加载自己类的属性和方法.
# 此时再调用, 就是自己的属性和方法
daqiu.make_cake() # 运用[独创煎饼果子技术] 制作煎饼果子



daqiu.make_school_cake()
# 运用[黑马煎饼果子配方] 制作煎饼果子
















































