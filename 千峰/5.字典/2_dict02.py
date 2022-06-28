'''
案例:
用户注册功能

username
password
email
phone

'''

# 欢迎界面:
print('-'*10,'欢迎来到互联招聘用户注册','*'*10, sep='')

# 模拟数据库(用啦存储)
database = [] # 保存每个用户的数据
'''
[
    user1 {},
    user2 {},
    ...    
]
'''

while True:
    username = input('输入用户名:')
    password = input('输入密码:')
    repassword = input('输入确认密码:')
    while password != repassword:
        repassword = input("请重新输入密码:")
    print("密码确认成功:")
    email = input('请输入邮箱:')
    phonenum = input("输入手机号:")

    # 定义一个字典:
    user = {} # 保存用户信息
    # 保存到字典里
    user['username'] = username
    user['password'] = password
    user['email'] = email
    user['phonenum'] = phonenum

    database.append(user) # 将临时的用户保存到列表里面去

    if input("是否要继续注册(y/n)") != 'y':
        break
print(database)



