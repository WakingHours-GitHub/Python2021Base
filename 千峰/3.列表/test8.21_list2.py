# 增删改查操作

brands = ['hp','dell','thinkpad','支持华为','lenovo','mac pro','神州']  # HASEE

# 改: 修改操作 # 将最后一个元素'神州',改变为其他元素
print(brands) # 打印整个列表
print(brands[-1]) # 打印列表中的最后一个元素
brands[-1] = 'HASEE' # 将最后一个位置的元素赋值为HASEE
# 赋值的步骤: 1. 查找该元素(通过index来查找) 2. 覆盖该位置上元素
print(brands) # 这样就修改完了
# 注意这里是通过index来查找需要修改的元素

print('-' * 30) # 分割

# 现在我想讲'支持华为'改成HUAWEI

# 错误写法:
for brand in brands: # 每次从列表中取出一个元素赋值给brand(迭代)
    if '华为' in brand: # 判断是否在当前元素中
        brand = 'HUAWEI' # 但是这个brand只是一个变量, 与原来的列表不一致
# 上面这种是错误写法
# 因为修改的只是brand这个临时变量,正确的写法是通过index来修改元素的位置,从而修改
print(brands) # 还是原来的列表

# 正确写法
for i in range(len(brands)):
    if '华为' in brands[i]: # 我们需要通过index来修改
        brands[i] = 'HUAWEI' # 修改时直接修改列表中的元素
        break
print(brands) # 成功修改

# 增删改查的删:
# 关键字: del (delete)

del brands[2] # 删除index = 2的元素(第三个元素) # 删除ThinkPad
print(brands)

# 删除案例: 只要出现hp, mac都需要删除 (删除多个元素的情况)
print('-'*20) # 切割

# 错误写法:
# for i in range(len(brands)):
#     if 'hp' == brands[i] or 'mac' == brands[i]: # 如果有hp或mac
#         del brands[i] # 删除
# print(brands) # 错误

# 分析原因: 删除一个后,列表中的元素就少一个,而此时i仍在+1,所以会出现要删除元素的后面元素不会被检查
# 初次之外, 由于len-1, 而range(len)已经产生序列了,所以会出现列表越界错误

# 修改: 使用while循环

l = len(brands)
i = 0 # 循环变量
while i < l:
    if 'hp' in brands[i] or 'mac' in brands[i]:
        del brands[i] # 删除
        l -= 1 # 长度-1
        continue # 
    i += 1 # 循环变量+1
print(brands)

'''
之前做的在字符串中删除另一个字符串的元素
str1: They are students
str2: yews
从str1中删除str2的字符

同样对列表:
words = ['hello','good','apple','world','digit','alpha']

输入一个单词.如果输入的单词在列表中则删除
最后打印删除后的列表

'''

words = ['hello', 'good', 'apple', 'world', 'digit', 'alpha']
w = input('请输入一个单词')
for i in range(len(w)):
    if w == words[i]:
        del words[i]
        break # 用for和break只能删除一个
else:
    print('没有该单词')
print(words)

# 改进: 删除多个的情况
len = len(words)
i = 0
while i < len:
    if w == words[i]:
        del words[i]
        len - 1 # 删除完之后长度-1
        continue
    i+=1
print(words)






