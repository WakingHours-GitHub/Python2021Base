# 介绍几种排序算法
from _typeshed import StrPath
from hashlib import new
import random

i = 0
ran_list = []
while i < 20:
    ran = random.randint(1,100) # 生成随机数
    if ran not in ran_list:
        ran_list.append(ran) # 若不存在则添加
        i += 1
print(ran_list)

# 直接用系统函数
new_list = sorted(ran_list) # sorted不改变本列表，但只是返回排好序的列表
print('new_list = {}\nran_list = {}'.format(new_list, ran_list))

# 排序算法1：直接排序
for i in range(len(ran_list)):
    for j in range(i+1, len(ran_list)): # 从i+1开始，到最后
        if ran_list[i] > ran_list[j]: # 当前i和j对比，若i(前)和j(后)
            ran_list[i], ran_list[j] = ran_list[j], ran_list[i]
print('->',ran_list)
# 同理,如果想要降序排列, 则把if条件>换成<


i = 0
ran_list = []
while i < 20:
    ran = random.randint(1,100) # 生成随机数
    if ran not in ran_list:
        ran_list.append(ran) # 若不存在则添加
        i += 1
print(ran_list)

# 算法2: 冒泡排序
for i in range(len(ran_list)-1): # n-1次
    for j in range(0,len(ran_list)-i-1): # 每次不要算最后一个-i个，因为已经是最小，次小了。。。
        if ran_list[i] < ran_list[j]:
            ran_list[i], ran_list[j] = ran_list[j], ran_list[i]
print(ran_list)

# 补充：
# 如何算出代码运行的时间
import time # 导入时间模块
# time.time() 返回
start = time.time() # 时间戳,保存代码开始的时间
# 需要测量时间的代码
end = time.time() # 获取代码结束后的时间
cha = end - start # 作差就是代码运行的时间
