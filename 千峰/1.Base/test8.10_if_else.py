# 条件判断语句
'''
python中严格控制缩进, 在if下,Tab一个,同级别的为一个代码块{}
python中没有switch-case

第一种形式
if 表达式:
    表达式为真的语句


第二种形式
if 表达式 :
    表达式为真的语句
else :
    表达式为假


第三种形式,级联的ifelse
if 条件表达式1:
    1为真时的语句
elif 条件表达式2:
    2为真时的语句
elif ...:
    ...
    
...
else:

第四种就是嵌套


上面几种形式都可以嵌套使用

'''

username1 = 'admin'
username2 = ''
if username1:  # 没有运算符
    print(username1, '已经登录了')
    # 执行

if username2:  # 没有关系运算符
    print(username2, '已经登录了')
    # 不执行

# Python默认将字符串''(空), 数值0, None等值认为False

num1 = 0
if num1:
    print(num1)  # 执行

num2 = 9
if num2:
    print(num2)  # 不执行
'''
所以
num <==> num != 0 ('', None)
'''

# 练习:
# 如果年龄大于18岁 并 输入姓名, 则打印XXX今年XX岁数

age = int(input('input age'))  # 因为要跟数值进行比较,所以我们这里强转
name = input('input name')

if age > 18 and name:
    print('{}今年{}岁'.format(name, age))
else:
    print('input error, out')

# 嵌套的if


# 随机数模块:random
# 需要导入模块. import关键字 (默认会从本地,根目录中导入,所以尽量不要出现与模块重名的文件)
# random模块中的函数randint(a, b) 返回一个[a,b]的随机整数

'''
财大小游戏

步骤:
1. 生成一个随机数, 利用random模块
2. 键盘输入一个数字
3. 比较
4. 猜对了就结束
5. 猜错了就告诉其大了, 还是下了
'''
import random

randNum = random.randint(1, 10)
num = int(input('please input a number, keep with a randInt'))
print(randNum)
while 1:

    if num == randNum:
        print('恭喜, 猜对了')
        break
    elif num > randNum:
        print('大了')
    elif num < randNum:
        print('小了')
    num = int(input('please input a number, keep with a randInt'))


'''
级联的if else语句
需要注意的是, 别的语言是else if, 而python中是elif

例: 百分之转换五分制:
'''

score = int(input('请输入得分'))
result = 0
if score >= 90:
    result = 'A'
elif 80 <= score <= 90:
    result = 'B'
elif 70 <= score <= 80:
    result = 'C'
elif 60 <= score <= 70:
    result = 'D'
elif 60 >= score >= 0:
    result = 'E'
else:
    print('请重新输入')

print('五分制结果:', result)