# 集合:set
# 列表: 可以重复, 并且有序, 可以用index
list1 = [3,1,5,4,8,9,1,5,9]
# 而集合是无序的,并且不可以重复
# 像高中的集合的概念

# 声明集合
s1 = {} # 这不是空字典吗
print(type(s1)) # <class 'dict'> #这是一个字典
# 直接用{}声明, 系统默认认为这是一个字典
s1 = set() # 只能用set() 生成一个空集合
print(s1) # set()

# 字典: {key: value, key: value, ...} # 呈键值对出现
# 集合: {element1, element2, ...}  # 而集合中的元素单个出现
 
s2 = {1,2,23} # 在{} 里放入单个元素
print(type(s2)) # <class 'set'>
# 我们来看一个集合的特性:
s2 = {1,1,3,3,5,5,6,4,4,2,2}
print(s2) # {1, 2, 3, 4, 5, 6}
# 我们发现集合中没有重复的元素, 并且我们放入进的元素已经去重了

# 字典的应用 : 首先就是他的最重要的一个应用set()
list1 = [3,1,5,4,8,9,1,5,9]
s3 = set(list1)
print(s3) # {1, 3, 4, 5, 8, 9} # 每个元素只有一次, 去除重复项

# 介绍完集合的声明和特性
# 对于集合的增删改查:
# 增加: set() 
# set.add()    set.updata()
# add(): 添加一个元素到调用的集合中去
s1 = set() # 声明一个空集合
returnResult = s1.add('hello') # 没有返回值: None
s1.add('小猪佩奇')
s1.add('luck')
print(s1, returnResult) # {'hello', '小猪佩奇', 'luck'} # 每次打印都不一样, 所以再次证明set是无序的

# updata() # 一次性添加多个元素, 列表, 元组, 都可以放进参数列表, 都可以添加到集合
t1 = ('张三丰', '马儿扎哈', '古力娜扎')
returnResult = s1.update(t1) # 没有返回值: None
print(s1, returnResult)

# 删除
# 因为集合是无序, 不重复的, 所以就不可能通过index来删除元素
# set.remove(element) 按照内容删除元素, 如果element在set中存在,则删除, 若不存在,则报keyError错误
# set.pop(): 文档中定义: 随机删除, 不过一般删除第一个元素
# set.clear() # 清空, 直接清空集合中的元素
# discard() 类似于remove()都是根据内容查找,并删除, 只不过discard()找不到元素时并不会报错, 而是返回None
# dicard: 丢弃, 废弃

# s1.remove('1')
# print(s1)

result = s1.discard('1')
print(result) # None 但是不会报错

s1.pop()
print(s1)

s1.clear()
print(s1) # set()

'''
    1. 产生10个1~20的随机数, 去除里面的重复项
    2. 键盘输入一个元素, 将此元素从不重复的集合中删除
'''
# 思路:
# 先生成随机数放到列表, 然后强转成set, 去除重复项 








