"""
书写student类.
学员信息要包含: 姓名, 性别, 手机号
添加__str__()方法,  方便查看学员对象的信息.

"""

# 书写student类
class Student(object):
    def __init__(self, name, gender, tel):
        self.name = name
        self.gender = gender
        self.tel = tel



    def __str__(self):
        return f"name: {self.name}, gender: {self.gender}, tel: {self.tel}"


# 测试: 只有
if __name__ == '__main__':
    xiaoming = Student("xiaoming", "male", "123")
    print(xiaoming)