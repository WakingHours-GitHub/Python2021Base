"""

import os

# 1. 系统相关内同
# os.name # 标识当前操作系统的类别.
print(os.name) # nt: 就是表示win10操作系统

# 配置好的环境变量
print(os.environ)

# 文件分隔符: 在windows下是\, linux下是/
# 打印文件分隔符
print(os.sep)
print(os.pathsep) #  文件分隔系统.
print(os.linesep) # 换行符的分隔符: '\r\n'

# 2. 文件和目录操作
# 创建目录, 默认是在当前目录下.
os.mkdir("")

# 删除目录.
os.rmdir("")

os.makedirs(), os.removedirs() # 创建和删除多级目录的方法

os.stat() # 目录的状态

os.getcwd() #  打印当前所在目录.

os.rename() # 重命名
os.replace() # 重命名

# 子模块: path
os.path.split() # 分割路径和文件名
os.path.isabs() # 路径是绝对路径

os.path.isfile() # 判断是否是一个文件
os.path.isdir() # 判断是否是一个目录

os.path.exists() # 判断路径是否存在

os.path.getatime() # 拿到文件最后的修改时间, 以时间戳来表示
os.path.getctime() # 创建时间,
os.path.getmtime() # 最后存储时间

os.path.getsize() # 拿到文件大小



with open() ... # 文件创建
os.remove()  # 文件删除



# 3. 执行命令和管理进程.
# 管理进程只支持在linux下
# 执行命令
# os.system()
# os.popen()
# 不过现在执行命令一般都是用sys模块了
# 不推荐使用os执行命令了.



























"""
