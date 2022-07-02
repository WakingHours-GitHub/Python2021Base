"""
为什么要转换数据类型?
input()接收得到的都是字符串类型的数据. 输入1, 转换为整形1, 如何做到?
转换数据类型的函数:
        函数              说明
    int(x, [base])      将x转换为一个整数       *
    float(x)            将x转换为一个浮点数      *
    complex(teal, [, image] 创建一个复数, real为实部, imag为虚部
    str(x)              将对象x转换为字符串      *
    repr(x)             将对象x转换为表达式字符串
    eval(str)           用来计算字符串中的有效python表达式, 并返回一个对象       *
    tuple(s)            将序列s转换为元组       *
    list(s)             将序列s转换为列表       *
    chr(x)              将一个整数转换为一个unicode字符
    ord(x)              将一个字符转换为他的ASCII整数值
    hex(x)              将一个整数转换为一个十六进制字符串
    octx(x)             将一个整数转换为一个八进制字符串


"""

# input进行接收.
num = input("请输入num数字: ")
print(num)
print(type(num))  # <class 'str'>
# input接收console中, 都是以字符串形式进行接收的.

# 使用int进行转换, 改变数据类型.
# 注意, 使用int()进行转换时, 一定要确保要转换的字符串只存在数字字符, 不存在字母以及其他字符.
print(type(int(num)))  # <class 'int'>

float_num = input("please a float figure: ")
print(float_num)  # 1.1
print(type(float_num))  # <class 'str'>

# 字符串转换为浮点型:
print(type(float(float_num)))  # <class 'float'>
print(float(float_num))

# 将整形转换为浮点型.
num1 = 10
print(float(num1))  # 10.0
# .0就表示为浮点型了.


# str(): 将数据转换为字符串类型
num1 = 10
num2 = 10.8
print(str(num1)) # 10
print(str(num2)) # 10.8
# 这就都转换为字符串类型了.
print(type(str(num2))) # <class 'str'>

# tuple() -> 将一个有序序列转换为元组
list1 = [1, 2, 3]
print(tuple(list1)) # (1, 2, 3)


# list() 将一个序列转换为列表
tuple1 = (1, 2, 3)
print(list(tuple1))

# eval() 计算括号内的表达式, 返回结果
# 计算在字符串中的有效python表达式, 并且返回一个对象
# 就是执行()中的字符串, 返回结果为一个对象
# 或者你也可以这样理解, eval()就是将数据转换为自己原本的类型的数据
str1 = '1'
str2 = '1.1'
str3 = '(1, 2 ,3)'
str4 = '[1, 2, 3]'
print(type(eval(str1))) # <class 'int'>
print(type(eval(str2)))
print(type(eval(str3)))
print(type(eval(str4)))



# 或者你也可以使用eval()执行一些python表达式
# 也就是将字符串当作python语句给解释器进行执行.
print(eval("1+2+1.2")) # 4.2


"""
Python console:
pycharm的交互式开发环境.
自动load默认的解释器
用于短时间验证一点什么什么东西. 
用于测试一些简单的代码片段, 这才使用python console
临时存储在内存中, 开发大型项目时仍然要使用传统的py脚本.




"""
