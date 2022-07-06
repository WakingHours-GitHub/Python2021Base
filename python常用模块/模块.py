"""
模块：

什么是模块:
    集合的工具包
    文件称之为模块
    文件夹称之为包
    在Python中, 一个.py文件就可以称之为一个模块: Module
使用模块的好处:
    避免函数名, 以及变量的冲突. 分门别类.
    快速开发, 直接使用已经开发好的包和库, 快速开发实现功能
模块的分类:
    标准模块, 内置模块, 标准库 大约有300个
    第三方模块 大约有18w个左右, 需要单独安装, 使用pip模块
    自定义模块, 自己开发的.
模块的导入和调用
    import 模块名, ...
        调用: 模块.方法()
    from 模块 import 方法
        调用: 方法()
    from 模块.xx.xx import 方法 as 重命名
        从模块中的.功能, 导入方法, 并且重构命名.
        就是一个文件夹下面有多个.py文件, 一个文件是一个模块, 所以就有了'.'这种操作.
        调用: 重命名()
    from 模块 import *
        从模块中导入所有的方法
        调用: 方法()
        不过这种方式, 就没说明前面是那种包的了, 容易造成名称冲突.
        并且我们无法使用: 模块.方法()进行调用了. 我们也不知道模块下有多少个方法了


    导入模块的操作一般放在文件开头去写, 这是一种规范.

自定义模块:
    一个py文件就是就是一个模块.
    在同一层目录下可以导入.
    并且直接import 模块, 会直接执行所导入的模块(文件)

    模块 查找路径有关系


查找路径:
    模块查找路径列表:
    import sys
    print(sys.path)
    所打印的就是python的模块查找路径.
    是由近及远, 因此来查找.
    在pycharm中, 执行路径为当前目录,
    如果是单纯使用python, 就是".", 表示当前目录.

    如果想要将自己的模块文件, 可以全局文件搜索, 那么就将自定义模块放到,
    sys.path下面的目录, 建议放到第三方库的目录下. site-packages
    或者放到标准库:


第三方模块的安装：
    pypi是python的开源社区。可以上传你开发的模块。
    如何去安装：
        源码安装： 先编译, 然后在安装源码
            编译源码: python 文件名.py build
            安装源码: python 文件名.py install
        通过pip安装：
            pip install 模块名
            pip install 模块名 -i 镜像源
        卸载:
            pip uninstall 模块名

    第三方模块默认安装在: site-package文件夹下.

    例如: paramiko: 远程登陆linux服务器并且可执行命令的模块.






"""
# 导入模块
# import os, sys

# 从模块中导入一个功能(函数)
from os import path

from os.path import pathsep

# from os import *
# 直接调用
# print(name)


# print(os.path)  # <module 'ntpath' from 'D:\\PATH\\Python39\\lib\\ntpath.py'>


# 导入自定义模块：
import my_module
# 直接就会执行所导入py文件

import sys

print(sys.path)

