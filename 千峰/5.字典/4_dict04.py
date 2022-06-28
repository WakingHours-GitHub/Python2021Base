# 增删改查的删除操作
# 删除操作：
# 回顾列表的删除操作
list1 = [1,7,6,9]
del list1[1] # 使用del关键字, 利用索引, 对列表进行删除操作
print(list1)
# 或者list用pop, remove, index()

# 那么字典如何删除呢
dict1 = {'张三':100,'李四':100,'王五':89,'赵柳':99} 
del dict1['张三'] # 根据key删除键值对
print(dict1)

# del dict1['张三'] # 当key不存在时, 会报错keyError

# 字典的内置函数: 删除操作
# 字典没有remove操作, 但是由pop函数:
# pop(key[,default]) -> 根据key删除字典中的键值对, 若删除成功,则返回key对应的value
# 若没有找到key则返回None, 当default启用时, 没有找到key则返回defualt值

# pop(key[, default]): 删除key对应的键值对, 若没找到则返回None, 有default的情况下, 返回default的值
result = dict1.pop('李四')
print(result) #  返回所删除key的value
print(dict1) #  已经被删除

result = dict1.pop('li', "123") # 字典中没有key的情况下,返回default值
print(result) # 123
print(dict1) # 没有删除, 并且也没有报错, 所以我们最常用的一般就是pop操作

print("##"*20)

# popitem(): 随机删除字典中的键值对(一般都是从末尾删除元素)
dict1 = {'张三':100,'李四':100,'王五':89,'赵柳':99} 

result = dict1.popitem() # 返回删除的键值对
print(result) # ('赵柳', 99)
print(dict1) # 把赵柳删除了
 
# clear() 同列表的clear(): 直接清空所有元素
dict1.clear() 
print(dict1) # {}

'''
综上: 总结:
关键字: del
del dict[key] # 删除key对应的键值对

dict.pop(key[, default]) # 删除指定key的键值对, 若没找到key则返回None, 有default就返回default的值

dict.popitem() # 随机删除, 但是一般是从末尾删除

dict.clear()   # 清空字典中的所有元素
'''
'''
补充:
其他的内置函数:
update() # 字典的合并{} + {}
fromkeys(seq[, default]) -> 将seq(可迭代对象)转成字典的形式, 如果没有默认的value将用None代替
          new_dict = dict.fromkeys(list1）--->      {'aa': None, 'bb': None, 'cc': None}
                         ---> 如果指定default，则用default替代None这个value值
		new_dict = dict.fromkeys(list1,10)	--->	  {'aa': 10, 'bb': 10, 'cc': 10}
'''
# 
dict1= {0:'tom',1:'jack',2:'lucy'}

dict2 = {0:'lily','4':'ruby'}
# dict3 = dict1+dict2 # 报错: 字典没有该运算符
# print(dict3)
# 如果想要合并两个字典, 使用update函数
dict3 = dict1.update(dict2) # 将dict2拼接到dict1中, 且重名的key用dict2的value覆盖吗, 且没有返回值
print(dict3) # None,
# 该函数没有返回值 #
print(dict1) # 将dict2拼接到dict1中, 保存dict1中

list1 = ['aa','bb','cc'] 
new_dict = dict.fromkeys(list1,10)
print(new_dict) # {'aa': 10, 'bb': 10, 'cc': 10}

''''
fromkeys(seq [,default]) -> 将seq可迭代转成字典的形式
                如果没有指定的default,则value的值用None代替

'''




