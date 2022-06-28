# 继续来说列表的增删改查
# 如何对一个现有的列表添加元素
# 增: list列表的添加

# 创建一个空列表
people = []
# 列表的内建函数使用: 添加:append()     extend()      insert()
# 我们一一介绍:
# append(element) 末尾添加(add,相当于添加)

people.append('张三丰') # 在末尾添加一个元素
print(people)

# 案例: 输入quit表示退出,实现循环添加
while True:
    name = input('请输入您要添加的明星名字')
    if name == 'quit': # 若输入quit则退出循环
        print('退出')
        break
    people.append(name)
print(people)

people = ['杨戬'] # 重新初始化

# 介绍extend(): 类似于列表的合并, 一个列表添加到另一个列表中
# 相当于addAll(), 一次性添加
names = ['张无忌','马儿扎哈','古力娜扎','小龙女']
name = '张三丰'

people.extend(name) # extend()返回值为None, 但是本身列表已经改变
print(people) # ['杨戬', '张', '三', '丰'] # 可以看到,他将'张三丰'拆开,然后加上去
# 所以其实extend的对象是一个字符串或者列表, 他会拆开,然后加到调用他的对象上去

people.extend(names)
print(people) # ['杨戬', '张', '三', '丰', '张无忌', '马儿扎 哈', '古力娜扎', '小龙女']
# 可见, 列表中的元素也被拆开,然后加到调用的对象上去

# insert() # 插入： 在指定索引位置上插入元素

# names = ['张无忌','马儿扎哈','古力娜扎','小龙女']
# index:       0        1           2          3

people.insert(1,'杨戬') # 在index = 1处，插入 '杨戬'
print(people)

# 复述以下：
# append()  末尾添加(add)
# extend()  一次添加多个元素（addAll)
# insert()  指定索引（位置）插入其中

# 列表案例：
# 产生10个随机数， 将其保存到列表中
'''
步骤：
1. 如何产生随机数: randomm模块
2. 产生的数字添加到列表中去
3. 打印列表
'''
import random
random_list = []
for i in range(10):
    random_list.append(random.randint(1,20))
print(random_list)

# 但是这个只能获取10次，但是每次的长度不一样
# 需求改变：
# 产生10个不同的随机数, 将其保存到列表中
random_list = list() # ~等同于random_list = [] # 都是赋予一个空列表
# 因为是产生10个不同的随机数, 所以循环的次数不相同, 所以不能用for,用while

count = 1
while count < 10:
    ran = random.randint(1, 20)
    if ran not in random_list:
        random_list.append(ran)
        count+=1 # 只有不同的随机数才+1
print(random_list) # 这样产生的就是10个不同的随机数了

print('--'*20)
# 找出列表中的最大值与最小值:
# 系统自带: max(), min() 分别返回列表中的最大值与最小值
max_value = max(random_list)
print(max_value) 

min_value = min(random_list)
print(min_value)

# 原理其实也很容易, 我们来自己写一个
maxTemp = random_list[0] # 假设第一个元素是最大值
minTemp = random_list[0] # 假设第一个元素是最小值
for value in random_list:
    if maxTemp < value:
        maxTemp = value
    if minTemp > value:
        minTemp = value
print('最大值是{}, 最小值是{}'.format(maxTemp, minTemp))

# 求和

sum_list = sum(random_list) # 使用系统函数对列表求和
print('系统计算求和', sum_list)

# 自己模拟求和函数
mysum = 0
for value in random_list:
    mysum += value
print(mysum)

# Python中的系统内置函数: 排序是sorted()而不是sort()
# sorted是系统函数, 而sort是list的内建函数,list.sort()
# sorted(list) -> 默认是对列表进行升序操作
# sorted(list, reverse = True) -> 降序(descending)
# reverse 反转
new_lsit = sorted(random_list, reverse=True) # 降序操作
print(new_lsit)

# sorted(list, reverse = True) # 是列表排序后逆序过来

# 自己写一个算法：用于排序：