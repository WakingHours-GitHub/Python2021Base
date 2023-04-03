# 使用for循环一次性迭代多个可迭代对象
# 使用zip()函数来一次组合做个可迭代对象, 并且同时遍历. 取最短的元素个数进行迭代.
# 这种方式称之为并联方式.
# zip(*iterables) -> 返回一个zip对象, 这是一个元组生成器.
# 同样的, itertools.chain, 它能够将多个可迭代对象链接.
# 就是将可迭代对象进行串联, 依次遍历. 这种方式称之为串联方式.

def chain_test() -> None:
    from itertools import chain

    for x in chain([1, 2, 3, 4], ['a', 'b', 'c', 'd']):
        # 1, 2, 3, 4, 'a', 'b', 'c', 'd' 相当于遍历这个可迭代对象. 类似于这种串联拼接.
        print(x)
        """
        1
        2
        3
        4
        a
        b
        c
        d
        """

from random import randint
from itertools import chain

def instance_02() -> None:
    # 三个不同人数的班级.
    cls_1 = [randint(40, 100) for _ in range(42)]
    cls_2 = [randint(40, 100) for _ in range(12)]
    cls_3 = [randint(40, 100) for _ in range(7)]

    count =0
    # 组合成一个大列表, 按照顺序依次遍历.
    for score in chain(cls_1, cls_2, cls_3):
        if score > 90:
            count += 1
    print(count)



def instance_01() -> None:
    chinese = [randint(40, 60) for _ in range(30)]
    math = [randint(40, 60) for _ in range(30)]
    english = [randint(40, 60) for _ in range(30)]

    res = list()
    # 在一个for循环中迭代多个可迭代对象.
    for c, m, e in zip(chinese, math, english):  # 返回一种类元素的数据类型. 然后解包.
        res.append(c + m + e)

    print(res)


if __name__ == '__main__':
    # instance_01()
    # chain_test()
    instance_02()