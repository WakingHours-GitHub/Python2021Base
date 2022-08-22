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






















































