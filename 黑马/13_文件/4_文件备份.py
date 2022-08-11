"""
文件备份:
    接收文件路径
    规划备份文件名
    备份文件写入数据


"""



# 接收文件路径

old_file_path = input("请输入要备份的文件路径: ")
# 输入什么类型都可以.
print(old_file_path)
# 需要对文件路径进行判断. 是否合法,
if '.' not in old_file_path:
    print("your input, is not a file")
    exit(1)

# 规划备份文件名:
# 找到最右边的., 右边就是后缀名
# 其实os.path.split()可以分隔文件路径和后缀名
# 或者使用rfind(), split()等字符串函数.
file_path, file_postfix = old_file_path.rsplit('.', 1)
# postfix表示后缀名

if file_path == '':
    print("无效文件名")
    exit(1)


# 进行拼接备份文件名. 以便区分.
new_file_path = file_path + "_backups." + file_postfix

print(new_file_path)

# 写入备份文件.
# 打开文件
old_f = open(old_file_path, 'rb')  # 使用字节方式打开
# 对于计算机来说, 底层都是使用二进制. 字节方式存储.
# 因此无论任何文件, 都可以以二进制方式打开, 只有文本文件才使用t模式打开.
new_f = open(new_file_path, 'wb')


# 文件写入:
# 如果不确定, 文件大小, 可以使用for循环读取.

while True:
    content = old_f.read(1000) # 读取1000个Bytes, 字节
    if len(content) == 0: # 表示读取完成, 终止循环
        break #
    new_f.write(content)

# 关闭文件流
old_f.close()
new_f.close()





