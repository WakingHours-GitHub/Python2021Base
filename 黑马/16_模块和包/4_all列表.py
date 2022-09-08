"""
what is "all list"
all列表是一个简称, 是一个变量名, 取值是一个列表.
作用: 控制模块导入功能时的行为.
如果一个模块文件有__all__变量, 那么当from xxx import * # 导入所有功能时,
那么只能导入all列表中的功能.



"""

# 导入模块中的所有功能
from module1 import *
# all-list, 只能限制住这种import*的形式的

test_a()

# test_b() # 报错 # 以为因为all列表中没有test_b没有在all列表中.



