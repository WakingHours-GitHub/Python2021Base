'''
总结：上面学到的所有知识: 
字符串方法:

# 字符串形式相关
str.capitalize(): 将字符串第一个单词大写, 返回新字符串
str.title(): 将字符串每个首字母大写, 返回title格式的字符串
str.istitle(): 判断是否为title格式（即: 是否首字母大写), 返回bool类型

str.upper(): 将字符串全部转换成大写字母,返回新字符串
str.isupper(): 判断字符串是否全为大写
str.lower(): 将字符串全部转换为小写字母
str.islower(): 判断字符串是否全是小写字母
str.isalpha(): 判断字符串是否全是字母字符组成的
str.isdigit(): 判断字符串是否全是由数字字符组成的

# 查找,替换相关
find(): find(str, beg=0, end=len(string))返回的是索引（位置）, start,end可以规定在指定区间内查找,查找失败返回-1
rfind(): 从左侧开始查找
lfind(): 从右侧开始查找(常用) 
index(): index(str, beg=0, end=len(string))   index与find方法一样, 只不过index找不到会直接报错
rindex(): 从左边index, 未找到会报错
lindex(): 从右边开始查找
replace():  replace(old, new [, max]) 替换,.中找old然后替换成new,可选参数:指定次数

# 连接:
join(): 连接符.join('str'): 将字符串字符以连接符连接, 返回一个新串

# 分割:
str.split('分隔符'): 根据分隔符分割str返回一个列表


# 网络:
str.encode(): encode(encoding='UTF-8',errors='strict')
            以 encoding 指定的编码格式编码字符串，如果出错默认报一个ValueError 的异常，除非 errors 指定的是'ignore'或者'replace'
str.decode(): 解码

# 判断是否以XXX开头或者结尾,返回bool类型
str.stratswith('substr'): 判断str是否以substr开头
str.strendswith('substr'): 判断str是否以substr结尾, 返回bool类型

# 计算包含个数:
count(): str.count('substr') 返回substr在str中的个数

# 取出空格,或者取出特定字符:
str.strip(): 执行lstrip()和rstrip(), 即取出两边的空格
str.lstrip(): 取出左边的(默认是空格)
str.rstrip()
括号里可以填入字符,使之取出特定字符

# 交换两数
a,b = b,a # 优雅



 


'''