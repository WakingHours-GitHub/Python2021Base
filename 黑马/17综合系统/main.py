"""
我们在main中书写主逻辑
将学员和管理系统书写好后导入进来.

"""
#  程序入口文件，就是运行这个文件, 从而启动我们的项目
# 导入模块:
from mangerSystem import *

if __name__ == '__main__':  # 只有当本模块启动时, __name__变量才是__main__, 此时才进入if语句.
    # run system
    StudentManager().run()  # run
