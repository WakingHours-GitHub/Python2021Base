# 实现一个可迭代对象的类, 它能够迭代出规定范围内的素数.


# 生成器是一个特殊的迭代器. 内部实现了迭代器的协议.
# 也就意味着他底层实现了__next__()方法, 并且他是可以被for迭代的, 因此他也应该实现了__iter__()方法.

# 生成器: 就是在一个函数的内部使用yield关键字.
def func():
    print("func_1")
    yield 1

    print("func_2")
    yield 2

    print("func_3")
    yield 3


def generator_test() -> None:
    f = func() # 返回结果, 此时f就是一个迭代器对象.
    # 可以使用内置的next()方法.
    print(next(f))
    print(next(f))
    print(next(f))
    print(next(f))
    """
    yield就是return并且暂停.
        输出打印.
        func_1
        1
        func_2
        2
        func_3
        3
        Traceback (most recent call last):
          File "D:\PyCharm\Python2021Base\python高级\9_使用生成器函数实现可迭代对象.py", line 35, in <module>
            generator_test()
          File "D:\PyCharm\Python2021Base\python高级\9_使用生成器函数实现可迭代对象.py", line 24, in generator_test
            print(next(f))
        StopIteration
    """


class PrimeNumbers:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    # 实现对应的方法, 即遍历规则
    @staticmethod
    def is_prime_numbers(k: int) -> bool:
        if k < 2:
            return False
        for i in range(2, k):
            if k % i == 0:
                return False
        else:
            return True

    # 重写__iter__()方法.
    def __iter__(self):
        for k in range(self.start, self.end+1):
            if self.is_prime_numbers(k):
                yield k






def PrimeNumbersFunction(start: int, end: int) -> int:
    for i in range(start, end+1, 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            yield i



def main() -> None:
    # f = PrimeNumbers(1, 30)
    # for i in f:
    #     print(i)

    for item in PrimeNumbers(1, 30):
        print(item)



if __name__ == '__main__':
    # generator_test()
    main()









