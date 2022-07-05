"""
条件语句:
语法:
    if 条件表达式: # :和缩进组成代码块 等同于{}
        代码块

    注意: 缩进是必不可少的, 表示代码块

if...else...:
语法:
    if 条件表达式:
        条件表达式成立 执行的代码
    else:
        条件表达式不成立 执行的代码
    注意, if,else同级缩进, 其中的代码块是更进一步缩进.
    if-else只会执行一次, 要么是if要么是else, 取决于表达式的布尔结果

if-elif-else:
语法:
    if 条件表达式1:
        条件表达式1成立 执行的代码
    elif 条件表达式2:
        条件表达式2成立 执行的代码
    ...
    else:
        以上条件表达式都不满足, 最后执行的代码.
    执行流程: 从上到下, 依次执行.
        所以判断的范围应该由小到大.

if嵌套:
语法:
    if 条件表达式1:
        条件成立执行的语句
        if 条件表达式2:
            条件表达式2成立 执行的代码

            ...



"""

# 快速体验:
if True:
    print("条件成立")
    print("代码块中")

# 没有加缩进的代码, 不在if的生命周期内.
print("代码块外")

if False:
    print("条件不成立")

age = input("please input your age that can allow you to play network: ")
# 注意, input接收的数据为str, 需要进行数据类型的转换
if age.isdigit():
    age = int(age)
    if age >= 18:
        print(f"{age}岁, 成年, 可以上网")
    else:
        print("未成年, 不可以上网")
else:
    print("输入的不是数字")

# 多重判断:
age = eval(input("请输入年龄: "))
if age < 18:
    print("未成年")
elif (age >= 18) and (age <= 60):  # 第一个表达式可以省略, 因为第一个表达式不符合, 自动符合补集
    print("工作")
else:  # 都不满足.
    print("退休")

# 在python中, 一些逻辑表达式是可以化简的.
# 例如使用and逻辑进行链接的一个区间范围, 我们可以这样去写, 但请注意, 仅仅是在python中.
if 18 <= age <= 60:  # 该种形式符合数学上的写法.
    print("工作")


# if嵌套:
# 公交车: 判断是否能够上车, 有没有足够的钱, 然后是否空座. 有空做就可以上车
#
money = 2
seat = 1

if money >= 1:
    print("有钱, 可以上车")
    money -= 1 # 有钱,
    # if嵌套: 里面的if是否执行, 取决于外面的if条件是否成立.
    if seat >= 1: # 有多余的座位
        print("有多余的座位")
    else: # 没有多余的座位
        print("没有多余的空座, 站着吧")
else:
    print("没钱, 不能上车")






























































































