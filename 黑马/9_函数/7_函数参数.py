"""
函数参数的详细写法:
在python中, 函数参数一共有4种写法: 位置参数, 关键字参数, 缺省参数, 可变定长参数

    位置参数(positional argument): 调用函数时根据函数定义的参数位置来传递参数.
        注意: 传递和定义参数的 顺序 及 个数 必须一致.

    关键字参数(keyword argument): 调用时通过 键=值 的形式指定. 可以让函数更加清晰, 并且更容易使用,
        同时这种方式 参数=值 指定了参数与值, 因此也无需遵循顺序.
    注意: 调用函数时, 如果有位置参数, 则位置参数必须放在关键字前去调用, 而关键字参数之间不存在先后顺序

    默认参数: 也称缺省参数, 用于在定义函数时, 提供默认值, 调用函数时可不传该参数, 默认为定义时的值,
        就是在定义时, 使用关键字参数=值的方式
        注意: 定义和调用时: 所有位置参数必须在默认参数前.

    可变参数: 也称不定长参数: 用于不确定调用时会传递多少个参数(不传参也可以)的场景.
        此时可以使用包裹(packing)位置参数, 或者包裹关键字参数, 来进行参数传递.
        包裹位置传递:
            语法: *变量名
            规范: *args python书写时底层就是使用的*args. 就表示可变参数.
            注意: 传入的参数会组包, 根据位置参数封箱(组包)成为一个元组, 为args, 这就是包裹位置传递
        包裹关键字传递:
            语法: **变量名
            规范: **kwargs 底层也都是使用kwargs, 包裹关键字参数.
            注意: 用于包裹关键字参数, key=value的形式, 因此会封箱(组包)成为一个字典
        注意, 无论是包裹位置传递, 还是包裹关键字传递, 都是一个组包的过程.





"""


# 1. 位置参数
def user_info(name, age, gender):
    print(f'name:{name}, age: {age}, gender: {gender}')


# 调用
user_info("tom", 20, "男")

# 注意事项, 顺序和个数必须一致, 否则函数逻辑错误, 或者语法错误
# user_info(20, 'gender', 'age') # 逻辑错误, 不是我们想要看到的结果. 顺序应该一直
# user_info('tom', 20) # 报错 个数不同.  TypeError: user_info() missing 1 required positional argument: 'gender'


# 2. 关键字参数:
user_info('Rose', age=20, gender='女')  # correct
user_info('Tom', gender='男', age=10)  # correct,


# 可见, 关键字参数之间无需顺序, 只需要对应的参数.

# 注意: 有位置参数时, 必须放在最前面, 并且位置参数仍然需要遵循顺序
# user_info(age=20, 'tom', gender='男') # SyntaxError: positional argument follows keyword argument
# 可见, 位置参数必须在关键字参数前


# 3. 默认参数:
def user_info_default_argument(name, age, gender='male'):
    print(f'name: {name}, age: {age}, gender: {gender}')


# 调用, 不传入gender
user_info_default_argument('tom', 29)  # 可以正常调用
# name: tom, age: 29, gender: male
# 可见, 在不传入gender参数的情况下, 使用定义时候的默认值

# 传入gender:
user_info_default_argument('rose', 19, '男')
user_info_default_argument('join', 18, gender='女')


# 都可以调用函数, 并且传入的gender参数会覆盖其默认值.

# 3. 可变参数:
# 包裹位置参数
def user_info_args(*args):
    print(type(args)) # tuple
    print(*args) # 这是单个元素
    print(args)


user_info_args("time")  #
# <class 'tuple'>
# ('time',)
# 可见, args是元组

user_info_args('tom', 'rose', 19)  # ('tom', 'rose', 19)
user_info_args()  # () 也可以不传入参数, 那就打印一个空元组
# 这就是包裹位置传递.


# 包裹关键字参数: 用于包裹多个关键词参数
def user_info_kwargs(**kwargs):
    print(type(kwargs))
    print(kwargs)

# 注意: 参数名称不可以加"", 因为变量
user_info_kwargs(name="tom", age=12)
# <class 'dict'>
# {'name': 'tom', 'age': 12}
user_info_kwargs() # {] # 单个{}, 默认就表示字典
# 只有set()才表示空集合. 例子如下:
set1 = set()
print(set1)