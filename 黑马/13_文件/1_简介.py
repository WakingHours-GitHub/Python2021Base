"""
文件操作:
目标:
    文件操作的作用
    文件的基本操作: 打开, 读写, 关闭
    文件备份
    文件和文件夹的操作.

文件操作的作用:
    将一些内容(数据)存储起来, 可以让程序下一次执行时, 直接使用, 而不用重新获取.

文件的基本操作:
    文件操作步骤: 打开文件, 读写等操作, 关闭文件.
    打开文件:
        file = open(file, mode='r', buffering=None, encoding=None, errors=None, newline=None, closefd=True)
        作用: 打开文件流, 并维持, 返回一个file流对象.
        参数:
            file: 目标文件路径, 为字符串类型
            mode: 模式, 默认为r, 表示读,
            buffering: 是否使用缓冲区
            encoding: 手动打开文件时, 所使用的编码格式. win默认是GBK, 其他平台基本上是utf-8
访问模式:
    模式      描述
    r       以只读方式打开文件. 文件的指针会放在文件的开头. 这是默认模式
    w       打开一个文件只用于写入, 如果不存在, 则创建. 如果存在则从文件开头写入, 覆盖文件原内容
    a       打开一个文件用于追加, 文件存在, 则文件指针指向结尾, 继续追加写入. 如果文件不存在, 则拆创建文件

    b       以二进制(字节, bytes)方式读写文件
    +       可读, 可写的模式. r+就是读写, w+也是读写, 如果不存在会创建文件.



"""

# 文件读写的实例:
import gc

f = open("text.txt", 'w')
# 以w模式打开文件, 如果文件不存在则创建文件.

# 读写操作
f.write('aaa')

# 关闭文件流
f.close()


# 测试访问模式:
# r
# f = open('text_1.txt', 'r') # 报错
# 使用r模式, (读取)  文件必须存在.
# r读取模式, 也不支持写入 (write)

f.close()

# w: 只写
f = open('1.txt', 'w')
# 使用w模式, 如果文件不存在则新建文件.
# w模式可以使用write函数, 可以写入.
# w模式, 打开文件, 默认每次指针都是文件开头. 因此写入会覆盖原有内容.
f.close()

# a: 追加模式
f = open('2.txt', 'a')
# 如果文件不存在, 也会新建文件
#
f.write('aaa')
f.write('bbb')
# 打开文件, 默认是在文件结尾, 因此是在原有基础上, 追加新的内容.

f.close()

# 默认模式为r;只读
# f = open('3.txt')
# f.close() #

gc.collect()







