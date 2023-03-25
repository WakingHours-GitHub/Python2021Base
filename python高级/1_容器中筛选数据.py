"""
python三种数据结构: 序列类型、散列类型与数值类型

容器类型:
序列：列表、元素、字符串、二进制序列。
散列: 集合、字典
数值：整数、浮点型、布尔、负数、字符。

"""


# 案例1：
# 根据条件筛选容器类型中的元素:
def instance_1():
    list_data = [1, 5, -7, -3, 0, -2, 6]
    res = []

    for i in list_data:
        if i >= 0:
            res.append(i)
    print(res)

    # 优化点1: 使用filter函数进行筛选。
    # lambda返回True和False.
    res = filter(lambda x: x >= 0, list_data) # 返回filter对象。
    res = list(res) # 需要强转.
    print(res) # 1.19us


    # 列表解析:
    res = [x for x in list_data if x >= 0] # 列表解析
    print(res) # 551ns, 所以是列表解析更快.

    # 通过timeit包进行测试, 在ipython中进行测试.
    # timeit 表达式. 就可以将这里面的表达式进行测试.
    # timeit [x for x in list_data if x>=0]


# 案例2:
# 在字典中筛选学生成绩大于等于90的学生.
def instance_2():
    from random import randint
    dict_data = {f'stu_{x}':randint(60, 100) for x in range(1, 21)}
    print(dict_data)

    # 使用字典推导式:
    res = {(k, v) for k, v in dict_data.items() if v >= 90}
    print(res)


# 根据条件筛选集合中的元素
def instance_3():
    from random import randint
    set_data = {randint(-10, 10) for _ in range(10)} # 通过集合推导式生成一个集合. 集合和字典都是使用{}, 却比在于是否是键值对形式
    print(set_data) # 集合不允许重复. 所以少于10是正常的.

    # 筛选能被3整除的元素:
    res = {x for x in set_data if x % 3 == 0}
    print(res)




if __name__ == '__main__':
    # instance_1()
    # instance_2()
    instance_3()
