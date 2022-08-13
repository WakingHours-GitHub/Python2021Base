"""
如果要操作文件或者文件夹的情况下, 要使用os模块
导入os模块
    import os


部分文件操作:
文件重命名: 重命名文件, 和文件夹
    os.rename(目标文件名, 新文件名)


删除文件: 只能删除文件, 不能删除文件夹
    os.remove(目标文件名)

针对文件夹:
创建文件夹:
    os.mkdir(文件夹名字)
    默认在当前文件同级目录下, 创建文件夹.
    当文件夹存在时, 则会报错.

删除文件夹:
    os.rmdir(文件名名字)

获取当前文件目录:
    os.getcwd() -> 返回当前文件 目录的绝对路径.
    注意, 是当前文件所在目录的绝对路径, 不到当前文件.
    get current whole dir

改变默认目录:
    os.chdir(目录)
    切换到其他目录文件夹

获取目录列表:
    os.listdir(目录)
    获取目录中所有文件和文件夹, 返回一个目标
    目录可以省略, 默认是当前目录.



"""
import os

# 文件重命名
# os.rename("2.txt", "20.txt")

# 删除文件
# os.remove("20.txt")

# 创建文件夹.
# os.mkdir('./2')

# 删除文件夹

# os.rmdir('./2')

# getcwd(): 获取当前文件的工作目录
print(os.getcwd()) # D:\PyCharm\Python2021Base\黑马\13_文件

# chdir(): 改变默认路径
# 就是改变当前工作的路径
# os.chdir('../')
# print(os.getcwd()) # D:\PyCharm\Python2021Base\黑马

# listdir(): 获取某个文件夹下的所有文件和文件夹, 返回一个列表.
print(os.listdir()) #

# rename重命名文件夹
os.rename('1', '2')


