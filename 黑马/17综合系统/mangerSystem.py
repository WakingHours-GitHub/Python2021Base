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


# 定义管理系统的类
class StudentManager(object):
    def __init__(self):
        # definite object attribute
        self.student_list = list()  # create list type.

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
                pass
            elif menu_num == 2:  # delete
                pass
            elif menu_num == 3:  # alter(modify)
                pass
            elif menu_num == 4:  # search information
                pass
            elif menu_num == 5:  # show all information
                pass

            elif menu_num == 6:  # save student information
                pass

            elif menu_num == 7:  # exit system
                print("exit student management system")
                break

    def load_student(self):
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
        system function menu:
            1. add student
            2. delete student
            3. modify student
            4. inquire student information
            5. show all student information
            6. save student information
            7. exit system
        """)

    def add_student(self):
        print("add student")


if __name__ == '__main__':
    StudentManager().run()
