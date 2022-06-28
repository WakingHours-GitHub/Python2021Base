# while循环 
"""
while循环

while 表达式: # 表达式为true时, 执行循环体
    循环体

while中一定要有改变循环变量的部分


"""
'''
死循环: while True
1. 循环体内部没有改变循环变量的语句(除非有break)
2. 避免表达式一直为True
3. 设计出死循环, 但是可以有break跳出循环
  


'''

print('-' * 30)
i = 0  # 与for不同, for头可以初始化一个循环变量
while i <= 10:
    print(i)
    i += 1

# 例子: 打印1~30之间, 所有3的倍数
# 算法1:
i = 1
while i <= 30:
    if i % 3 == 0:  # 能够整除3
        print(i)
    i += 1

i = 3
# 算法2
while i <= 30:
    print(i)
    i += 3

# 打印100以内, 即使3的倍数又是5的倍数
i = 1
while i <= 100:
    if i % 3 == 0 and i % 5 == 0:
        print(i)
    i += 1

# 因为3,5是小质数
# 所以若整除15,同样也是3,5的倍数

print('-'*30)

'''
练习:
使用while循环算1~20的累加和
累加: 保留上一次计算结果，下一次迭代时用
'''
i = 1
result = 0
while i <= 20: # 到20
    result += i # 累加
    i += 1

print(result)
