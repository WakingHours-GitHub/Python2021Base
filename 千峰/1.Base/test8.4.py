print('test, 这是一个测试语句')
test = '''
这是测试
\'\'\'
字符保留原格式的应用

'''
print(test)

print(test, type(test)) # type()返回变量类型

print('-------分割线--------')


print('w' + 'd' + 'n' + 'm' + 'd') # str + str 必须是同类型才可以使用+(连接符)进行连接
# 但是当类型不一样时,就会报错, 例如:
age = 10
# print('岁数:' + age) # 报错
# 我们可以使用str()函数  int -> str (类似于强制类型转换)
print('岁数:' + str(age)) # 正确
# 或者使用下面的方法: 占位符

print('下面测试，占位符的应用')
NAME = '张三丰'
age = '19'
print('我叫%s, 我%s岁' %(NAME, age)) # 底层: %s -> str 底层直接套一个str(类似java的toString)
# 同理 %d (int() 强转成为int) %f (强转成float)
# %f float 小数点后面的位数,且是四舍五入 例: %.2f 表示小数点后保留两位

# 作业:练习:

'''
格式: 
电影:xxx
人数:xxx
单价:xxx
总票价:xxx (小数点后面保留1位)

'''
move = '波西米亚狂想曲'
ticket = 45.9
count = 35
total = ticket * count
print('电影:%s\n人数:%d\n单价:%.1f\n总票价:%.1f' % (move, count, ticket, total))


# 另一种方式:
message = '''
电影: %s
人数: %d
单价: %f
总票价: %.1f
''' % (move, count, ticket, total) # 注意, 这里的%() 要与结尾的'''在同一行
                                   # 或者在'''后加上\(反斜杠)


print(message)

# 以上就是输出的格式化函数,下面介绍输入的格式化.