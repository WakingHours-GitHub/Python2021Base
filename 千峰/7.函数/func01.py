"""
定义函数: 产生随机数

# 自动格式化: alt + ctrl + shift + l (PyCharm))
# 格式化： PEP8编码规范


"""

# 编写我们的第一个函数
# 随机产生10个随机数并且打印出来
import random

# 定义函数: def 关键字
def generate_random():
    for i in range(10):
        ran = random.randint(1,20)
        print(ran)

# 看看函数是什么样的
print(generate_random) # <function generate_random at 地址 >
# 打印出来是表明这是一个函数, 在内存中的地址

"""
那么在python中是如何做的呢
首先python的解释器会一行一行执行你的代码
当看到了def时, py知道你声明了一个函数, 于是python就加载函数到内存堆栈区了
当打印函数名时候, print就会打印这个属性, 也就是 function 函数名 at 地址
所以, 函数是有地址的, 在内存中存放
而() 表示调用, 函数名() 表示调用函数, 那么程序就会自动进入函数中去执行
也就是进入函数的入口地址

"""
# 调用: 函数名()  找到函数的入口地址, 并且执行函数体的内容
# () 确保了这是一个函数, 而不是一个变量, ()有调用的意思
# 只有打印函数名,才能告诉你这是一个函数, 以及他的入口地址 加上() 就是调用
print('-'*100)
generate_random()  # 打印十个随机数

# 调用函数的底层原理
# 函数名()
# 就是找到函数对因入口地址, 开始执行
