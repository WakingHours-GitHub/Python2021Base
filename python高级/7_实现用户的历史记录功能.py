# 实现用户的历史记录功能
# 很多应用程序都有保存历史记录的功能、例如浏览器、视频播放器等等。
# 例如显示最近的五条数据。
# 使用pickle, 和deque.

from random import randint

# 使用一个新的数据结构: deque: 双端循环队列.
# 大小固定, 如果新加数据, 则会将之前最先入队的数据pop出去.

import pickle  # 编码. 可以将python中的值编码成二进制数据.
# 这样就可以写到文件当中.
# 使用dump或者load方法. dump: 转储, 就是从内存(动态) -> 存储(静态)这个过程就叫做转储.

from collections import deque

history = deque([], 5)  # 生成队列. 存储历史数据.

N = randint(0, 100)  # 随机生成.


def guss(k):
    if k == N:
        return True
    if k < N:
        print("猜小了")
    else:
        print("猜大了")
    return False


def main() -> None:
    while True:
        data = input("请输入你要输入的数字: ")
        if data.isdigit():  # 判断是否是数字.
            res = int(data)
            history.append(res)
            pickle.dump(history, open("./history.txt", "wb"))  # dump表示编码
            if guss(res):
                break
        elif data == 'h?':  # 就是帮助文档. 就可以打印出来当前内存历史信息.,
            print("内存中的历史记录信息: ", list(history))
            file_history = pickle.load(open("./history.txt", 'rb')) # 读取二进制, 然后load进来

            print("文件中的历史记录信息: ",file_history) # 也可以进行强转.


        else:
            print("输入的不是纯数字")


if __name__ == '__main__':
    main()
