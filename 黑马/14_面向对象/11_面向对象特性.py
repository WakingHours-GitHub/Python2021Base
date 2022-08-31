"""

面向对象三大特性。
    封装, 继承, 多态.
    封装:
        将属性和方法写道类里的操作即为封装
        封装可以为属性和方法添加私有权限
    继承
        子类默认继承父类的所有属性和方法
        子类可以重写父类属性和方法
    多态
        传入不同的对象, 产生不同的结果

多态:
    多态指的是一类事物有多种形态, 一个抽象类有多个子类, 因此, 多态的概念依赖于继承.
    定义:
        多态是一种使用对象的方式, 子类重写父类方法, 调用不同子类的对象的相同父类方法, 可以产生不同的执行结果.
        python多态不一定要依赖于继承, 但是最好要依赖于继承, 重写父类的方法, 然后一个父类可以有多个子类, 并且都能够
            创建对象, 因此, 不同子类对象传入父类的方法时, 将会产生不同的执行结果.
        好处: 调用灵活, 有了多态, 更加容易编写出通用的代码, 做出通用的编程, 适应需求的不断变化.
    实现步骤:
        定义父类, 提供公共方法
        定义子类, 并重写父类方法
        传递子类对象给调用者, 可以看到不同子类执行效果不同.




"""


"""
需求:　警务和警犬一起工作．　追击敌人和追查敌人
    携带不同的警犬, 执行不同的工作.

步骤:
    1. 定义父类: 提供父类方法
    2. 定义子类: 子类重写父类方法
    3. 创建对象, 调用不同的功能, 传入





"""

# 定义父类: 提供公共方法
class Dog(object):
    def work(self):
        pass


# 定义子类, 子类重写父类方法: 定义两个类表示不同的警犬, 那么所作的工作也不同.
class ArmyDog(Dog):
    def work(self):
        print("追击敌人")

class DrugDog(Dog):
    def work(self):
        print("追查毒药")

# 定义人类, 用于携带.
class Person(object):
    def work_with_dog(self, dog: Dog): # 这个dog就是一个父类,
        # 那么传入子类后, 根据不同子类, 调用子类的work方法, 这样就是他本类所对应的方法
        dog.work()

# 创建对象, 传入不同的对象, 看结果
# 创建对象:
ad = ArmyDog()

dg = DrugDog()

person = Person()
# 这就是多态:
# 多态可以使代码更加灵活, 更加丰富.
person.work_with_dog(ad) # 追击敌人
person.work_with_dog(dg) # 追查毒药













