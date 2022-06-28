''' 
字符串:
string由
' ' " " ''' '''围起来的称为字符串
其中''' ''' 是保留原格式的字符串

字符串的比较: == 和 is 
其中==比较的是内容, is比较的是地址

'''


s1 = 'abc'
s2 = "abc"
s3 = '''
abc
''' # 这种三引号的字符串是保留原格式的

print('s1:id是{}, s2:id是{}, s3:id是{}'.format(id(s1), id(s2), id(s3)))

print('-' * 10)

print(s1 == s2) # True
print(s1 is s2) # True

print('-'*10)

print(s1 == s3) # False
print(s1 is s3) # False
# 综上： == 是比较内容， is是比较地址
print('-'*10)

s1 = input('please input s1: ') # 123
s2 = input('please input s2: ') # 123
# input函数是从键盘输入流，所以从input中输入的都默认为字符串
# 因为是流输入，在底层，即使两个字符串输入相同,但起地址仍不不相同
print('s1 = %s, id = %d \n s2 = %s, id = %d' % (s1, id(s1), s2, id(s2)))
# 123 2819...128 123 1819...192 # 可见内容相同, 地址不同
print(s1 == s2) # True
print(s1 is s2) # False

# 常量字符串运算符: + * 
# + 在字符串中为连接符, 而* 在字符串可以意为复制(倍数)
s3 = s1 + s2 # 将s1 和 s2 拼接赋值给s3
s4 = s3 * 5 # 将s3复制五份复制给s4 (倍数)
print(s3, s4) # 123123 123*5

# in, not in关键字
# in: 在...里面
name = 'steven'
# 需要查找的字符串必须为一个整体, 不连的无法查找
result = 'eve' in name # 返回一个bool类型: True False
print(result) # True

# not inL: 没有在...里面
result = 'tv' not in name
print(result) # True

# 字符串的格式化输入输出
print('','','')
print('%s说%s' %(name, 'Fucking world'))
print('{}'.format)

# r 在print('')字符串前面加r, 保留原格式, 不发生转义
print(r'%s说: \'哈哈哈\' ' % name) # \'没有发生转义

# 初始列表:
filename = 'picture.png'
'''
       p   i   c   t   r   u   e   .   p   n   g
方向-> 0   1   2   3   4   5   6   7   8   9   10
      -11 -10 -9  -8  -7 -6  -5  -4  -3  -2  -1  <-方向
      可见[:-2] ~ [:9]

'''

# 通过[index]索引, 取出目标位置处的值

print(filename[5]) # u 特点:只能取出一个字母
# [start: end]: 
# 其实就是和ranage()差不多, 都是包前不包后
# ranage(1,10) <=类似=> [1: 10]. 范围都是[1,10) (不包括10)

print(filename[0:7]) # picture

# 截取字符串
print(filename[3:7]) # true

# start或者end省略
print(filename[3:]) # end省略, 表示一直取到字符串的末尾
print(filename[:7]) # start省略, 表示从0索引处开始取

# 负数的情况呢?:
print(filename[8: -1]) # pn # [8,-1) ~ [8, 10) = [8, 9]
# 负数省略的情况:
print(filename[:-2]) # picture.p # 从最一开始, 到-3(8)

print(filename[-1:]) # g

print(filename[-5:-1]) # e.pn

print('=>',filename[10:0]) # 空. 从10到0,方向->,所以找不到,所以为空

# [start: end: step]
# 起始的索引, 结束的索引, 以及步长('-'代表方向)

# [::-1] 倒叙
str = 'abcdefg'
print(str[::-1]) # 逆序输出
 
print(str[-1:-5:-1]) # 首先方向从右到左侧 -1到-5:gfed

print(str[5:0:-1]) # 方向从右到左, 5->0 方向不对,逆向取值:fedcb

print('->',str[5:0:1]) # 5->0, 方向:左->右: 所以很明显,从5开始向右找0就是没有,空的: (空)

# 不是间隔为1的情况:
print(str[::2]) # acdg # 间隔为2,输出

print(str[::-2]) # geca # 间隔为2,逆序打印



'''
总结:
字符串[start: end: step]
分别是,起始位置,终止位置,以及方向步长
方向: 1 表示从左->右 (从左到右)
     -1 表示从从左<-右 (从右到左)

strat和end: 其实就是和ranage()差不多, 都是包前不包后
所以截取范围:[start, end)
# ranage(1,10) <=类似=> [1: 10]. 范围都是[1,10) (不包括10)

      注意: 起始,结束与方向的关联
例如: 正向:  5:0   为空
      反向:  5:0  就可以取

Python 字符串直接在方括号（[]）中使用索引即可获取对应的字符
字符串中第一个字符的索引为 0、第二个字符的索引为 1，后面各字符依此类推。
此外，Python 也允许从后面开始计算索引，最后一个字符的索引为 -1，
倒数第二个字符的索引为 -2······依此类推。

要素:
1. step 步长要注意方向和步长
2. 注意起始位置与结束位置的方向

'''

'''
练习: str: hello world

1.逆序输出:world: -> dlrow
2.正向输出:hello
3.逆序输出整个hello world
4.获取oll, 打印
5.打印llo wo

'''
str = 'hello world'
# 1.
print(str[-1:-6:-1]) # dlrow

# 2.
print(str[0:6]) # hello

#3.
print(str[::-1])

#4.
print(str[6:1:-1]) # oll

#5.
print(str[2:8:1]) # llo wo
