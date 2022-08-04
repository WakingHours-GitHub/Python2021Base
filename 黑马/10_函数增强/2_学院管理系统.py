"""
需求分析:
    需求: 进入系统显示系统功能页面:
    1. 添加学员
    2. 删除学员
    3. 修改学员信息
    4. 查询学员信息
    5. 显示所有学员信息
    6. 退出系统


步骤:
    显示功能页面
    用户输入功能序号
    根据用户输入的功能序号, 执行不同的函数


"""


# 开始书写代码:
def menu():
    """
    display function menu.
    :return:
    """
    print('\t'+'--'*10+"""
    请选择功能: 
        1. 添加学员
        2. 删除学员
        3. 修改学员信息
        4. 查询学员信息
        5. 显示所有学员信息
        6. 退出系统
    """+'--'*10)

# 系统功能需要循环使用, 直到退出系统, 才退出系统.
while True:
    # 显示功能界面:
    menu()


    # 用户输入功能序号:
    user_num = eval(input("请输入功能序号: "))

    # 按照用户输入的功能序号, 执行不同的功能. -> 多重判断
    if user_num == 1:
        print('添加')
    elif user_num == 2:
        print("删除")
    elif user_num == 3:
        print("修改")
    elif user_num == 4:
        print("查询")
    elif user_num == 5:
        print("显示所有")
    elif user_num == 6:

        print("退出系统")
        break
    else:
        print("未找到输入的序号, 请重新输入")





