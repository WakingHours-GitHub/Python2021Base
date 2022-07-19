"""
需求: 8位老师, 3个办公室, 将8位老师随机分配搭配3个办公室

步骤:
    1. 准备数据:
        8 老师 -> 列表
        3 办公室 -> 列表嵌套.
    2. 分配老师到办公室
        随机分配 -> random模块
    3. 验证是否分配成功
        打印办公室
"""
import gc
import random
teachers = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
offices = [[], [], []]

# 随机分配:
for teacher in teachers:
    offices[random.randint(0, 2)].append(teacher)


for i in range(3):
    print(f"第{i+1}个办公室, 有{len(offices[i])}人, 成员如下: ")
    for teacher in offices[i]:
        print(teacher)
gc.collect()
print(offices)
