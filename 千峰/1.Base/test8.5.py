# 字符串的格式化输出
# 方式: 1. 使用占位符 2.format

# format 是一个字符串中的函数, '...{}...'.format() ,此处的.表示调用(类似java)

age = 20
NAME = '张三分'
# 这里的{}也是类似占位的意思, .format就是填入这里的
message = '名字:{}, 今年{}岁'.format(NAME, age)
print(message)


# input(prompt = None) 标准的输入流（这里是键盘）

name = input('请输入名字') # 阻塞式(需要回车)
print(name)


# 做练习:
print('''
***********************
        捕鱼达人
***********************
''')

userName = input('请输入参数游戏者用户名')
password = input('请输入密码')

print('%s请充值才能加入游戏!' % userName)

coins = input('请充值') # input()从键盘输入的都是str类型,即使输入的是数字,也同样是'数字'(字符串)
# print(type(coins))
# 解决方法: 强转
coins = int(coins)

print('%s充值成功, 还剩余%d个币' % (userName, coins))

# 练习2
print('''
***********************
        英雄联盟
***********************
''')

role = input('请输入使用的角色')
equipment = input('输入拥有的装备')
upgrade_equipment = input('输入需要购买的装备')
pay = input('输入付款金额')

# 变量的赋值替换
equipment = upgrade_equipment # 更新装备

print('{}拥有{}装备, 购买{}该装备花了{}钱'.format(role, equipment, equipment, pay)) # 这里格式字符串不一定要使用format
