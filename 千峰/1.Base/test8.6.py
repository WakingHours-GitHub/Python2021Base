# 运算符

# 1. = 赋值运算符

name = 'admin' # 这里'admin'看成一个常量字符串, 编译器就会专门给一个地址存放这个字符串
# 此时name里面就存放的是'admin'的地址, 此时也称name指向了'admin'
# 以此来实现复用, 节省空间
name1 = name # 此时name1也指向'admin'
print(id(name), name) # 1844259716208 admin
print(id(name1), name1)# 1844259716208 admin

# 函数id CPython(python的编译器是用c语言写的
# 所以这里返回的是这个对象的内存地址)
# help(id)

name1 = 'admin1' # 此时python检查常量池中有无该字符串,若没有,则申请
# 此时name1的指向就与name不同了,因为不是同一个字符串
print(id(name1), name1) # 1848902286192 admin1

print(id(name), name) # 1848902286512 admin



num = 8 # 这个num也是一个指针
print(id(num), num)
# 复合运算符
num += 5 # num = num + 5 (此时+为运算符)
print(num)
num -= 10
print(num)

a = 'abc'
a += 'ff'  # 等效于 a = a + 'ff' (此时+为连接符)
print(a) # abcff
# 字符串只有+=没有-= *= /=an


# 拓展运算 ** //
a = 8
b = 2

result = a * b
print('乘法运算',result)
result = a / b
print('除法运算', result)

# 那么**和//是什么作用呢
result = a ** b # 其实就是a的b次方,就是a乘以b个a而已(次幂)
b = 3
result1 = a ** b
print(result, result1) # 64 512

b = 3
result = a // b # 整除 8 / 3 = 2...2 整除
print(result)
# 要记住,//不是开方,而是整除

result1 = a % b # 取余mod,8 / 2 = 2...2 求余
print(result1)








































