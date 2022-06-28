"""
    1. 产生10个1~20的随机数，去除里面的重复项
    2. 键盘输入一个元素，将此元素从不重复的集合中删除
"""
import random
import time

list_rand = list()
# 产生随机数
for i in range(10):
    list_rand.append(random.randint(1,20)) 

set1 = set(list_rand) # 强转成set直接去重
set1.update(list_rand) # 更新到set1中

print(set1)

# 下一个案例：
# 键盘输入一个数字, 在集合中删除该数字
# num = int(input('请输入一个数字'))
# set1.discard(num) # 删除
# print(set1)

# 方法2: 直接set.add: 但是仍然不能生成10个
set1 = set()

for i in range(10):
    set1.add(random.randint(1,20)) # 直接添加到集合中
print(set1)

# 我自己的改进方式:
start = time.time() # 获取`当前时间
set1 = set()

while len(set1) < 10: # len(set1) = 10 跳出
    set1.add(random.randint(1,20))
print(set1)

end = time.time() # 计算时间戳

# 补充: 第三种格式打印字符串的方式:
print(f"len:{len(set1)}\n程序所用的时间:{(end - start)}")

print('----'*50) # 分割


# 其他操作：符号操作
# in, not in, ==, != , is, not is
set2 = {2,3,4,5,6,7,8,9}
set3 = {3,4,5,6,7,8,9,10}

print(set2 == set3) # False
# 判断两个集中的内容是否相等
print(set2 != set3) # True
# 判断两个集合中的内容是否相等

# (+ *不支持), 但是支持 - & | ^ 运算符
# 那么- & | ^ 运算符都是什么意思呢
# set4 = set2 + set3 # 不支持 + 运算符
# print(set4)

# set5 = set2 * 2 # 倍数?, 算了吧根本不可用, 报错
# print(set5)

# - 差集 difference() 不同, 差集
# - 和 difference() 一样, 一个是运算符, 一个是函数
set4 = set2 - set3
print(set4) # {2}
# - 差集的作用是set2-set3排除所有相同的元素, 即排除s2中所有s3的元素
set4 = set2.difference(set3)
print(set4)

# & 交集 intersection() 十字路口, 交叉, 相交
# 取交集, 也就是取两个集合共同的元素
set6 = set3 & set2
print(set6) # {3, 4, 5, 6, 7, 8, 9}

set7 = set3.intersection(set2) # 函数的效果和运算符效果相同
print(set7) # {3, 4, 5, 6, 7, 8, 9}

# | 并集 union() 联合
# | 并集, 也就是两个集合中的所有元素
set8 = set3 | set2
print(set8) # {2, 3, 4, 5, 6, 7, 8, 9, 10}

set9 = set3.union(set2)
print(set9)

# ^ 对称差集: symmetric_difference()
# 找两个集合不一样的元素
set10 = set3 ^ set2
print(set10) # {2, 10} # 只有{2, 10}是不同的元素

set11 = set3.symmetric_difference(set2)
print(set11)

'''
什么时候用到集合:
就是表示关系运算的时候,要用到集合

'''


"""
案例
已知两个列表
l1 = [5,1,2,9,0,3]
l2 = [7,2,5,7,9]

找出两个列表的不同元素
找出两个列表的共同元素
"""
l1 = [5,1,2,9,0,3]
l2 = [7,2,5,7,9]

# 首先我们一定要明确, 只有集合才能做关系(- & |)运算

s1 = set(l1)
s2 = set(l2)
# 找出两个列表不同的元素
setDiff = s1 ^ s2 # 对称差集, 直接找到不同的元素
print(setDiff)  # {0, 1, 3, 7} 
# 或者用其他方法, 两个集合的并集,和两个集合的交集求差集
setDiff = (s1 | s2) - (s1 & s2)
print(setDiff) # {0, 1, 3, 7}


# 找出两个列表共同的元素
# 直接用交集嘛就好了
sameDiff = s1 & s2
print(sameDiff) # {9, 2, 5}





