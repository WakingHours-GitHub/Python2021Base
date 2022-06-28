# 类型转换 合集
# 强制类型转换
# int() str() int() list() tuple() dict() set()

# str -> int, list, set, tuple
s = '8'
print(s.isdigit()) # 判断s中是否全为数字字符 True
i = int(s) # 使用int将s强转成int的前提是str中必须全由digit组成

s = "abc"
l = list(s)
print(l) # ['a', 'b', 'c'] # 将每个字符单独转换成一个元素

set1 = set(s)
print(set1) # {'b', 'c', 'a'} # 同样也是将每个字符转成单独的一个元素了

t = tuple(s)
print(t) # ('a', 'b', 'c')

# 反过来：str <- int, list, set, tuple, dict, floot

i = 8
s = str(i)
print(s, type(i))

l = str(['a','b','c'])
print(l, type(l))

# 元组,集合,字典,浮点数,都可以转换成str
tuple1 = (1,2,3,4)
s = str(tuple1) # '(1, 2, 3, 4)' <class 'str'>
print(s, type(s))

set1 = {1,2,3,4,5}
s = str(set1)
print(s, type(s)) # '{1, 2, 3, 4, 5}' <class 'str'>

dict1 = {1:"aa", 2:"bb"}
s = str(dict1)
print(s, type(s)) # '{1: 'aa', 2: 'bb'}' <class 'str'>

# 其他数据类型之间的转换
# list -> set() tuple() 同样也可以转换成字典, 前提: 嵌套的,并且是一对一对的
list1 = [1,2,3,4]
tuple1 = tuple(list1)
print(tuple1, type(tuple1))

set1 = set(list1) # 去重
print(set1, type(set1))

# tuple -> list set 
tuple1 = (1,12,3,45)
list1 = list(tuple1)
print(list1, type(list1))

set1 = set(tuple1)
print(set1, type(set1))

# dict -> list 或者 tuple # 不过仅仅是key转换
dict1 = {1:"1", 2:"2"}
list1 = list(dict1)
print(list1, type(list1))

tuple1 = tuple(dict1)
print(tuple1, type(tuple1)) # (1, 2) <class 'tuple'>
# 所以dict -> list or tuple 仅仅是key保存
















