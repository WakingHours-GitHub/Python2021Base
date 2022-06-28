'''

总结:
字符串中可以使用的符号:
+		拼接
*		倍数,乘以多少个
in		字串是否在字符串中
not in
is		两个字符串的比较(地址)
not is
[]		切片,截取

同样列表也支持上面的一些符号
'''

# + 在list中的使用
l1 = [1,2,3]
l2 = [4,5,6,7]
l3 = l1 + l2; # 表示把l1和l2拼接起来
print(l3)

# 用函数拼接呢?
l3 = l1.extend(l2) # 将l2拼接到l1后面,然后保存在l1中!!
print(l3) # None # 没有返回值!!!
l3 = l1
print(l3)


# * 在list中的应用
l4 = l1*3 # 相当与3个l1
print(l4)

result = 3 in l1 # 3 在 l1中吗
print(result) # True

result = [3] in l1 # [3] 在l1中吗, 此时[3]作为一个整体
print(result) # Flase

result = [3] in [1,2,3, 4, [3, 4], [3]] # 列表中套列表
print(result) # True

'''
列表中可以包含的元素:
整形
字符串类型
浮点型(小数)
列表
元组
字典
对象(自定义类,自定义对象)

# 列表,元组,也是可以相互的嵌套
[[], [], ....]
[(), (), ...] 或 ([], [], []...)
'''

print('-'*30) # 分隔符号
result = [3] in [1, 2, 3, [3], 4] # 3 和 [3]是不同的
print(result) # True

# 列表里面可以嵌套列表, 那么列表中的每一个列表是一个元素
list5 = [[1,2], [1,2,5], [4,0], [7,4,6]]
print(len(list5)) # 4 # 说明每一个列表是一个元素

ele = list5[2] # 取出list5中index=2的元素,其实是一个列表:[4,0]
print(ele, type(ele)) # [4, 0] <class 'list'>

print(ele[1]) # 0

print(list5[1][2]) # 在[1,2,5]取出5

print(range(1, 10, 3)) # range(1, 4, 7) 我们不能直接打印出来返回的数字,因为底层封装是generater
# 但是实际上我们知道是1, 4, 7.我们如何给他转换成我们熟悉的形式呢? 类型转换:list()

"""
类型转换, 强转
str()       强转成为字符串类型
int()       强转成int类型
list()      将可迭代对象转换成列表

print(list(range(1, 10, 3)))
# 这样就可以打印出(1,,4,7)了

同样: 任何可迭代对象,或者说能够放入到for循环里面的,都可以强转成list
s = 'abc'
result = list(s)
print(list(s)) # ['a', 'b', 'c']

iterable: 可迭代的, 就是可以一个一个拆分出元素的, 或者说可以放入到for...in...中
'abcde' -> list('abcde') -> a b c d e
for X in XXX:
    pass

"""
print(list(range(1,10,3))) # [1, 4, 7]

s = 'abc' # 字符串也是一个可迭代对象
print(list(s)) # ['a', 'b', 'c']
# 将单个元素分隔开放入list中

# 我们需要注意这样一点：整形不是可迭代对象
# print(list(10)) # TypeError: 'int' object is not iterable

# print(int([4,5])) # TypeError
print(int('45')) # 45

# 但是可以这样操作
s1 = '0123456789' 
print(int(s1[3:5]) + int(s1[-5:3:-1]) ) 
# 可以截取字符串，然后强制转成int

# 书面上的练习题, 还记得join吗,连接符.join():将可迭代对象拆分,然后用连接符相连
x = "abc"
y = "def"
z = ["d", "e", "f"]
print(x.join(y)) # dabceabcf
print(x.join(z)) # dabceabcf
