'''
循环部分经典题目：打印三角形
设
*
**
***
****
......

分析：
第一层1颗星
第二层2颗星
...
星数取决于层数


'''

n = 5  # 行数（层数）
for i in range(n):
    for j in range(i + 1):  # 打印*
        print('*', end='')
    print()

print('-' * 20)

# 简便写法：
for i in range(n):
    print('*' * (i + 1))  # py特有

'''
九九乘法表
1*1 = 1
1*2 = 2 2*2=2
...
1*9 = 9 2*9 = 18 ...
'''

for i in range(1, 10):
    for j in range(1, i + 1):
        print('{}*{} = {}  '.format(j, i, j * i), end='')  # 一层的内容，不要换行

    print()  # 一层之后的内容，可以换行

'''
综合案例：
抛筛子

1. 欢迎XXX进入游戏
2. 输入用户名， 默认用户没有币
3. 提示用户充值(100rnm 30币, 充值必须为100的倍数, 充值不成功可以再次充值)
4. 玩一局勾除2个币（猜大小， 随机数模拟骰子的数值）
5. 只要猜对了奖励1一个币，可以继续玩（没币自动退出， 金额不足的时候提醒， 也可以自己退出）


'''

import random

print('#' * 28)
print('#' * 5, '欢迎进入抛筛子游戏', '#' * 5)
print('#' * 28)

username = input('please input user name:')
money = 0  # 初始金币为0

while input('确定要进入游戏吗（y/n)?:') == 'y':
    print('欢迎 [{}] 进入游戏!!!'.format(username))
    while money < 2:
        print('游戏币100元30个, 且只接受100的倍数')
        temp = int(input('当前金币不足， 请充值:'))
        if temp % 100 == 0 and temp > 0:
            money = (temp // 100) * 30
            print('充值成功, 当前', str(money), '个币')

    judge = input('当前金币数：{}。 是否选择进入游戏（y/n):'.format(money))
    if judge == 'y':
        while True:  # 开始游戏
            money -= 2  # 只要进入游戏就扣除金币
            t1 = random.randint(1, 6)
            t2 = random.randint(1, 6)
            guess = input('随机完成,请输入您猜的大小')
            if (guess == '大' and t1 + t2 > 6) or (guess == '小' and t1 + t2 <= 6):
                print('猜对了, 赠送一个游戏币')
                money += 1
            else:  # 猜错了的情况
                print('猜错了')

            if input('游戏结束，当前金币剩余：{}。 还需要继续玩吗(y/n)?'.format(money)) == 'y':
                if money < 2:
                    temp = input('当前金币不足, 请充值')
                    money = (temp // 100) * 30

            else:
                print('退出游戏')
                break

'''
以前的练习题：

1. 0010 1000 的十进制：40
print(bin(40))


'''

# 2.:
a, b = 2, 4
print(b)  # b = 4
b = c = 5
print(a, b, c, sep='#')  # 2,5,5

print(c - a > b - a)  # False

a += 3

result = a + b
print(result)

# 3.if判断
t = int(input('please input temperature '))
if t > 30:
    print('today so hot')
else:
    print('temperature is good')

# 4.3 布尔表达式：
# p and not q = not ( p and q)

# 5. while循环输出1~50的偶数

i = 1
result = 0
while i <= 50:
    if i % 2 == 0:
        print(i, end=' ')
        result += i

    i += 1

print('\n', result)

'''
复习补充:
for循环也可以实现累加和

'''
sum = 0
for i in range(1, 51):  # 包前不包后
    forin = i
    if i % 2 == 0:
        sum += i

print(sum, i) # 650 50
print(forin) # 50
'''
注意之类变量的作用域: i和,forin是for里面声明的,但是在for外面仍然可以打印出来
这是py与其他语言不一样的地方
py没有作用域一说, 在代码块缩进外面, 都可以获取变量

'''

'''
跳转语句:
break, continue
pass

pass: 缩进占位，使其没有语法错误
continue: 跳过循环体语句, 直接开始下一次的循环
break: 跳出循环

'''

result = 0
for i in range(10):
    if i % 3 != 0:
        result += i
print(result)

result = 0

for i in range(10):
    if i % 3 == 0:
        continue # 跳过后面的部分
    result += i
print(result)
