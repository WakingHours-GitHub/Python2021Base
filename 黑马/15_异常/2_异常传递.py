"""
运行python文件的新方法, 也就是使用cmd去运行python文件.



异常的传递:
    实际上也就是捕获异常的嵌套。
    需求:
        尝试只读模式打开文件, 如果文件存在则读取文件内容, 文件不存在则提示用户即可.
        读取文件内容要求: 循环读取文件内容, 读取过程中如果检测到用户意外终止程序, 则except捕获异常并提示给用户.

    分析:
        首先要使用try尝试文件打开的操作, 然后只有文件打开的情况下, 我们才去循环读取文件中的内容.
        因此这里使用的嵌套的异常捕获
        如何终止循环中的程序呢, 使用ctrl+c, 这样程序就会被强制终止, 同时会报出键盘终止的异常信息。







"""

import time

try:
    f = open("test.txt")

    # 尝试循环读取内容
    try:
        while True:
            content = f.readline() # 一次读取一行.
            # if read end, exit
            if len(content) == 0:
                break
            time.sleep(3) # 停止, 方便我们手动终止程序
            print(content)
    except:
        # 在cmd中如果使用键盘中断则捕获异常, 进入该except
        print("在cmd使用键盘中断")

    finally:
        f.close()


except:
    print("该文件不存在")








