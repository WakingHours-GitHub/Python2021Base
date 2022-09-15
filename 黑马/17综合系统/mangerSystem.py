"""
存储管理系统. 相关文件.
需求:
    存储数据的位置: 文件
        加载数据文件
        修改数据后保存到文件
    存储数据形式: 列表存储学员对象
    功能:
        添加学员
        删除学员
        修改学员
        查询学员信息
        显示所有学员信息
        保存学员信息

    定义程序入口函数.
        加载数据, 从文件加载数据.
        显示功能菜单
        用户输入功能序号
        根据用户输入的功能序号执行不同的功能.
    定义系统功能函数, 添加删除学员等等.



"""
from typing import List

from student import *


# 定义管理系统的类
class StudentManager(object):
    def __init__(self):
        # definite object attribute
        self.student_list: List[Student] = list()  # create list type.
        # 这里指定为list类型, 成员变量为Student对象.

    # 管理系统内部的框架:
    # 程序入口:
    def run(self):
        # load student data, not loop
        self.load_student()
        while True:
            # show menu
            self.show_menu()

            # input
            menu_num = int(input("please input function range number: "))

            # execute different function.
            if menu_num == 1:  # add
                self.add_student()
            elif menu_num == 2:  # delete
                self.delete_student()
            elif menu_num == 3:  # alter(modify)
                self.modify_student()
            elif menu_num == 4:  # search information
                self.inquire_student()
            elif menu_num == 5:  # show all information
                self.show_all_student()
            elif menu_num == 6:  # save student information
                self.save_student()
            elif menu_num == 7:  # exit system
                print("exit student management system")
                break

    def load_student(self):
        """
        load data from 'student.data' file,
        and we should be operate data that in file,
        so, we have to load data
        step:
            1. try read file, if file not exist, then we use 'w' mode to open file.
            2. if file exist, then load data and save data
                a. load data
                b. transition data type: from list.dict to Student object
                c. save student data to list
            3. close file
        """
        try:
            f = open("./student.data", 'r')
        except: # file not exist
            f = open("./student.data", 'w')

        else: # file already exist
            # data type: [{}, {}, {}] in list, thus we use 'eval()' function,
            # to execute, then from this type to List[dict] type
            data = f.read()
            student_dict_list = eval(data)
            # create object and input self.student_list
            self.student_list = [Student(student['name'], student['gender'], student['tel']) for student in student_dict_list]

        finally:
            # 3. 关闭文件
            f.close()





        pass

    # 1. show menu
    @staticmethod
    def show_menu():  # this is a static method, because it don't require any parameter
        """
        system function menu:
            1. show menu
            2. add student
            3. delete student
            4. modify student
            5. inquire student information
            6. show all student information
            7. save student information
            8. load student information
        """
        print("""
    --------------------------------
        system function menu:
            1. add student
            2. delete student
            3. modify student
            4. inquire student information
            5. show all student information
            6. save student information
            7. exit system
    --------------------------------
        """)

    def add_student(self):
        """用户输入学员姓名, 性别, 手机号, 然后添加到系统当中去. """
        print("add student")
        while True:
            input_infor = input("please input name, gender, tel, and split by space(enter 'q' to exit): \n")
            if input_infor == 'q':  # only input 'q' to exit loop
                break
            name, gender, tel = tuple(input_infor.strip().split(' '))
            s = Student(name, gender, tel)  # 创建对象
            self.student_list.append(s)  # 添加到当前学生列表当中去.

        # print(self.student_list) # 测试

    def delete_student(self):
        """input target name, to delete this student """
        print("delete student")
        while True:
            name = input("please input name that delete name(input 'q' to exit): ")
            if name == 'q':
                break
            # elif name in [name_list.name for name_list in self.student_list]: # 直接使用列表生成式.
            #     print(f"already deleted \'{name}\' student")
            #     self.student_list.remove()
            # else:
            #     print(f"name is \'{name}\' not exist, please input again")
            for student in self.student_list:
                if student.name == name:
                    self.student_list.remove(student)
                    break
            else:
                print(f"name is \'{name}\' not exist, please input again. ")
            """
            或者遍历列表: 使用for-else
            for i in self.student_list:
                if del_name == i.name:
                    ...
            else:
                "no this name".print
            """
            # print(self.student_list) # test

    def modify_student(self):
        """用户输入学员姓名, 如果学员存在则修改学员信息"""
        print("modify student")
        while True:
            name = input("please input name that modify student name(input 'q' to exit): ")
            if name == 'q':
                break
            for student in self.student_list:
                if student.name == name:
                    new_name, new_gender, new_tel = input(
                        "please new information that include name, gender and tel: ").strip().split(' ')
                    # update information
                    student.name = new_name
                    student.gender = new_gender
                    student.tel = new_tel
                    break

            else:
                print(f"name is \'{name}\' not exist, please input again")

    def inquire_student(self):
        """research student information"""
        print("inquire student information")
        while True:
            name = input("please input name that inquire student's name(input 'q' to exit): ").strip()
            if name == 'q':
                break
            for student in self.student_list:
                if name == student.name:
                    print(student)  # output student information
                    break
            else:  # student not exist
                print(f"no \'{name}\' student")

    def show_all_student(self):
        print("show all student information")
        print("name\t gender\t  tel: ")

        for student in self.student_list:
            print(student)  # we definite __str__ magic method

    def save_student(self):
        """
        save student information
        file operation.

        """
        print("save student information")
        # open file pointer.
        f = open("./student.data", "w")

        # file input file
        # 2.1 student information in list input to file.
        # 2.2 input data that str type to file
        student_dict_list = [student.__dict__ for student in self.student_list]
        # print(student_dict_list) # [{'name': '1', 'gender': '1', 'tel': '1'}] #
        # evey element is dict that present student information in list.

        # write in file
        f.write(str(student_dict_list))


        f.close()




if __name__ == '__main__':
    StudentManager().run()
