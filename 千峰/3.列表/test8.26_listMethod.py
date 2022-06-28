# 列表内建函数：只有列表才能调用，并且对原列表操作

'''
添加: append()  extend()   insert()
    append(): 相当于add, 从末尾添加元素
    extend(): 相当于+,拼接, addAll
    insert(): 在index位置上插入元素

删除: del list[index] # 删除指定索引处的元素
      remove(e) # 删除列表中第一次出现的元素e,返回值是None
                  若没有找到元素e,则报错(异常)
       pop(): # 弹栈: 默认移除列表中最后一个元素, 返回值是删除的元素
                      默认是删除最后一个元素, 但是也可以指定index删除  
        clear()  # 清空, 清空列表(删除列表中的所有元素)

翻转:
    recerse() # 逆序

# 排序:
    list.sort() # 对调用列表进行排序操作, 返回值是None
    sorted(iterable, cmp=None, key=None, reverse=False)

    iterable -- 可迭代对象。
    cmp -- 比较的函数，这个具有两个参数，参数的值都是从可迭代对象中取出，此函数必须遵守的规则为，大于则返回1，小于则返回-1，等于则返回0。
    key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
    reverse -- 排序规则，reverse = True 降序 ， reverse = False 升序（默认）。

# 次数:
    count() # 统计某个元素在列表中出现的次数
'''

# 案例练习:
hotpot_list = ['海底捞','呷哺呷哺','张亮麻辣烫','热辣一号','宽板凳']


hotpot_list.append('张亮麻辣烫') # 从末尾添加
print(hotpot_list) # ['海底捞', '呷哺呷哺', '张亮麻辣烫', '热辣一号', '宽板凳', '张亮麻辣烫']

# remove:
result = hotpot_list.remove('张亮麻辣烫') 
print(result) # None # 即没有返回值
print(hotpot_list) # 删除第一个张亮麻辣烫

# 若要删除一个不存在的元素呢
# [Error] hotpot_list.remove('aaaa') # ValueError: list.remove(x) x not in list

# 综上remove是从左到右删除第一个匹配的元素, 没有返回值(None), 若没有找到则报错

# pop: 弹栈, 默认删除最后一个元素
result = hotpot_list.pop() # 返回删除的元素
print(result)
print(hotpot_list) # 最后一个元素被删除
# pop(index)函数也可以删除指定索引处的元素
hotpot_list.pop(2) # 返回删除的元素
print(hotpot_list)

# clear各位更是重量级, 清空列表中的所有元素
result = hotpot_list.clear() 
print(result) # None, 由此可见result也没有返回值
print (hotpot_list) # [] 空列表

hotpot_list = ['海底捞','呷哺呷哺','张亮麻辣烫','热辣一号','宽板凳']

# list.reverse(): 函数: 反转列表,对列表对象本身进行操作
print(hotpot_list[::-1]) # 只是倒序打印, 列表还是原来的列表
print(hotpot_list.reverse()) # None , 所以reverse同样没有返回值
print(hotpot_list) # 列表,是原来的逆序了


# sorted(list, reverse = ) # 这个系统函数,不是列表的内建函数, 所以list是参数
# 返回值是新的排好序的列表, 默认是升序排列, 参数reverse=True时为降序(实际上是先升序,然后反转)
new_list = sorted(hotpot_list)
print(hotpot_list) # 原来的列表没有变化
print(new_list) # 返回的列表是是排好序的

# list.sort(reverse=) 函数是对列表本身进行排序,返回None,调用后列表排序
result = hotpot_list.sort()
print(result) # None
print(hotpot_list) # 排好序的结果

# count: 看xxx在list中的个数
listNum = [1,2,3,4,9,5,1,1,1,1,5,65]
listNum.sort()
print(listNum)

result = listNum.count(1) # 看1在listNum中出现过几次
print(result) # 5











