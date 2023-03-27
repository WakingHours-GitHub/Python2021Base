# 统计容器类型的元素出现频率


from random import randint


# 统计频率
def instance_0() -> None:
    # 找到一个列表中出现次数最高的三个元素, 并且显示出现次数
    list_data = [randint(0, 20) for _ in range(20)]
    print(list_data)
    # {字符: 出现次数, ... }使用这样一种数据结构去实现.
    dict_data = dict.fromkeys(list_data, 0)  # 就是从一个可迭代结构生成字典, 每个key对应的value都是0
    # 这里的key也是没有重复的. 字典中的key是不允许重复的.
    print(dict_data)

    for x in list_data:
        dict_data[x] += 1
    print(dict_data)

    # 第一种方式: 进行排序, 然后使用切片得到前三个元素, (这种方式不包括次数相同的情况)
    method_1 = sorted(dict_data.items(), key=lambda x: x[1], reverse=True)[: 3]
    print(method_1)


# 第二种方式: 使用容器工具类的Counter
def instance_1():
    from collections import Counter
    list_data = [randint(0, 20) for _ in range(20)]
    counter_obj = Counter(list_data)
    print(counter_obj)  # Counter对象也是一个字典.

    print(counter_obj.most_common(3))  # 这就代表出现频次最高的前三位.
    # 与上述方法一样.


# 现在是统计英文文章的词, 或者字符.
# import this.
# 他就会输出python之禅. 英文的小文章.
def instance_2() -> None:
    # import this
    from collections import Counter
    import re  # 正则表达式
    python_doc = """The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""
    counter_obj = Counter(re.split('\W+', python_doc))
    # 按照非字符串(最长)的格式的进行分割.
    print(counter_obj)
    print(counter_obj.most_common(10))  # 拿到词频最大的10个单词.


if __name__ == '__main__':
    # instance_0()
    instance_1()
    instance_2()
