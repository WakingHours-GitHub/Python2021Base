# 使用线程完成并发任务.

import time
import threading  # 用来完成多线程的标准库


# threading是一个py文件. 有一个Thread类




def work_1():
    for i in range(5):
        print("work_1")
        time.sleep(1)


def work_2():
    for i in range(5):
        print("work_2")
        time.sleep(1)


def main() -> None:
    # work_1()
    # work_2()

    # 创建线程对象:
    t1 = threading.Thread(target=work_1)
    t2 = threading.Thread(target=work_2)
    t1.start()
    t2.start()

if __name__ == '__main__':
    main()
