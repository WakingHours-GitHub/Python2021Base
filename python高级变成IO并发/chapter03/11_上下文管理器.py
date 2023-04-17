"""
什么是上下文管理器:
    with语句. 简化try finally语句.



"""

def exe_try():


    # try except finally
    try:
        print("code started")
        raise KeyError

        return 1
    except KeyError as e:  # 只能捕获KeyErro这一种异常
        print("Key error")
        return 2

    else:  # 如果没有异常的情况下, 就进入else
        print("no error")
        return 3
    finally:  # 无论有没有异常, 最终都会进入. 一般做资源释放.
        print("finally")
        return 4
    # 压栈, 2,4. 然后返回的时候, 直接从栈顶去取, 所以返回4. 所以说顺序一定要讲清楚.


# 上下文管理器: 回顾Python中的协议, Python是基于协议来进行编程的.
# 上下文管理器, 是我们Python中的第一个协议, 上下文管理器协议.
# 既然是协议, 那么就和我们的魔法函数挂钩的. 我们是通过魔法函数来实现上下文管理器.
# 涉及到两个魔法函数:__enter__, __exit__.
# 通过将一些特定的魔法函数实现, 那么这个类, 就具有某些特性, 这样一来就完成某种属性.


class Sample:
    def __enter__(self):
        print("enter")
        # 因此可以在enter中获取资源
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # 在exit中释放资源.

        print("exti")

    def do_someting(self): # 操作资源.
        print("doing something")

def exe_with() -> None:
    # 实现了这种协议, 那么我们就可以直接使用with.
    with Sample() as sample:
        sample.do_someting()

def main():
    # print(exe_try())
    """
    code started
    Key error
    finally
    4

    """

    # with语句:
    exe_with()
    """
    可见, 调用with的时候, 调用了entre函数, 结束的时候调用了exit函数
    enter
    doing something
    exti

    """


if __name__ == '__main__':
    main()