'''
练习:

定义一个登陆函数，参数是：username，password
函数体：
判断参数传过来的username,password是否正确，如果正确则登陆成功，否则打印登陆失败
'''

# 函数的定义
def login(username, password): # 注意函数体的缩进
    # 相当于数据注册的用户名和密码
    uname = "admin123"
    pwd = "123123"

    for i in range(3): # 循环三次, 只有三次机会
        if username == uname and password == pwd:
            print("登录成功!")
            break # 登录成功就退出
        else:
            print("登录失败")
            username = input("输入用户名")
            password = input("输入密码")
    else: #  for-else: else在for迭代器为空的时候进入
        print("账户锁定")   

# 调用部分
username = input("输入用户名")
password = input("输入密码")
login(username, password) # 调用函数

