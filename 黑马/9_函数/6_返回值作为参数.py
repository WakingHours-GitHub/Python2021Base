"""
在一些场景当中, 返回值可以作为参数传递. 以简化代码

函数的返回值(细节部分):






"""

def test1():
    return 50

def test2(num):
    print(num)

test2(test1()) # 将test1的返回值作为参数传入到test2


# return -> 函数的返回值.

# 多个return的写法:
def return_num():
    return 1
    return 2 # 不执行
"""
    函数执行到return就结束, 弹栈, 返回调用处,
    因此多个return顺序执行, 只执行第一个.  
"""

result = return_num()
print(result) # 1


# 函数多个返回值
def return_num2():
    # 一个return多个返回值, 写法: 数据, 数据
    # 用','分割的数据.
    # 可以返回引用, 可以返回列表, 元组, 字典, 集合, 以及多个值
    return 1, 2


result = return_num2()
print(result) # (1, 2)
# 居然返回了一个元组,
# 因此, 当一个return返回多个数据时, 使用一个变量会自动封箱, 返回一个元组


# return其他数据类型
def return_other_type():
    # return (20, 10)
    # return [10, 20]
    return {'name': 'python'}

# a,b = return_other_type()

print(return_other_type())

