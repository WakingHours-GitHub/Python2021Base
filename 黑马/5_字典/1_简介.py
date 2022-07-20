"""
字典的学习：目标:
字典: 一种python自带的数据结构, 使用键值对的方式存储数据, 字典是一种可变数据类型
    字典数据和数据的顺序没有关系, 即字典不支持下标. 需要根据key, 就能找到对应的value.

    字典的应用场景:

    创建字典的语法:
        使用符号为{}, {}内数据以key: value形式出现, 各个键值对之间使用','分割
        dict = {key: value, ...}

    字典常用操作:
        增:
            dict[key] = value,
            如果key存在, 则修改这个key对应的value, 如果key不存在, 则新增该键值对.
            增加key: value值

        删除:
            关键字: del() / del: 删除字典或者删除字典中指定键值对.
            value = dict.pop(key): 根据key删除该键值对, 并且返回value
            (key,value) = dict.popitem(): 删除dict中最后的一个键值对, 返回key和value组成的元组.
            dict.clear(): 清空字典.



        修改:
            dict[key] = value
            key存在, 则修改该key对应的value, 如果key不存在则新增此键值对.

        查找:
            按照key值查找, 以及使用函数方式进行查找
            key值查找:
            dict[key] # 返回字典中key对应的value
            注意: 如果key存在, 则返回对应的value, 如果key不存在, 则会报错.

            value = dict.get(key, 默认值):
                如果key存在, 返回对应的value. 如果当前查找的key不存在, 则返回默认值, 如果省略第二个参数, 则默认为None

            dict.keys() # 返回所有key组成的dict_keys对象, 也是一个可迭代对象, 可以使用list, tuple进行强转
                也可以使用for进行遍历

            dict.values() # 返回value足证的dict_value对象. 返回一个包含所有value的可迭代对象

            dict.items() # 返回[(key, value), ...]的可迭代dict_items对象.







    字典的循环遍历:
        遍历字典的key

        遍历字典的value

        遍历字典的元素








"""

# 创建字典:
# 直接使用数据创建字典:
import gc

dict1 = {'name': 'tom', 'age': 20, 'gender': '男'}
print(dict1)  # {'name': 'tom', 'age': 20, 'gender': '男'}
print(type(dict1))  # <class 'dict'> # 为字典类型

# 创建空字典
dict2 = {}
print(type(dict2))

dict3 = dict()  # 使用字典对象创建空字典
print(type(dict3))

# 给字典新增数据.
dict1['id'] = 100
print(dict1)  # 新增了: id: 100

dict1['name'] = 'rose'
print(dict1)
# 如果key存在, 是修改, 如果key不存在才是新增键值对.


# 删除数据
dict1 = {'name': 'tom', 'age': 20, 'gender': '男'}
del dict1['name']
print(dict1)  # {'age': 20, 'gender': '男'} # 删除键值对

# del dict1['names'] # KeyError: 'names' # 报错
# 使用del删除时, 字典是需要通过key来取value的, 如果key不存在, 则会报错.

print(dict1.pop('age'))
print(dict1)

# 删除最后的键值对
print(dict1.popitem())
print(dict1)


dict1.clear()
print(dict1)  # {}

gc.collect()  # 清除垃圾.

# 修改字典
dict1 = {'name': 'tom', 'age': 20, 'gender': '男'}
dict1['name'] = 'rose'  # 使用已经存在的key, 赋值新value就是修改
print(dict1)  # {'name': 'rose', 'age': 20, 'gender': '男'}


# 查找字典中的数据:
# 使用key进行查找
dict1 = {'name': 'tom', 'age': 20, 'gender': '男'}
print(dict1['name']) # tom
# print(dict1['names']) # KeyError: 'names' # 报错.

# 使用函数进行查找
print(dict1.get('name')) # tom # 如果存在返回对应的value
print(dict1.get('names')) # None # 如果不存在, 默认返回None

print(dict1.get("names", 'meiyou')) # meiyou # 找不到key, 返回默认值.

# keys(): 返回只有key组成的dict_keys对象, 也就是返回所有的key的可迭代对象
print(dict1.keys()) # dict_keys(['name', 'age', 'gender'])

# values():
print(dict1.values()) # dict_values(['tom', 20, '男'])

# items(): 返回嵌套组合
print(dict1.items()) # dict_items([('name', 'tom'), ('age', 20), ('gender', '男')])


# 遍历字典
# 遍历字典的key:
dict1 = {'name': 'tom', 'age': 20, 'gender': '男'}
for key in dict1.keys():
    print(key)


# 遍历字典的value
# 打印所有的value
for value in dict1.values():
    print(value)


# 遍历字典中的元素:
for item in dict1.items():
    print(item) # 打印tuple

# 自动拆包: tuple会自动拆包.
# 当有两个变量接收时, 元组会自动拆包.
# 变量, ... = 元组. 会自动拆包.
for key, value in dict1.items():
    print(f"{key} = {value}")










