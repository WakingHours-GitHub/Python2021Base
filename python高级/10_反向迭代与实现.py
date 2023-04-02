# 完成反向迭代以及实现反向迭代.

# 实现一个连续浮点数发生器FloatRange, 功能类似range(). 根据指定的范围和步长产生一系列连续的浮点数.
# 例如: FloatRange(3.0, 4.0, 0.2)可以产生一下序列.
# 正向: 3.0 > 3.2 > ....
# 反向: 4.0 > 3.8 > ....


# 内建函数: reversed(可迭代对象) # 返回一个迭代器对象.
# 可迭代对象里面有一个__reversed__()方法, 类似于iter方法. 用来反转迭代.
# 通过实现__reversed__()方法, 当使用reversed函数时, 底层就会调用__reversed__()方法.
# 因此实现反向迭代, 首先就要实现__reversed__()魔术方法.


class FloatRange:
    def __init__(self, start, end, step=0.1):
        self.start = start
        self.end = end
        self.step = step

    # 实现一个生成器. 可迭代对象.
    def __iter__(self):
        t = self.start
        while t <= self.end:
            yield '%.1f' % t  # 格式化我们的t.
            t += self.step  # 然后还需要加上我们的步长. 达到正向迭代

    # 反向迭代器
    def __reversed__(self):
        t = self.end # 从后往前遍历.
        while t >= self.start:
            yield '%.1f' % t
            t -= self.step


def main() -> None:
    for item in FloatRange(3, 5, 0.5):
        print(item)

    print("==" * 20)
    # 反向迭代:
    for item in reversed(FloatRange(3, 5, 0.5)):
        print(item)



if __name__ == '__main__':
    main()