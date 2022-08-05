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

    删除学员:
        接收输入, 然后删删除这个数据
        判断输入用户是否存在, 才能删除.

    修改学员信息:
        接收输入, 找到该学员.
        然后修改学员的信息, 例如id和tel

    查询学员信息:
        接收输入, 找到该学员
        然后打印该学员信息, 如果没有, 需要提示.

    查询所有学员信息:
        很简单, 就是遍历info即可.

"""

# 开始书写代码:
import gc


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

    if new_name in [info_dict['name'] for info_dict in info]:  # 使用列表推导式生成name序列, 然后直接判断是否存在, 以此判断.
        print("成员姓名存在, 无法重复添加")  # 提示信息
        return  # 弹栈, 结束函数

    else:  # 输入数据不存在, 则添加数据到列表当中
        # 创建新字典
        info_dict = {}  # {}默认是空字典, set()才是空集合
        info_dict['id'] = new_id  # 如果key存在, 则修改, 如果id不存在, 则新增键值对
        info_dict['name'] = new_name
        info_dict['tel'] = new_tel
        # print(info_dict)

        # 添加到列表当中
        info.append(info_dict)

    # pass  # 占位, 保留逻辑, 避免语法错误


def del_info():
    """
    删除学员信息.
    :return:
    """
    global info  # 声明局全局变量.

    del_name = input("请输入要删除的学员的姓名")  # 接收输入
    for i in info:  # 遍历列表, i是字典
        if del_name == i['name']:  # 删除列表中的字典
            info.remove(i)  # 根据内容删除, 就是remove函数
            print(del_name + " 用户已经删除")
            # print(info) # 测试使用
            break  # 如果删除了, 则直接推出 -> 提高效率./
    else:  # 如果for没有break(正常结束), 那么也就是没有del_name的信息.
        print(del_name + " 成员不存在, 没有删除")

    return


# 修改学员信息:
def modify_info():
    """
    修改学员信息
    :return:
    """
    global info

    name = input("要修改的学员的姓名")
    for i in info:
        if name == i['name']:
            print("正在修改" + name + " 学员信息")
            # id, tel key存在, 所以是修改对应的value.
            i['id'] = input('学号')
            i['tel'] = input("手机号")
            break  # 提高效率
    else:
        print("没有" + name + "成员信息")

    return


# 查询学员信息
def search_info():
    """
    查询学员信息
    :return:
    """
    global info

    name = input("请输入要查询学员的姓名")

    for i in info:
        if name == i['name']:
            print(name + " 学员, 信息如下.")
            print(i)
            break
    else:
        print(name + " 学员， 不存在")

    return

def print_all_info():
    """
    显示所有学员信息
    :return:
    """

    print('%-10s %-10s %-10s' % ("学号", "姓名", "手机号"))
    # 使用格式化字符串, 定义宽度
    for i in info:
        print(i)

# 系统功能需要循环使用, 直到退出系统, 才退出系统.
while True:  # 不断循环, 系统不能够停止.
    gc.collect()
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
        del_info()
    elif user_num == 3:
        print("修改")
        modify_info()
    elif user_num == 4:
        print("查询")
        search_info()
    elif user_num == 5:
        print("显示所有")
        print_all_info()
    elif user_num == 6:
        if input("确定要推出吗? (y or n): ") == "y":
            print("退出系统")
            break
        # break  # 退出循环.

    else:  # 判断输入错误序号时的代码.
        print("未找到输入的序号, 请重新输入")
