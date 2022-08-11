"""


测试:
r+和w+区别
文件指针对数据读取的影响.

seek(): 移动文件指针.
    seek(offset: int, whence: int = 0) -> int:
    file.seek(偏移量, 起始位置)
    偏移量: 字符, 或者字节 数.
    起始位置:
        0: 文件开头
        1: 当前位置
        2: 文件结尾.

"""

# r+: 可读可写, 文件指针在开头, 但是当找不到文件时会报错, 不会自动创建
f = open('text.txt', 'r+') # r+: 可读可写, 没有文件则报错.

print(f.read())

f.close()

# w+: 可读可写, 文件指针在开头, 不过会用新内容覆盖原内容. 会清空文件.
# 不过当找不到文件时, 会自动创建该文件.
f = open('text.txt', 'w+')

# 没有调用write(), 因此文件是空的
print(f.read()) # 空

f.close()


# a+: 可读,可写. 没有文件也会新建文件.
# 文件指针在结尾, 因此无法读取数据
#
f = open('text.txt', 'a+')
print(f.read()) # 空
print(f.read())

f.close()


"""
seek函数: 改变文件指针. 
"""

# 测试seek函数
# 测试:
# r模式, 改变文件指针位置, 移到结尾, 不能读取文件
f = open('1.txt', 'r+')
# 改变文件指针:
# f.seek(2, 0) # 从开头, 偏移2个字符开始读取.
#
# aaa
# bbbbb
# ccccc
# ddddd
# eeeee

f.seek(0, 2) # 放到结尾
# 空

print(f.read())

f.close()



# a: 改变文件指针位置, 做到可以读取数据
f = open('1.txt', 'a+')

f.seek(0, 0)
print(f.read())
# aaaaa
# bbbbb
# ccccc
# ddddd
# eeeee

f.close()
