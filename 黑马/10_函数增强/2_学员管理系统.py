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

考虑存储学员信息的数据结构, -> 即, 列表嵌套字典使用.
每一个字典是一个学员信息, 列表就是总的数据表, 并且该变量是全局变量, 因为无论是增加, 查询, 删除都需要使用该变量

功能分析:
    添加学员:
        接受输入, 并且按照指定格式添加学员
        判断是否已经有学员信息


"""


# 开始书写代码:
def menu():
    """
    display function menu.
    :return:
    """
    print('\t' + '--' * 10 + """
    请选择功能: 
        1. 添加学员
        2. 删除学员
        3. 修改学员信息
        4. 查询学员信息
        5. 显示所有学员信息
        6. 退出系统
    """ + '--' * 10)


info = list(dict())  # 生成空列表. 容器, 存储所有学员的信息.


# 添加学员信息的函数
def add_info():
    """
    添加学员函数
    :return:
    """
    global info  # 声明容器 全局变量, 不能使用局部变量

    # 用户输入, 学员, 姓名, 手机号
    new_id = input('学号')
    new_name = input("姓名")
    new_tel = input("手机号")

    # 判断是否在学员列表中

    if new_name in [info_dict['name'] for info_dict in info]: # 使用列表推导式生成name序列, 然后直接判断是否存在, 以此判断.
        print("成员姓名存在, 无法重复添加")  # 提示信息
        return # 弹栈, 结束函数

    else: # 输入数据不存在, 则添加数据到列表当中
        # 创建新字典
        info_dict = {} # {}默认是空字典, set()才是空集合
        info_dict['id'] = new_id # 如果key存在, 则修改, 如果id不存在, 则新增键值对
        info_dict['name'] = new_name
        info_dict['tel'] = new_tel
        # print(info_dict)

        # 添加到列表当中
        info.append(info_dict)


    # pass  # 占位, 保留逻辑, 避免语法错误


# 系统功能需要循环使用, 直到退出系统, 才退出系统.
while True:  # 不断循环, 系统不能够停止.
    # 显示功能界面:
    menu()

    # 用户输入功能序号:
    user_num = eval(input("请输入功能序号: "))

    # 按照用户输入的功能序号, 执行不同的功能. -> 多重判断
    if user_num == 1:  # 增加
        add_info()  # 调用函数.
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
        break  # 退出循环.

    else:  # 判断输入错误序号时的代码.
        print("未找到输入的序号, 请重新输入")
