# 实现可迭代对象与迭代器对象.
# 如果一次抓取所有的城市天气信息, 显示一个城市气温则会有很高的延迟, 并且浪费空间.
# 我们期望使用"用时访问"的策略来完成功能. 将所有的城市信息封装到一个对象当中, 并且能够使用for循环迭代.


"""
可迭代对象: iterable.
    例如, 列表, 字符串, 都是可以通过for循环进行迭代的.
    python是如何区分出一个对象是否是可迭代对象呢?
    看一个对象的底层是否有__iter__()

    python判断对象底层是否有__iter__()方法, 如果有这个属性, 则说明这个对象是可以被迭代的.

迭代器对象:
    主要职责是定义循环迭代的规则.
    如果一个对象的底层有__next__()方法的话, 则说明这个对象是一个迭代器对象. __next__方法主要负责迭代规则.
    通过iter()将一个可迭代对象转换为迭代器对象.





"""

import requests
import json, jsonpath
from collections.abc import Iterable, Iterator  # 分别导入可迭代对象类, 以及迭代器类.


# 自定义迭代器类
class WeatherIterator(Iterator):
    def __init__(self, cities):
        self.cities = cities
        self.index = 0  # 初始索引.

    def get_weather(self, city: str) -> str:
        resp = requests.get(
            f'https://v0.yiketianqi.com/api?unescape=1&version=v91&appid=43656176&appsecret=I42og6Lm&ext=&cityid=&city={city}')
        # print(resp.text)  # city的json格式.
        resp_dict = json.loads(resp.text)
        # print(f'{resp_dict["city"]}: {resp_dict["data"][0]["tem1"]}-{resp_dict["data"][0]["tem2"]}')
        return f'{resp_dict["city"]}: {resp_dict["data"][0]["tem1"]}-{resp_dict["data"][0]["tem2"]}'

    # 需要定义城市的循环规则: 需要重写__next__()方法.
    def __next__(self):
        if self.index == len(self.cities):  # 已经列表越界了.
            raise StopIteration  # 抛出错误
        city = self.cities[self.index]
        self.index += 1
        return self.get_weather(city)


# 自定义可迭代对象类:
class WeatherIterable(Iterable):  # 自定义可迭代对象类.
    def __init__(self, cites):
        self.cities = cites

    # 这是内置的迭代函数, 使用for循环中, 每次调用一次.
    # 需要再自定义可迭代对象中返回一个迭代器的实例. 需要返回迭代器对象, 也就是要有__next__()函数.
    def __iter__(self):
        return WeatherIterator(self.cities)


def main() -> None:
    my_iterable = WeatherIterable(["北京", "上海", "深圳", "长沙"])  # 返回迭代器对象.
    for i in my_iterable.__iter__():
        print(i)


if __name__ == '__main__':
    main()
