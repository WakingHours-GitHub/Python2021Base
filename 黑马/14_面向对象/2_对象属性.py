"""
添加和获取对象属性.
    特征 -> 特征, 可以添加属性, 也可可以获取属性.
    对象属性既可以在类外面添加获取, 也可以在类里面添加获取.

    分为本质属性和非本质属性.

    类外 添加对象属性
        对象.属性 = 值

    类外 获取对象属性
        对象.属性

    类里 获取对象属性
        self.属性名

"""

class Washer():
    def wash(self):
        print("洗衣服")


    def print_info(self):
        print('self.width', self.width)
        print('self.height',self.height)



haier = Washer()

# 添加实例属性: 对象.属性 = 值
haier.width = 100
haier.height = 500

# 类外获取属性
print(haier.width) # 100
print(haier.height) # 500

haier.print_info()
# self.width 100
# self.height 500
