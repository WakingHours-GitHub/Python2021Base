"""
增加元素(key:value)
dict[key] = value -> {key:value} # 添加一对键值对
特点: key 在字典中是唯一的, value值是可以不唯一
一个字典实例: {'name': 'value', 'names': 'aaa'} 
错误实例:{'name':'tom','name':'aaa'}  错误定义, 有重复的key
如果该key在字典中已经存在,则在原有的key中修改对应的value

增加元素对比:(列表与字典对比)
list1 = []
list1.append(element)
list1.extend(list)
list1.insert(index, element)

dict1 = {} # 声明一个空字典
dict1[key] = value

修改:
list[index] = newValue

dict[key] = newValue # 若key在字典中存在, 则修改原本的value值

查询:
列表通过索引去查找
list[index] -> element

字典通过key查询
dict[key] -> element

修改
列表是根据下标(index)做修改, 查询的
字典是用key做添加的, 修改, 查询等 操作的
返回元素值: 字典都是根据key获取value的

"""




list1 = [3, 5, 7, 9]
print(list1[2])  # 7 返回索引处的数值

dict1 = {'1': '张三', '2': '李四', '3': '王五'}
print(dict1['1']) # 根据key去找value

dict2= {'张三':100,'李四':100,'王五':89,'赵柳':99} 
print(dict2['王五'])  # 89 # 通过key
# key和value不限制类型

print('---'*10)
# 尝试遍历字典:
for key in dict2:
    print(key) 
# 仅仅是通过for循环遍历的结果是得到字典的key

for key in dict2:
    print(key,dict2[key])
# 通过key找value这样就可以得到所有的内容了

# 字典里面的函数:
# items()   values()    keys()

# dict.items() # 返回的是: [(key, value), (key, value), ....] # 可迭代对象, 里面的每一个元素是一个元组
# dict.values() # 返回的是所有value的值, 返回一个列表
# dict.keys() # 返回的是所有key的值

# 接下来分别说说
# items() 将字典键值对转换成列表保存的形式了， 列表就可以用for进行迭代了
'''
for i in [(key, value), (key, value), ...]: # i ->（key, value)
    pass 
'''
print(dict2.items()) # dict_items([('张三', 100), ('李四', 100), ('王五', 89), ('赵柳', 99)])
# 既然返回的是一个列表, 其中的元素是元组, 那么元组里面分别就是key和value
for i in dict2.items():
    print(i) # 打印的是列表中的元组元素


# 筛选分数大于90分的人
for i in dict2.items():
    if i[1] > 90:
        print(i)
# 既然是元组, 那么就可以使用自动拆箱
# 另一种写法:
for key, value in dict2.items():
    if value > 90:
        print(key, value)

# values: 取出字典中的所有value, 保存到一个列表中
value_list = dict2.values()
print(value_list)

for i in value_list: # 遍历value_list
    print(i) 

for score in dict2.values():
    print(score)

# 求所有学生考试成绩平均分
totle = sum(dict2.values())
print(totle)

avg = totle/len(dict2.values())
print(avg)


# keys(): 获取字典中的所有key, 返回一个列表(键值对)
names = dict2.keys()
print(names)
# 遍历所有人的名字
for name in names:
    print(name)

'''
综上:
items()是取出键值对列表, 返回一个列表,列表中的元素是各个键值对元组
values() 是取出value, 返回一个列表
keys() 是返回所有的key, 用列表返回
'''
# 判断元素是否在字典中出现过
# in: 也可以用于字典操作
# 用于判断元素是否在字典中的key中出想过, 注意in关键字, 在对字典进行操作时查找的是key
# 8 in dict
print('王五' in dict2) # True

'''
综上:
1. 根据key获取value, 若key在字典中没有存在则报错: keyError
    dict[key] -> value
2. 字典的内置函数:
    get(key) -> value 若字典中没有该key,则返回None, 不会报错
    get(key, default) -> value 如果能够取到值,则返回字典中的值, 若没有找到key则返回default的数值
    很明显, 两个参数的get可以针对特殊的key做不同的返回值, 有更广泛的用处
    
    items() # 返回[(),(),...] 返回一个列表, 列表中的元素是各个键值对元组
    keys() # 返回一个由key组成的列表
    values() # 返回一个由value组成的列表
'''
print(dict2.get('赵飞',-1)) # 返回-1


