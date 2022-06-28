'''
# 讲解一些字符串的其他函数: is开头的一些函数
isalnum(): 若字符串至少有一个字符并且所有字符都是字母或者数字,返回True, 否则返回Flase
isnumeric(): 若字符串中只包含数字字符,返回True, 否则返回Flase
isspace(): 若字符串中只包含空格字符,返回True,否则返回Flase

常用:
isalpha(): 判断一个字符串是否全是字母,是则True, 否则Flase
isdigit(): 判断字符串是否只包含数字,是则True,否则Flase

重点:
str.join(seq): 以指定字符串作为分隔符,将seq中的所有元素(字符串表示)合并成为一个新的字符串

'''

s = ' abccd123'
print(s.isalpha()) # Flase 因为有数字

s = 'abcd'
print(s.isalpha()) # True 全是字母

s = '123456'
print(s.isdigit()) # True

'''
应用场景:
我们想从输入中作转换,如果输入的全是数字字符串我们就转换成int(int()),否则提示(字符换还有字母强转int报错)
此时我们做一个判断,判断是否全是数字,然后再用int强转,这样就不会报错了
'''

sum = 0

for i in range(3):
    num = input('请输入数字')
    if num.isdigit():
        # pass
        num = int(num)
        sum += num
    else:
        print('您输入的字符串不全是数字')
print('sum = {}'.format(sum))

# 但是这有一个问题,也就是无论输入什么都循环三次
# 我们想输入数字的时候算次数,其他时候不算,显然for循环无法解决这个问题
# 我们使用while循环:
sum = 0
i = 0 # 计数循环
while i < 3: 
    num = input('请输入数字')
    if num.isdigit():
        sum += int(num)
        i += 1 # 只有是数字的时候i才++
    else:
        print('您输入的字符串不全是数字')
print(sum)

# 重点:join(seq)
# 连接符.join(字符串): 将字符串以连接符分隔开,重新组合一个新的字符串
# newString = 连接符.join([可迭代对象])
new = '-'.join('abc')  # 即将abc以-连接
print(new) # a-b-c

# join中的参数列表中布置能放字符串, 也可以放入任何可迭代对象,例如列表
# python列表: list = [] 类似于其他语言的数组,但是列表的功能更强大
list1 = ['a', 'v', '0', '9'] # 这里的列表是一个一个字符,若想转换成字符串:
result = ''.join(list1) # 以空字符串来连接列表的中的元素, 这样就是一个字符串了
print(result) # 'av09'

result = ' '.join(list1) # a v 0 9 # 这是以空格来连接列表
print('result = {}, Type = {}'.format(result, type(result))) # a v 0 9, str

'''
区分:
join与+不同, +是将多个字符串紧密拼接起来了
但是join可以指定其中的连接符号
'''

'''
其他函数:
str.maketrans(intab, outtab): 创建字符映射的转换表,对于接受两个参数的最简单的调用方式  
            第一个参数是字符串,表示需要转换的字符,第二个参数也是字符串转换的目标
            intab -- 字符串中要替代的字符组成的字符串。
            outtab -- 相应的映射字符的字符串。
            就是把str中的intab对应替换成outtab中的字符, 具体可以参考数字替换元音
            
max(str):返回字符串 str 中最大的字母。
min(str):返回字符串 str 中最小的字母。
'''
# 截取函数:lstrip    rstrip    strip 

# lstrip(): 截掉字符串左边的空格或指定字符
# rstrip(): 截掉字符串右边的空格或指定字符
# strip(): 在字符串上执行lstrip和rstrip,即去除两边的空格
# 默认是去除空格

'''
应用场景
百度:搜索: 你可能打了一堆的空格,但是在搜索的时候你会发现看空格都消失了,
这就是strip函数使用场景
'''
s = '    hello     ' 

# 两边加上[]标识
new = s.lstrip() # 去除字符串左边的空格
print('['+new+']') # [hello     ]

new = s.rstrip() # 去除字符串右边的空格
print('['+new+']') # [    hello]

new = s.strip() # 去除字符串两边的空格
print('['+new+']') # [hello]

new = new.strip('o') # 去除两边的'o'字符
print('['+new+']') # [hell]

# split() 通过指定分隔符对字符串进行切片，如果参数 num 有指定值，则分隔 num+1 个子字符串
# 函数原型: split(str='', num=string.count(str)): 分割字符串,将分割后的字符串
# 返回值是分割后的字符串的列表
# 例: str.split('substr')表示str以substr分割,num取max次数(就是全分割)

s = 'hello world hello kitty'

result = s.split(' ') 
print(result) #['hello', 'world', 'hello', 'kitty'] 一个列表


result = s.split(' ', 2) # 以' '为分隔符, 分割两次
print(result) # ['hello', 'world', 'hello kitty']


# count(args) 求字符串中指定args的个数
n = s.count(' ')
print('个数',n) # 个数 3: 说明有s中有3个空格

s='hfdsjkhfdf;lksd;fk'
s.count('s') # 判断s字符串里面有多少个's'

'''
总结：

与大小写有关的: lower() upper()
于查找相关的: find() rfind() lfind() index()
替换: replace(old,new,num)
分割: split('分割符')
连接: join(): 连接符.join('str')
编码与解码: encode()    decode()
计算个数: count()   查找字串在目标字符串中的个数
去除空格或者指定字符: strip()   lstrip()    rstrip()
is开头,用于判断的:
isalnum()   判断字符串是否全是字母或者数字
isnumeric() 判断字符串是否只有数字
isspace()   判断字符串是否只有空格

isalpha()   判断字符串是否只有字母
isdigit()   判断字符串是否只有数字

isupper()   判断字符串是否全由大写字母组成的
islower()   判断字符串是否全由小写字母组成的

startswith('str')判断是否由str开头
endswith('str')判断是否由str结束

'''












