# 作业部分:
'''
6. 输入两个字符串, 从第一个字符串中删除第二个字符串中的所有字符.
例如, 输入'They are students.' 和 'aeiou'
则删除之后的的第一个字符串变成'Thy r stdnts.'
'''
s1 = input('请输入第一个字符串')
s2 = input('请输入第二个字符串')

# 方法一
# 字符串也可以作为集合(可迭代对象), 放进for里面
s3 = '' # 初始空字符串
for i in s1: # i每次都从s1拿出字符(可迭代)
    if i not in s2: # 如果i不在s2中, 就添加到s3
        s3 += i # 连接符
print(s3)
s1 = s3  # 赋值

# 方法二
for i in s2: # 遍历s2
    s1 = s1.replace(i,'') # 将s2中的字符,在s1中替换掉
print(s1)

s3 = ''
# 方法三
for i in s2: 
    if i not in s3:
        s3 += i
print(s3) # s3就是将s2去重(复)后的结果
for i in s3:
    s1 = s1.replace(i, '') # 然后直接替换去重后的,这样速度可能较快
print(s1)
'''
7.小易喜欢的单词具有以下特性：
1.单词每个字母都是大写字母
2.单词没有连续相等的字母（两个一样的字母不能挨着）吧

例如：
小易不喜欢"ABBA"，因为这里有两个连续的'B'
小易喜欢"A","ABA"和"ABCBA"这些单词
给你一个单词，你要回答小易是否会喜欢这个单词。

提取: 喜欢大写,并且没有相连的字母
'''
# 老师提供的算法
word = input('please input a word, judge islike: \n')
for i in range(len(word)):
    if not word[i].isupper():
        print('不喜欢, 原因有字母不是大写的!')
        break
    else: # 已经是大写字母了
        if i < len(word)-1 and word[i] == word[i+1]:
            print('不喜欢, 原因是叠词')
            break
else: # 如果for没有break
    print('喜欢')


# 自己的算法:
word = input('please input a word, judge islike: \n')

if word.isupper():
    for i in range(len(word)-1):
        if word[i] == word[i+1]:
            print('叠词')
            break
    else:
        print('喜欢!')
else:
    print('不喜欢, 不是大写字母')    

'''
3.循环提示用户输入：用户名、密码、邮箱 （要求用户输入的长度不超过 20 个字符，如果超过则只有前 20 个字符有效）
打印输出 
用户名   密码   邮箱
Admin  123    hfjs@163.com
Lily     111    yweuyr@163.com
....

如果用户输入 q 或 Q 表示不再继续输入。
'''
s = ''
while True:
    print('请输入用户名,密码,邮箱,且不超过20个字符,若超过则只有前20个字符有效')
    username = input('请输入用户名')
    if username == 'q' or username == 'Q':
        print('退出')
        break
    password = input('请输入密码')
    if password == 'q' or password == 'Q':
        print('退出')
        break
    email = input('请输入邮箱')
    if email == 'q' or email == 'Q':
        print('退出')
        break


    username = username[1:21] # 截断1~20
    password = password[1:21]
    email = email[1:21]

    msg = '{}\t{}\t{}\n'.format(username, password, email)
    # expandtabs(tabsize = 8) 将字符串中的tab符号转换成' '(空格), tab符号默认转换空格数为8
    msg = msg.expandtabs(10) # 格式好看
    s += msg # 连接起来
    
