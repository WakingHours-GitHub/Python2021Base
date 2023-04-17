"""
Python提供了一种更加简便的写法, contextlib.




"""
import contextlib

@contextlib.contextmanager # 可以将我们的生成器函数变成我们的上下文管理器.
def file_open(file_name: str): # 会将这个函数, 包装成with对象, 巧妙的用到了生成器的特性.

    # 这就变成了一种顺序的逻辑, 更符合人的思维, 首先打开, 然后操作, 最后关闭.
    print("file open") # 相当于__enter__逻辑.

    yield {}

    print("file end") # 相当于__exit__的逻辑.
# 然后我们的contextmanager就可以将这个生成器函数, 支持with协议.

with file_open("lipu.txt") as f_opened:
    print("file_processing")
# file open
# file_processing
# file end









