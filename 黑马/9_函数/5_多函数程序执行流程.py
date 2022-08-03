"""
一般实际开发过程中, 一个函数往往由多个函数组成(一个类), 并且多个函数共享某些数据



"""

# 声明一个全局变量
glo_num = 0


# 修改全局变量
def test1():
    global glo_num
    # 修改
    glo_num = 100


# 打印全局变量
def test2():
    # 打印全局变量, 没有找到局部变量
    # 然后找全局变量, 满足就近原则
    print(glo_num)


print(glo_num)  # 0

# 调用函数,
test1()  # 执行test1, 修改glo_num

test2()  # 100

print(glo_num)  # 100
