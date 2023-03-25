"""
为元组中的每个元素命名提高程序的可读性.
大量的索引会降低程序的可读性.


"""


# 方式一, 定义类似与其他语言中的枚举类型.
def instance_0() -> None:
    student = ("离谱", 16, "长沙")
    NAME, AGE, ADDRESS = range(3)  # 元组拆包.
    print(student[NAME], student[AGE], student[ADDRESS])






# 使用另外的元组类型.
def instance_1() -> None:
    from collections import namedtuple # 是tuple的子类.


    # 对象 = namedtuple(名字, 可迭代对象)
    student_obj = namedtuple("student", ['name', 'age', 'address']) #
    print(student_obj)
    student = student_obj("lipu", 19, "南京")
    student1 = student_obj(name="离谱", age=19, address="南京")
    print(student)
    print(student1)


    # 取值, 类似于面向对象的格式.
    print(student.name, student.age, student.address)



if __name__ == '__main__':
    # instance_0()
    instance_1()