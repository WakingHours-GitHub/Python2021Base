"""
字典推导式的作用: 快速合并列表为字典或者提取字典中目标数据
字典推导式: 显然语法:
    {表达式: 表达式 for 元素 in 可迭代对象 if 条件表达式}
















"""

# 创建一个字典: 字典key是1-5数字, value是该数字的2次方
# 使用字典推导式.
dict1 = {i: i**2 for i in range(1, 6)}
print(dict1) # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


# 将两个列表合并为一个字典
list1 = ['name', 'age', 'gender']
list2 = ['tom', 20, 'man']


dict1 = {list1[i]: list2[i] for i in range(len(list1))}
print(dict1)

# 使用zip()方法, 前提要保证可迭代对象长度相同. 返回一个[()...]
dict1 = {key: value for key, value in zip(list1, list2)}
print(dict1)

# 提取字典中的目标数据, 使用if过滤数据, 返回满足if的数据.
counts = {'MBP':268, 'HP': 125, 'DELL':201, 'Lenovo':199,'acer':99}
counts1 = {key: value for key, value in counts.items() if value >= 200}
print(counts1) # {'MBP': 268, 'DELL': 201}






