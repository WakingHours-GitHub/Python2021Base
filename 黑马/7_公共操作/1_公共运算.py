"""

公共运算:
运算符:
    运算符   描述            支持的数据类型.
    +       合并          字符串, 列表, 元组
    *       复制          字符串, 列表, 元组
    in      元素是否存在   字符串, 列表, 元组, 字典, 集合
    not in  元素是否不存在  字符串, 列表, 元组, 字典, 集合



"""

# 先初始化变量:
str1 = "aa"
str2 = 'bb'

list1 = [1, 2]
list2 = [10, 20]

t1 = (1, 2)
t2 = (10, 20)

dict1 = {'name': 'tom'}
dict2 = {'age': 30}

# +: 合并
# 字符串:
print(str1 + str2) # aabb
# 可见是将两个字符串拼接起来, 组成一个新的字符串.

# 列表:
print(list1 + list2) #  [1, 2, 10, 20]
# 可见是将两个列表拼接起来了.

print(t1 + t2) #  (1, 2, 10, 20)
# 可见, 两个元组也被拼接起来了


# print(dict1 + dict2) # TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
# 可见, 对于dict类型上, 是会报错

# * 复制
str1 = 'a'
list1 = ['hello']
tuple1 = ('world', ) # 注意, 单个元组需要带',' ,才能表示这是要给元组

# 字符串
print(str1 * 10) # aaaaaaaaaa
print('='*20) #

# 列表:
print(list1 * 5) # ['hello', 'hello', 'hello', 'hello', 'hello']
# 可见复制了列表中的元素, 得到一个新的列表
list2 = ['h', 'b']
print(list2 * 5) # ['h', 'b', 'h', 'b', 'h', 'b', 'h', 'b', 'h', 'b']

# 元组, 也是一样, 和列表相同
print(tuple1 * 3) # ('world', 'world', 'world')

# in 和 not in
print('a' in 'abcd') # True
print('a' not in 'abce') # False

list1 = ['a', 'b', 'c', 'd']
print('a' in list1) # True

# 元组也是一样
print('a' not in ('a', 'b', 'c', 'e')) # False

# 集合也是
set1 = {10, 20 ,3 ,1}
print(3 in set1)  # True

