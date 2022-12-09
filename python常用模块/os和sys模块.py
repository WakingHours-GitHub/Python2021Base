"""
os标准库:
    系统相关变量和操作
    文件和目录相关操作
    执行命令和管理进程
    
os模块中的常用函数:
得到当前工作目录路径: os.getcwd(), 也就是你当前动作区路径.
返回指定目录下的所有文件和目录名: os.listdir(路径)
删除一个文件: os.remove("文件路径")
删除多个目录: os.removedirs("")
判断路径是否是一个文件: os.path.isfile("路径")
判断路径是否是一个目录: os.path.isdir("路径")
判断是否是绝对路径: os.isabs("路径")
判断路径是否存在: os.path.exists("路径")
路径和文件名分割: os.path.split()
分离拓展名: os.path.splitext()
提取路径名: os.path.dirname("路径")
获取绝对路径: os.path.abspath()
获取文件名: os.path.basename()

运行shell命令: os.system(需要运行的命令: str)
读取操作系统环境变量HOME的值: os.getenv("HOME")
返回OS所有的环境变量: os.environ
设置OS环境变量: os.environ.setdefault('HOME', 添加的环境变量) (仅仅在程序运行时有效)

给出当前平台使用的终止符: os.linesep
    windows使用'\r\n', linux使用'\n'
显示你当前使用的平台: os.name

重命名: os.replace(old, new)
    os.rename(old, new), new存在时, 则会报错
创建多级目录: os.makedirs(r"路径")
创建单个目录: os.mkdir("路径+文件夹")
修改文件属性: os.stat(file)
修改文件权限与时间戳: os.chmod(file)
拼接路径与文件名: os.path.join(path, filename)
    因为windows下是以\进行拼接的, 而linux中是以/进行拼接的,
    使用该方法可以识别操作系统, 然后自动使用当前平台下的路径拼接符
改变工作目录: os.chdir("new_path")
获取当前终端的大小: os.get_terminal_size()
杀死进程: os.kill()




sys模块:
sys.argy        命令行参数List, 第一个元素是程序本身路径
sys.exit(code)  退出程序, 正常退出时候为exit(0)
sys.version     获取python解释器的版本
sys.maxint      最大的Int值
sys.path        返回模块的搜索路径, 初始化时使用 PYTHONPATH
sys.platform    返回操作系统平台名称
sys.stdout.write("please:") # 标准输入, 引出进入条的例子
    在py3不行,
var = sys.stdin.readline()[: -1} # 标准输入
sys.getrecursionlimit() # 获取最大递归层数
sys.getrecursionlimit(n) # 修改最大递归层数
sys.getdefaultencoding() # 获取解释器默认编码
sys.getfilesystemencoding() # 获取内存数据存到文件时的默认编码


"""
import os
# os.replace() # 重命名


print(__file__) # 打印当前文件路径
# D:\PyCharm\Python2021Base\python常用模块\os和sys模块.py
# 在pycharm中打印的是绝对路径, 但是__file__打印的就是相对路径

print(os.path.abspath(__file__)) # 这样获取的就是绝对路径了.
# 这样无论是在终端还是pycharm中运行都获取的是绝对路径.























































