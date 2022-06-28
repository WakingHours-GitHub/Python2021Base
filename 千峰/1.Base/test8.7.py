'''
总结与复习：
常量 变量
type()查看变量的类型
print(values,...., sepp = '', end = '\n')函数
格式化的输出: 输出字符串
1. 占位符
%s %d %f
print('%s,%d,%f' % (values...)
    类型转换:
    int->str: str()
    str->int: int() 前提: 这个字符串中必须只能有数字

2.format()
print('{} {}...'.format(values...)

input('提示信息')函数: 阻塞式
input()函数输入的最终都是字符串类型
所以若想比较数字，则必须使用强制类型转换


运算符:
算术运算符:
+ - * /
**次幂  // 整除

特殊用法, 字符串也可以用*
例如: print('#'*10) # 输出10个#

赋值运算符:
= += -= *= /=

id()函数
查看指向的地址(address)


'''

# 关系运算符 结果只有两种:True False
# > < >= <= == !=

# 因为input从键盘流读取到的东西都是str, 所以这里必须强转
n1 = int(input('请输入第一个数'))
n2 = int(input('请输入第二个数'))

result = n1 > n2
print('n1>n2?', result) # False

# 那么字符串可以用关系运算符吗
str1 = 'hello'
str2 = 'hello'
result = str1 == str2
print('str1 == str2', result) # True
# ==运算符用于根据字符串中存储的值比较两个字符串

# is 用户对象的比较(地址比较)
# 这里有一类问题
age1 = 8
age2 = 8
print(age1 is age2, id(age1), id(age2))
# 结果:True 140722022651776 140722022651776

# 在命令行中:
'''
    >>> menoy = 200000
    >>> id(menoy)
    2583837895568
    >>> seleary = 200000
    >>> id(seleary)
    2583837895536
    >>> seleary == menoy
    True
    >>> seleary is menoy
    False
    >>>
'''
# ==和is的区别:


# 为什么在源文件中和在命令行敲出的结果不一样,这是一道经典的面试题
'''解释:
Python中有小整数对象池和大整数对象池
小整数对象池:python对于小整数的定义是:[-5, 256]这些整数对象是提前建立好的,不会被垃圾回收


大整数对象池.说明:
终端是每次执行一次, 所以每次的大整数都需要重新创建
而pycharm中,每次运行的代码都是加载到内存属于一个整体.
'''




















