"""
需求:
    将小于房子剩余面积的家具摆放到房子中.

步骤分析:
    涉及两个事物: 房子 和 家具, 因此有两个类.

房子类:
    属性
        房子地理位置
        房屋占地面积
        剩余面积
        房子家具列表.
    方法:
        容纳家具
    显示房屋信息

家具类:
    家具名称
    家具占地面积


"""

# 代码实现
# 家具类:
class Furniture():
    def __init__(self, name, area):
        self.name = name
        self.area = area
    def __str__(self):
        return  f'{self.name}, 占地: {self.area}'


# 房子类:
class Home():
    def __init__(self, address, area):
        self.address = address
        self.area = area
        self.free_area = area # 剩余容量
        self.furniture = list() # 家具列表.

    def add_furniture(self, item: Furniture):
        """添置家具"""
        if self.free_area >= item.area:
            self.furniture.append(item.name)
            # 减去添置的家具
            self.free_area -= item.area

        else:
            print("家具太大, 剩余面积不足, 无法容纳")
    def __str__(self):
        return f"{self.address}, 剩余容量{self.free_area}, 家具列表: {self.furniture}"



# 生成家具:
bed = Furniture("双人床", 6)
sofa = Furniture("沙发", 10)

# 房子1:

jia1 = Home("北京", 1200) # 生成对象
jia1.add_furniture(bed) # 将家具对象添加到其中
# item就是家具对象.

print(jia1)

ball = Furniture("篮球场", 2000)
jia1.add_furniture(ball) # 可见, 并没有添加到jia中
print(jia1) #




