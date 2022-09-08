"""
包: 一个文件夹,
    包将有联系的模块组织在一起, 即放到一个文件夹下, 并且在这个文件夹创建一个__init__.py的文件,
    这个__init__文件可以控制包的导入行为. 那么该文件夹就称之为包.
包和模块是不同的, 包是一个带有__init__.py的文件夹, 其中可以包括多个模块
    而模块是一个python文件, 里面包含多个功能.

制作包:
    python package, 新建包名.
    在该文件夹中, 会自动创建一个__init__.py的文件.然后我们将在init中控制导入


导入包:
    方法1:
        导入: import 报名.模块名
        调用: 包名.模块名.目标
    方法2:
        导入: from 包名 import *
        调用: 模块.目标

        使用这种形式导入, 必须要在__init__.py中添加__all__变量,
        控制允许导入的模块列表. 只有这样, 才能通过import *导入.


总结:
导入模块的方法:
    import Module
    from Module import Object
    from Module import *
导入包的方法:
    import Package.Module
    from Package import *

    as起别名.

    __all__ = [] # from ... import * 允许导入的模块或者功能列表.

"""

# 导入包的不同写法
"""
导入模块
方式1:
    导入: import 报名.模块名
    调用: 包名.模块名.目标
"""
# 导入package下的module1, 使用方式1
import test_package.module1

# 调用: 没有提示, 但是可以正常调用.
test_package.module1.testA()


# 方式2:
# from package import *
# 这种方式一定要在package文件夹下的__inti__文件, 添加__all__变量, 以指定添加模块.

from test_package import *

# 模块.目标
module1.testA()

# all列表中, 没有module2元素, 因此import *导入后, 无法导入module2模块
# module2.testB() # 报错

