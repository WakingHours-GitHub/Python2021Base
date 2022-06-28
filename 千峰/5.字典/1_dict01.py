'''
字典:
1. 符号: {}
2. 关键字: dict
3. 保存的元素是键值对: key:value

定义: dict = {} # 元素必须是一对一对的, 不能单独出现

列表, 元组, 字典的区别:
列表    元组    字典
[]      ()      {}
list    tuple   dict
ele     ele     key:value # 一对,绑定在一起

# 列表和元组都是一个一个元素添加的
# 而字典的添加则是以一个键值对为单位来添加的
# 这有点像java中的map的概念

[].append() # 列表是一个元素一个元素加入
而字典是一对一对添加的
element: 元素

'''
# 字典(dictionary) 部分
# 定义

dict1 = {} # 空字典(更常用)
dict1 = dict() # 这个也可以返回一个空字典
# 只是这种方式并不常用
# list1 = list() 空列表, tuplu1 = tuple() 空元组
print(id(dict1)) # 分配成功

# 创教一个非空字典, 其元素必须是一对一对放入的
# dict = {key:value, ...} # 对列表进行初始化
dict3 = {'ID': '9384403','name':'lucky','age':18}
# 每一个元素都是键值对: enptyKey

# dict4 = dict(('name','lucky')) # {'name': xxx, 'lucky': xxx}
# ValueError: dictionary update sequence element #0 has length 4; 2 is required
# print(dict4) # 它默认会把()里面的都认为是key, 此时就没有value与之对应了, 此时就会报错

# 所以我们强转的时候, 列表或者元组必须一对一对放, 所以[(), (), ...] . ((), (), ...)
# 正确的方式:
temp = [(1,2),(3,4),(5,6),(7,8)]
dict1 = dict(temp)
print(dict1) # {1: 2, 3: 4, 5: 6, 7: 8}
# 字典的增删改查:
# 增加:
# 格式：dict6[key] = value
# 特点: 按照上面的格式,如果在字典中存在同样的key,则发生替换
#       若没有同名的key，则是添加到字典中
dict6 = {} # 定义空字典
dict6['brand'] = 'huawei' # 添加键值对: brand: huawei
print(dict6) # {'brand': 'huawei'}

dict6['brand'] = 'mi' # 当dict6中的key存在时: 则发生替换
print(dict6) # {'brand': 'mi'}

dict6['type'] = '10'
dict6['price'] = 2000
dict6['color'] = '黑色'

print(dict6) # {'brand': 'mi', 'type': '10', 'price': 2000, 'color': '黑色'}
# 这样就打印出来了dict6字典的内容


















