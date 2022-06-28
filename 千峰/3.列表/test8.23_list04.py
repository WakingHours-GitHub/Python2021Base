# 字符串切片操作
'''
s = 'abcdefg'  s[2:5] -> cde (对字符串进行截取操作)
同样切片操作对列表来说也是也同理:
list[start: end: step]
默认从左到右开始, 步长为1
'''
# 除此之外, 列表可以存放不同类型的元素,但是我们一般不会如此操作
list1 = ['杨超越','热巴','佟丽娅','杨幂','赵丽颖','刘亦菲','黑嘉嘉',100,99.9]
print(list1) # 打印整个列表

print(list1[3]) # 通过index取出元素

print(list1[3:6]) # 将截取的结果保存在另一个列表中
# 不过仍然是包前不包后[start,end)

print('-'*40) # 分隔

print(list1[::-1]) # 逆序输出 

# 同样也包含负索引, 是从右到左的反向, 从-1开始
print(list1[-3:-1]) # -3到-2

print(list1[::2]) # 步长为2, 即每隔1个截取

print(list1[-5:-1:2]) # 从左到右,间隔1,-5到-2

print('-' * 40)

# 当step = 负数时候,方向从右到左
print(list1[-1::-1]) # 从左到右, -1到结尾全部取出

print(list1[-1::-2])


# 总结以下系统内置函数
'''
str(): 强转成str类型
int(): 强转成int类型
list():强转成list(符合类型)
len(): 求列表或者str的长度
sorted(obj,reverse=): 升序排序

enumerste(): 函数用于将一个可迭代(可以用for遍历)的数据对象(如列, 元组或字符串)组合为一个索引序列,一般用在for中
enumerate: 枚举;举例


'''

# 交换两个数:
num1 = 10
num2 = 20

# 常规算法:
temp = num1
num1 = num2
num2 = temp

# py中的快速交换
num1, num2 = num1, num2
print(num1, num2)














