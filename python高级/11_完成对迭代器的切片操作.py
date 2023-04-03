# 完成迭代器的切片操作

# 在python中文件对象是一个可迭代的对象, 我们是否可以使用切片的方式得到一个指定范围的内容呢.
# 那么我们如何对f使用切片操作. 需要使用itertools.islice方法, 它能够返回一个迭代对象切片的生成器.
# 生成器, 可以认为说, 用多少取多少.

def code_test() -> None:
    f = open("test.txt", "r")  # 返回文件对象
    # print(f[10: 20]) # 没办法直接读取.
    # f.readlines() # 可以使用realines()函数读取, 但是他是一次性读取的, 可能会占用内存.
    # 对文件对象进行迭代:
    for res in f:
        print(res)
    f.close()


def main() -> None:
    from itertools import islice
    f = open("test.txt", "r")  # 打开文件.
    obj = islice(f, 3, 5)  # 生成islice对象., 这就可以可以使用切片操作了.
    """
    islice(f, 300) # 从0位置读取到300行.
    islice(f, 300, None) # 从300行的位置读取到末尾.
    """
    for item in obj:
        print(item, end='')

    f.close()


if __name__ == '__main__':
    # code_test()
    main()
