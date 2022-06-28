# 书接上回

'''
words = ['hello','good','apple','world','digit','alpha']

提示输入一个单词比如：hello，如果输入的单词在列表中则删除

最后打印删除后的列表

'''

words = ['hello','good','gooo','world','digot','alpha']

w = input('请输入一个单词：')
# 方式1(我自己的方式):
if w in words:
    i = 0
    len = len(words)
    while i < len:
        if w == words[i]:
            del words[i]
            len -= 1
            continue
        i += 1
else:
    print('没有该单词')
print(words)


'''
区分:in在字符串, 列表和for循环里面的区别, 以及in和==符号的区别
首先in是一个关键字, ==是一个符号
== 表示连个变量内容是否相等, in表示一个变量是否在另一个变量中,表示包含关系

in 在字符串中表示字串在目标串中是否存在
in 在列表中表示该元素是否在列表中存在

而for中的in表示组成for的关键字, 也可以理解为迭代器,的一项操作
就是把集合中的元素一个一个赋值给变量

if 表达式:
    pass
迭代器:
for 变量 in 可迭代对象:
    pass

# 还有一点的是: 变量之间的交换
两个变量交换,别的语言往往都是需要借助临时变量
temp = num1
num1 = num2
num2 = temp
但是py有一种优雅的写法:
a,b = b,a # 不需要其他变量就可以实现两变量交换

'''


if 'good' == 'good': # == 比较的是内容:
    print('True')

if 'good' in 'goods': # in判断是否包含
    print('Ture')

if 'good' in ['goods','good','abc','aaaa']: # 表示'good'在这个列表里面
    print('in')

i = 1
for w in ['goods','good','abc','aaaa']:
    print('good' in w) # 哪个w(字符串)中有'good'
    print('->',i)
    i+=1

# 错误写法:
# for word in words:
#     if w in word:
#         del word # 只是删除了迭代器的变量,而不是原来列表的
#         break

# 老师写法:

len = len(words)
i = 0
while i < len:
    if w in words[i]:
        del words[i]
        len -= 1 # 删除完则长度-1
        continue
    i += 1
print(words)

# 今天介绍的其实是根据内容查找,然后删除该元素
# 其实list的内建函数已经为我们封装好了:就是remove()
# 如果remove('元素')没有查找到元素,则报错(Error),我们后面会讲解该函数