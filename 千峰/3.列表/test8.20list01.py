'''
什么是list
作用: 类似于其他编程语言的数组, 但是比数组强大得多
符号: [] ->代表一个列表

列表是一个容器, 存放数据
列表也可以存放不同类型的数据
list = [string, int, char,...]
但是我们一般不会这么干, 通常一个列表里都是统一类型的
'''
# 声明, 用[]声明, 并且赋值
names = ['jack', 'tom', 'lucy', 'superman', 'ironman'] # 列表
computer_brands = [] # 声明一个空列表, 能分配吗, 看下地址

print(id(names))
print(id(computer_brands)) # 有地址, 说明分配成功

# 列表的一些操作: 增删改查
# 查: 通过索引(index),获取元素(element). 既然是索引,所以从0开始
print(names[0]) # jack ; 列表中的第一个元素
print(names[1]) # tom ; 列表中的第二个元素

'''
列表的索引和字符串一样:
names:      jack      tom     lucy     superman     iromen
index:         0       1        2          3           4
负索引:        -5      -4       -3        -2          -2  
'''
# 获取最后一个元素
print(names[-1]) # ironmen # 于字符串一样, 同样可以通过负数索引取值
# print(len(names)) # index out(数组越界)
print(len(names) - 1) # len-1才是最后一个index

# 结合循环：
for i in 'hello': # 字符串是可迭代对象， 所以可以放进for里，i每次从字符串里面取出一个
    print(i) 

    # 列表也是一个集合（序列, 可迭代对象)
for name in names: # 遍历列表
    print(name) # name每次从names中取出一个元素

# 查询names里面有没有保存超人, 有就结束
result = '有' if 'superman' in names else '没有'
print(result)

for name in names:
    if name == 'superman':
        print('有')
        break
else:
    print('没有')


