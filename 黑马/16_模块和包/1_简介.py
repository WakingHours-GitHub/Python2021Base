"""
模块和包
目标:
    了解模块: 模块是什么, 模块的作用
    导入模块: 如何导入, 模块
    制作模块: 自定义模块.
    __all__: all列表, 控制模块的导入行为, 控制模块中那些可以导入, 那些不可以导入
    包的使用方法.

了解模块: 模块是什么
    模块. Module, 是一个python文件, 以.py结尾, 包含了Python对象定义和Python语句.
    模块中能够定义函数, 类, 和变量, 模块中也可能含有可指定的代码.

    因此模块, 就是一个Python文件, Python文件中有什么, 那么模块中就有什么.
    模块里面的文件是已经书写好了. 因此导入模块, 就可以调用别人写好的文件.


导入模块:
    导入模块的方式:
        import Module, Module...
        from 模块名 import 功能名, ... # 在导入时允许同时导入多个功能.
        from 模块名 import *
        import 模块名 as 别名
        from 模块名 import 功能名 as 别名

    import:
        import 模块名
        import 模块名, 模块名... # 不推荐这种写法

        调用功能:
            模块名.功能名()
    from ... import 功能
        直接使用功能名即可使用.

    from Module import *
        导入该模块中的所有功能. 导入所有代码
        直接使用功能名即可调用功能

    as定义别名
        原有的模块名可能不善长于使用, 因此我们可以使用as进行起别名的操作.
        import Module as name
        from Module import Function as name
        我们可以将模块和方法都定义成别名.
        定义别名后, 只能使用别名而不能使用原名.

"""


import math # 导入模块, 使用math.功能 进行调用即可.
"""

导入模块
测试是否导入成功. 
"""

print(math.sqrt(9)) # 开平方.
# 3.0 # math涉及到计算, 返回得到的基本都是浮点数.

# from Module import Function, ...

from math import sqrt

# 调用方式: 直接使用功能名即可调用功能.
# 不需要书写Module.Function, 直接使用Function.
print(sqrt(9))

# from Module import *
from math import * # 这里*表示所有.
print(sqrt(9))
# 因为是导入了模块中的所有功能, 因此也不需要Module.功能.

# as定义别名:
# 我们可以将模块和方法都定义成别名.
# 定义别名后, 只能使用别名而不能使用原名.
# 测试:
import time as tt # 为time起别名. 为tt

tt.sleep(2) # 使用tt进行调用.
print("hello")
# time.sleep(1)  # 报错
# 可见, 当起别名后, 只能使用别名进行操作.


from time import sleep as sp
sp(2)
print("hello")
# sleep() # 报错
# 起别名后, 原名字无法使用, 只能使用别名.




