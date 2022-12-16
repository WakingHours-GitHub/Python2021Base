"""


只读property.
就是当我们是通过计算得到的"属性"
我们就可以使用property
将一些方法, 用"属性"进行展现.
这是不同的设计模式.

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


def main():
    square = Square(5)

    square.width = 9
    print(square.area)  # 25. 这就是只读property. # 81



if __name__ == '__main__':
    main()
