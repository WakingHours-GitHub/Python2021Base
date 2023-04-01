# 让字典保持有序。
# 当前所讲授的知识点基于python2版字典的特性.
# 在python3.5之后的版本中, 字典数据类型为有序. 会根据当前输入的顺序进行排序.
# 可以作为拓展内容.

# 使用OrderedDict, 这个orderedDict在很多框架中都有实现.
import random
from random import randint
from time import time
from collections import OrderedDict

from typing import *
from functools import reduce


def instance_0() -> None:
    dict_data = OrderedDict()  # 创建有序字典对象. 特性就是根据输入的顺序排序.
    # 在python3.5之后, 直接创建dict()对象. 直接就是有序的.

    player = ['顾安', '扶苏', '安娜', '双双']

    # 创建答题时间对象:
    t_start = time()  # 返回时间帧.
    player_max_index = len(player) - 1

    for i in range(len(player)):
        # 模拟同学的答题过程
        input("随便输入, 以模拟答题过程: ") # 会阻塞当前线程
        t_end = time()
        random_index = random.randint(0, player_max_index - i)
        dict_data[player[random_index]] = t_end - t_start
        player.pop(random_index)


    print(dict_data) # 就是根据顺序来的。但是如果是python2中的dict则随机顺序。




if __name__ == '__main__':
    instance_0()
