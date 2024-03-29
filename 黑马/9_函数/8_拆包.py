"""
拆包和交换变量的值.
刚才通过可变参数和可变关键字参数, 我们已经看见了组包,
可变参数组包成为一个tuple, 可变关键字参数组包成为一个dict
组包, 就是将单个数据元素, 组合到一个数据类型当中,
拆包: 就是将一个数据类型对象, 拆为单个元素

拆包分: 元组 和 字典

交换变量的值:
    交换变量的值有多种方法:
    方法1: 结束第三个变量存储数据.
    方法2: 异或
    方法3: python的语法糖: a,b = b,a 这是同时进行的.



"""

# 拆包元组数据
import gc


def return_num():
    return 100, 100

result = return_num()
print(result) # (100, 100)

num1, num2 = return_num() # 元组自动拆包.
print(num1, num2) # 100 100

# num1, num2, num3 = return_num() # 报凑
# 可见, 当元组拆包时, 一定要和对应元素对应

# 字典拆包
dict1 = {'name':'tom', 'age':18}

a, b = dict1

# 对字典单独拆包, 赋予变量时, 取出来的就是key
print(a) # name
print(b) # age

print(dict1[a]) # tom
print(dict1[b]) # 18

def test_kwargs(**kwargs):
    print(kwargs)

# 字典作为可变关键字参数传入函数:
test_kwargs(**dict1) # {'name': 'tom', 'age': 18}
# **就表示手动拆包, 为kay=value的形式, 然后传给**kwargs, 也就是可变关键字参数


# 交换变量
a = 10
b = 20

# 方法1:
c = a
a = b
b = c
print(a, b) # 20 10 # 可见, 数据已经转化了.

del c

gc.collect()


a, b = 10, 20 # 个数需要相同
a, b = b, a # py特有的交换便令的方式
print(a, b) # 20 10 #







