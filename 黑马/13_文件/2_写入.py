"""
文件读取的相关操作:
    file.read(n=-1):
        作用: read()函数, 逐个读取字节(字符)的内容.
        n表示要从文件中读取的数据的长度, 单位是字节(字符), 如果n=-1, 则表示读取文件中的所有数据.
    file.readlines():
        readlines可以按照行的方式把整个文件的内容进行一次性读取, 并且返回的是一个列表, 其中每一行的数据为一个元素.

    file.readline():
        readline一次读取一行内容. 然后文件指针指向下一行.





"""

# 文件读写的相关操作。
f = open('text.txt', 'r')
# print(f.read())
print('-'*10)

print(f.read(10))
# aaaaa
# bbbb

# 文件是我们打开时展示的内容， 但是在计算机读取的时候都是二进制的字节。
# 文件换行时， 实际上是有一个文件换行符(\n)在其中的.
# aaaaa\n
# bbbb
# 这正好就是10个字节的内容。
f.close()


f = open('text.txt','r')
print(f.readlines())

# ['aaaaa\n', 'bbbbb\n', 'ccccc\n', 'ddddd\n', 'eeeee']
# 从这可以清晰的看到每行后有\n换行符号.
f.close()

f = open('text.txt')

print(f.readline()) # aaaaa (\n)
print(f.readline()) # bbbbb
# 可见调用readline(), 文件指针会指向下一行.

f.close()



