# for循环
'''

应用场景:

适用于一些需要重复进行的操作

for 变量名 in 集合:
    # 语句 (同一缩进级别)

for ... else:
for 变量名 in 集合:
    # [有数据执行的]语句 (同一缩进级别)
else:
    # [没有数据执行的]语句(集合没有元素的时候执行)
    
当集合执行为空后, 进入到else中执行. 相当于在for语句执行完后在进行的一些操作


pass, break 关键字:

pass:   空语句: 用于在缩进中占位(缩进中的内容不确定), 若没有pass就会出syntax error(语法错误)
break:  跳出循环: 跳出整个for循环（包括else部分）


集合是什么, 我们这里还不知道

所以介绍range()
help(range)

'''
# 分割

'''
range()函数的使用:
1. 一个参数: 
range(n)        返回一个[0,n)的序列, 从0开始, 但是不包含n
print(range(n)) # range(0, n) # 0~n-1

2. 两个参数:
range(n, m)     返回一个[n, m)的序列 即:从n开始, 到m-1

3. 三个参数
range(n, m, step)   返回一个[n, m] 间隔为step的序列 step:步长


'''

# 例子1:
for i in range(5):
    print("Hello-->{}".format(i)) # 打印从0到4的值

print('-'*10,'分割线','-'*10)
for i in range(1,6): # 1,2,3,4,5
    print("Hello-->%d" % i) # 打印从1到5的值


# 例子2：
num = int(input('请输入要吃的馒头数量'))

name = '张无忌'
for i in range(num): # --> i 从0到num-1
    print('{}很饿， 正在吃第{}馒头'.format(name, i+1))

else:
    print('没有馒头, {}饿哭了'.format(name))



# pass和break语句:
if 10 > 7:
    print('10是大的')
else:
    pass
    # pass # 若没有pass语句, 就会出现语法错误
    # 可以认为pass占着这个位置, 然后有需要的时候, 就添加语句

for i in range(3):
    pass

# 可以作为一道面试题



print('-'*20)

for i in range(3):
    username = input('请输入用户名:')
    password = input('请输入密码:')
    if username == '张无忌' and password == '159357':
        print('登录成功!欢迎{}'.format(username))
        break # 登录成功就退出(退出一整个for循环(包括else部分))
    else:
        print('用户名或者密码有误')
else: # 只有当for集合为空的时候，才执行这条语句
    print('账号锁定, 需要重新激活!')

print('EOF结束')




