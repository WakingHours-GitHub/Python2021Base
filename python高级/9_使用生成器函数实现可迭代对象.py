# 实现一个可迭代对象的类, 它能够迭代出规定范围内的素数.


# 生成器是一个特殊的迭代器. 内部实现了迭代器的协议. 应该有

# 生成器: 就是在一个函数的内部使用yield关键字.
def func():
    print("func_1")
    yield 1

    print("func_2")
    yield 2

    print("func_3")
    yield 3


def generator_test() -> None:
    f = func() # 返回结果, 此时f就是一个迭代器对象,
    # 可以使用内置的next()方法.
    print(next(f))
    print(next(f))
    print(next(f))
    print(next(f))
    """
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





def PrimeNumbers(start: int, end: int) -> int:
    for i in range(start, end+1, 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            yield i



def main() -> None:
    f = PrimeNumbers(1, 30)
    for i in f:
        print(i)



if __name__ == '__main__':
    # generator_test()
    main()









