"""
在python中, 循环有while和for两种
while是普通循环, for是迭代器循环.
不过最终实现的效果都是一样的.

while语法:
while 条件表达式:
    条件成立时执行的代码

for语法：
for 元素 in 可迭代数据(序列):
    重复执行的代码.
    ...




break和continue
break和continue: 是满足一定条件退出循环的两种不同方式。
break: 终止本层循环, 直3接跳出循环.
continue：直接进行下一次循环, 后面的代码不在执行.

while循环嵌套:
    也就是while循环中包含while. -> 嵌套.
    语法:
    while 条件1:
        while 条件2:
        ...
    外面循环一次, 内部循环一圈.


循环的else介绍:
in python, loop can use whit else
在python中, 循环可以和else配合使用.
else中缩进的代码, 是指只有当循环正常结束后所要执行的代码.



"""

# while循环
# 一般来说, 这种代表循环次数的变量, 我们使用i,j,k这种变量进行命名.
# 起始值, 我们一般都设置为0, 然后循环条件时, 使用<号
# 这是工作中常用的习惯.
import gc

i = 0
while i < 5:
    # 缩进表示while执行代码块
    print(i, "离谱")
    i += 1  # 用于改变控制循环变量.

print("while结束后")

# 累加1-100
# 准备数据, 增量为1, 保存结果, 循环加法, 最后打印结果.
sum = 0  # 累加变量
i = 1  # 计数变量
while i <= 100:
    sum += i  # 累加i~[1, 100]
    i += 1  # 累加1
print(sum)  # 打印结果

# 计算1-100偶数累加和
# 偶数: 可以被2整除. 即, 和2取余为0
# 第一种方法
i = 0
sum = 0
while i <= 100:
    if i % 2 == 0:  # 偶数
        sum += i
    i += 1
print(sum)

# 第二种方法. 使用计数器控制累加.
i = 2
sum = 0
while i <= 100:
    sum += i
    i += 2  # 计数增量设置为2.
print(sum)

# 注意, 一定要有修改循环条件的语句, 否则将会陷入死循环的过程中.


# 了解break和continue作用
i = 1
while i <= 5:

    if i > 3:
        print("吃饱了, 不吃了")
        break
    print(f"吃了{i}个苹果")
    i += 1

i = 0
while i < 5:
    if i == 3:
        print("有虫子")
        i += 1

        continue  # 不执行后面的代码, 直接进行下一次循环. 但是要注意, 需要修改条件.
    print(f"吃了第{i}苹果")
    i += 1

# while循环嵌套
i = j = 0  # 赋予同一值
while i < 3:
    print("刷碗")
    j = 0  # 重置
    while j < 3:
        print("我错了")
        j += 1
    i += 1

gc.collect()  # 强制垃圾回收

# while循环应用: 打印星号
i = j = 0
while i < 5:
    j = 0  # 重置
    while j < 5:  # 一行星星的打印
        print("*", end='')  # 需要修改print结束符, 做到五个星星在一行.
        j += 1
    print()  # 输出换行符.
    i += 1

print()

# while循环应用: 打印三角形
# 分析: 每一行输出的星星个数和行号是相等的.
i = j = 0
while i < 5:
    j = 0
    while j <= i:  # 控制每行打印多少个*. 与i(行)相同, 就是三角形.
        print("*", end='')
        j += 1
    print()
    i += 1

# while循环应用: 九九乘法表
# 打印表达式: x * x = x*x
# 一行打印多个表达式.
i = j = 1
while i <= 9:
    j = 1
    while j <= i:  # 外部循环和内部循环是有关系的.
        print(f"{j}*{i}={i * j}", end='  \t ')  # 对齐
        j += 1
    print()
    i += 1

# for循环体验
# 什么叫可迭代对象(数据序列),
# 简单理解, 就是一个数据对象是由多个更小的子数据所组成的.
# 其中的元素是可以一个一个剥取的. 也就是是由元素, 构成了数据序列
# 例如, 字符串, 列表, 元组, 集合, 字典.
str1 = "itheima"
for i in str1:  #
    print(i)  # 将字符一个一个打印出来.


# break和continue同样可以在for循环中使用.

# 循环配合else使用
# else缩进的代码, 表示循环正常执行后所要执行的代码
# 适用于对while循环进行是否正常执行的判断.
i = 1
while i < 5:
    print("离谱")
    if i == 3:
        break
    i += 1
else:
    print("while_else")
