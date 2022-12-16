
"""

property.deleter装饰器
有人想要删除这个属性时, 我们做什么. 就用这个装饰器.

"""


class Square:

    def __init__(self, width):
        self.__width = width
        self.__area = None

    @property
    def width(self):
        return self.__width


    @width.setter
    def width(self, width):
        if width < 0:
            raise Exception(f"width can't a negative number")
        self.__width = width # 赋值
        self.__area = None # 更新值后, 我们reset的area, 这样提高速度.

    @property
    def area(self):  # 计算面积, 实际上没有真实的属性对应, 而只是一种设计. 通过计算出来的.
        if self.__area is None: # 缓存, 提高性能速度.
            self.__area = self.__width ** 2
        return self.__area

    @area.deleter
    def area(self):
        del self.__area

def main():
    square = Square(5)
    print(square.area)  # 25.
    square.width = 9

    # del square.area
    print(square.area)  # 25.



if __name__ == '__main__':
    main()
