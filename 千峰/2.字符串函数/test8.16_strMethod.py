# 字符串函数
# 字符串的内建函数： 声明一个一个字符串， 默认可以调用内建函数（即：系统标准库里面的函数）

# 第一部分，大小写格式相关：
'''
capitalize(): 将字符串第一个单词大写

title(): 将字符串每个首字母大写, 返回title格式

istitle(): 判断是否为title格式（即: 是否首字母大写)

upper(): 将字符串全部转换成大写字母

isupper(): 判断字符串是否全为大写

lower(): 将字符串全部转换为小写字母

islower(): 判断字符串是否全是小写字母


'''
message = 'python is a program language'

msg = message.capitalize() # 开头第一个字母大写
print(msg) # Python is a program language

msg = message.title() # 返回title格式字符串（首字母大写）
print(msg) # ython Is A Program Language

istitle = message.istitle() # 判断是否为title格式
print(istitle)

istitle = msg.istitle()
print(istitle)

msg = message.upper() # 将所有字母转换成大写字母(只有字母转换)
print(msg)

msg = message.lower() # 将所有小写字母转换成小写字母
print(msg)

# 应用场景：
# 案例： 验证码案例

s = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm0987654321'
print(len(s)) # 输出字符串长度

# 如何抽取四个随机字母
# 既然是随机我们就要用到random模块
import random

code = ''

for i in range(4):
   code += s[random.randint(0, len(s) - 1)] # 获取随机数，(randint()函数是两边都包含的，[])

print('验证码：{}'.format(code)) # 每次都是随机的


# 用户输入验证码， 验证码匹配
# 不过用户输入完验证码，一般都是两边进行统一的，也就是两边都不区分大小写来进行对比
# 所以最好的办法就是同时转换为小写，进行比较
user_code = input('请输入验证码')
if user_code.lower() == code.lower():
    print("验证码正确")
else:
    print('验证码错误')