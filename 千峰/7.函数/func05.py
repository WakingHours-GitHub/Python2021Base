# 有参数的函数之可变参数
"""
def add(a, b): # 两个参数的函数只能传入两个参数
    pass
add(1, 3)
add(1, 3 ,5) # 此时就会报错了
# 解决方法： 可变参数

# 那么可变参数的定义方式：
def add(*args): # arguments 参数
    pass
# 调用：
add() # 可以没有参数，那么打印的就是() 就是空元组
add(1) # (1, )
add(1, 2) # (1, 2)
add(1, 2, 3) # (1, 2, 3)
这就是可变参数, 可以没有参数, 也可以有多个参数

那么解释一下底层的原理:
还记得拆包和装包操作吗:
*args = 散列的元素
那么
args = (散列的数据, ) # 就是这样是一个元组类型的装包了
你打印*args 就是散列的数据
打印args时候, 就是元组


"""
# 接下来我们使用一下

def add(*args): # arguments 参数: argument: 争吵
    print(args) # 此时args是一个元组 (1, 2, 3, 4)
    print(*args) # 此时*args是散列的数据 1 2 3 4
    sum = 0
    if len(args) > 0: # 有元素的情况
        for i in args:
            sum += i
        print(f"累加和是{sum}")
    else:
        print("没有元素")


add()
add(1, 2, 3, 4)

# 现在我们做一个可变参数和不可变参数一起的情况
# 回顾
a, *b = 1,2,3,4,5,6
print(a, b) # 1 [2, 3, 4, 5, 6]

# 但是在函数中
# def add(*args, name):
#     print(args, name)
# add1(1, 2, 3, "wdnmd") # add1() missing 1 required keyword-only argument: 'name'
# 可见, 在函数中, 可变参数必须放在参数列表的最后
# 先放不可变参数, 最后放方便参数 

# xxx计算出来的累加和是: XXX
def add(name, age, *args):
    print("本次计算", args, name)
    sum = 0
    if args:
        for i in args:
            sum += i
        print("%s累加和为sum: %d" % (name, sum))
    else:
        print("没有元素可以计算")

add("大佬", 1) # 本次计算 () 大佬 没有元素可以计算

add('马儿扎哈', 2,3,4,5)  # 本次计算 (3, 4, 5) 马儿扎哈 马儿扎哈累加和为sum: 12


# 综上: 可变参数必须放在最后面: name, *args
# 多个固定参数和可变参数放在一起时, 固定(不可变参数)参数必须传值, 可变参数可传, 可不传




