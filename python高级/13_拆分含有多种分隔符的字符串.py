# 我们需要把某个字符串根据不同分隔符拆分成不同的字段.
from typing import List

s = 'hs,i|uags;df\tsg;qwesdeff'


# solution1: 使用str.split()方法, 每次处理一种分隔符.
#   通过str.split()方法和map()函数, 进行映射.
# solution2: 使用正则表达式: re.split()一次性完成字符串分割.


def solution1() -> None:
    res1 = s.split(',')
    print(res1)  # 返回的是一个列表.
    print(list(map(lambda x: x.split('|'), res1)))
    r"""
    ['hs', 'i|uags;df\tsg;qwesdeff']
[['hs'], ['i', 'uags;df\tsg;qwesdeff']]
    """

    # 封装成一个函数
    def my_split(s: str, ds: List[str]) -> List[str]:
        res = [s]  # 变成iterable. 使之可以放入map函数当中
        for d in ds:
            t = []
            list(map(lambda x: t.extend(x.split(d)), res)) # 降维.
            res = t
        return [x for x in res if x]  # 不要空字符串.

    # 测试:
    print(my_split(s, ",|\t;'"))
    # ['hs', 'i', 'uags', 'df', 'sg', 'qwesdeff']
    # very good!


# 第二个方式: 使用正则表达式:
def solution2() -> None:
    import re # 导入re. 去学习一下re语法规则.
    s = 'hs,i|uags;df\tsg;qwesdeff'
    res = re.split('[,|;\t]+', s) # []表示其中的任意字符, +表示字符出现1次或者多次.
    print(res) # ['hs', 'i', 'uags', 'df', 'sg', 'qwesdeff']





if __name__ == '__main__':
    # solution1()
    solution2()