# 逻辑运算符
# and   or    not
# and 逻辑与
# or 逻辑或
# not 逻辑非
# 逻辑运算符的运算结果同样也是True和False

'''
and: 有0出0, 全1出1
or : 有1出1, 全0出0
not: 取反
'''

flag = True
result = not flag
print(result)



# 位运算
# 了解位权,进制转换

#bin() 转换变量的二进制表示, 返回的是str
a = 13
print(bin(a), type(bin(a))) # 0b1101 <class 'str'>
b = 0b1011


# 负数怎么表示:
c = -8
print(bin(c)) # -0b1000
# 但这只是python给我们的结果,实际上负数在内存中是按照补码方式存放
# 所以真正的负数, 是对应其整数取反(反码)在加1得到的(补码)

'''
0b开头:表示二进制
0o开头:八进制: 不能超过8
0x开头:十六进制: 以字母代替10~15, 最大不能超过16
'''