"""
模块定位顺序:
当导入一个模块时, Python解析器对模块位置的搜索顺序是:
    1. 当前目录, 即当前py文件所在的文件夹.
    2. shell变量PYTHONPATH下的每个目录.
    3. 如果没有, Python会查看默认路径, UNIX下, 默认路径为/usr/local/lib/python

    模块搜索定位是由近及远的.

    模块搜索路径存储在system模块下的sys.path变量中. 变量里包括当前目录
    PYTHONPATH由安装z过程决定的默认目录

注意!!!:
    自己的文件名不要和已有的模块名重复, 否则会导致模块功能无法使用.
    使用from ... import ...时, 如果功能名字重复, 那么调用到的是最后定义或导入的功能.





"""
# 书写代码:
# 两点注意事项
# 自己文件名不能与已有模块名重复, 如果重复则导致较远的那个模块无法使用
import time

import random #
num = random.randint(1, 5)
print(num) # 老版本会报错.
# 注意, 模块名不能和已有的模块名使用, 否则无法调用.
# 因为python解释器搜索模块是由近及远的.


# from import导入功能时, 只会定义最后定义的重复名字的功能
from time import sleep

time.sleep(1)

# 自己定义函数
def sleep():
    print("自定义sleep")

sleep()
# 所以默认会更新最后一个定义的同名函数.



















