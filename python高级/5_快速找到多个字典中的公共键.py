# 如何在多个不同的字典中找到快速的公共键

import random
from random import randint, sample


# sample:
def sample_using() -> None:
    name_list = ["国安", "复苏", "安娜", "离谱"]
    res = sample(name_list, 3)  # sample就是在容器中随机选取三个.
    print(res)


def instance_0() -> None:
    # 生成字典, 构建一个数据结构:
    name_list = ["国安", "复苏", "安娜", "离谱"]

    # 生成字典, 构建三次抽奖结果.
    dict_data_1 = {x: randint(10, 50) for x in random.sample(name_list, 3)}
    dict_data_2 = {x: randint(10, 50) for x in random.sample(name_list, 3)}
    dict_data_3 = {x: randint(10, 50) for x in random.sample(name_list, 3)}
    print(dict_data_1, dict_data_2, dict_data_3)

    res = []  # 存储三次中奖的同学.
    for k in dict_data_1:  # 循环key
        if k in dict_data_2 and k in dict_data_3:
            res.append(k)
    print(res)  # 这样就找到了三轮都中奖的人.


# 第二种方式: 可以利用集合数据类型交集特性完成功能.
def instance_1() -> None:
    name_list = ["国安", "复苏", "安娜", "离谱"]

    # 拿到三个字典中的key.
    # dict.keys() -> 类似set的容器. a set-like object.
    # ipython: dict.keys?
    dict_data_1 = {x: randint(10, 50) for x in random.sample(name_list, 3)}
    dict_data_2 = {x: randint(10, 50) for x in random.sample(name_list, 3)}
    dict_data_3 = {x: randint(10, 50) for x in random.sample(name_list, 3)}

    res = dict_data_1.keys() & dict_data_2.keys() & dict_data_3.keys()  # 取交集.
    print(res)

    # 有一个缺点: 也就是需要知道有多少个字典. 有多少个就要写多少个.


# 使用map
def instance_2() -> None:
    name_list = ["国安", "复苏", "安娜", "离谱"]

    dict_data_1 = {x: randint(10, 50) for x in random.sample(name_list, 3)}
    dict_data_2 = {x: randint(10, 50) for x in random.sample(name_list, 3)}
    dict_data_3 = {x: randint(10, 50) for x in random.sample(name_list, 3)}
    print(dict_data_1, dict_data_2, dict_data_3)

    # 使用map和reduce函数. map(函数引用, sequence)
    map_data = map(dict.keys, [dict_data_1, dict_data_2, dict_data_3])
    print(map_data)  # map对象. 其实就是对sequence中的每个元素进函数引用的调用.

    from  functools import reduce # 导入reduce函数.
    res = reduce(lambda a, b : a & b, map_data) # 将这几个进行reduce. 这是一种具体化的操作.
    print(res)


if __name__ == '__main__':
    # sample_using()
    # instance_0()
    # instance_1()
    instance_2()