'''
列表要告一段落了
总结一下列表:
列表关键字: list
1. 定义, 声明:
list = [] # 生成一个空列表(申请内存空间)
list = list() # 也是返回一个空列表

list = [元素, 元素 ...] # 初始化列表

2. 可以使用的运算符
+
*
in
not in
is
not is

3. 系统提供的函数
len(list) # 返回列表的长度(int)
list = sorted(list, reverse=Flase) # 将列表排序, 返回排好序的列表, 默认是升序,reverse=True时,降序
# list.sort() # 对调用的列表排序, 没有返回值
max()
min()
list()
enumerate(可迭代对象) # 枚举, return: index, value

4. 列表本身的方法(内建函数)
# 对列表的操作: 增删改查
添加元素:
    list.appen()            # 末尾添加
    llist1.extend(list2)    # 将list2拼接到list1后
    list.insert()           # 在指定下标处插入
删除:
    del lsit[index]         # 关键字, 删除index处的元素
    list.remove(element)    # 删除指定内容的元素, 如果元素不存在, 则报异常
    list.pop([index])       # 默认删除最后一个元素, 但是也可以指定index,删除指定位置上的元素
    list.clear()            # 清空列表, 成为一个空列表
改:
    list[index] = value     # 修改索引元素, 注意不能越界index < len(list)
查:
    list[index]             # 直接通过下标查询


其他:
    list.count(ele)          # 指定元素的个数
    list.sort()              # 排序
    list.reverse()           # 逆序

'''
# 今天开始学习的新的内容
'''
元组:
类似列表, 都是容器, 可以存放元素
特点:
关键字: tuple
符号: ()
特点: 元组中的元素定义后,就不可以修改,类似于只读,只能看不能写

'''

t1 = () # t1 = tupel() # 都是定义一个空元组
print(t1, type(t1)) # () <class 'tuple'>

# 元组的特点:
t1 = (1)
print(t1,type(t1)) # 1 <class 'int'> # 可以发现, 这是一个int类型

t2 = ('hello', )
print(t2, type(t2)) # ('hello',) <class 'tuple'> # 这个就不是str类型,而是元组

# 上述这种情况是元组的一个特性, 如果元组中只有一个元素, 那么类型就是他本身
# 所以我们如果想要声明只有一个元素的的元组, 那么我们需要在元素后面加上','


t4 = (3,5,4,1,3,4,5,6,12,3,4) # 元组一旦创建就无法修改
# 元组的特定点: 创建后就无法对元组进行操作了, 所以增删改都无法进, 只能查


# 元组无法修改, 那么我们想生成10个随机数存放到元组中去,怎么办
# 我们可以先用list保存十个随机数, 然后再强转成tuple
import random

list = []
i = 1
while i <= 10:
    ran = random.randint(1,20)
    if ran not in list:
        list.append(ran)
        i += 1
print(list)

# tuple() 强转成元组类型
t5 = tuple(list)
print(t5) # 元素一样, 只是变成了() 元组类型

# 那么一旦元组被创建, 就无法修改
# 查询(根据下标): 使用切片对元组进行截取 [::]使用切片操作获取元组的元素
# 查询(根据内容): tuple.index()函数,查询内容, 返回第一次出现的index
print(t5[0]) # 拿到index=0的元素
# 同样支持-号, 和付下标
print(t5[-1])

print(t5[2:-3]) # 返回一个元组
print(t5[::-1]) # 倒叙

# 使用index函数,根据元组的内容返回所在下标


# 使用系统内置函数:(与列表大致相同)
# 最大值与最小值
print(max(t5)) # 找出元组中的最大值
print(min(t5)) # 找出元组中的最小值

# 求和
print(sum(t5)) # 对元组求和

# 求长度
print(len(t5)) 

# 元组中的内建函数(元组调用的函数)
# tuple.index(element) # 查找element在元组中的是否存在,若存在则返回下标, 若不存在则报错
# tuple.count(element) # 计算element在元组中出现的个数

print(t5.index(4)) # 在元组中查找4返回index

print(t5.count(5)) # 计算5在元组中出现的次数