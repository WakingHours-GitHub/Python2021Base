"""
面向对象的综合需求。

被考的时间和对应的地瓜状态:
    0-3分钟: 生的
    3-5分钟: 半生不熟
    5-8分钟: 熟的
    超过8分钟: 烤糊了

添加调料:
    根据用户添加对应的调料

步骤分析:
    地瓜, 地瓜类.
    属性:
        被烤的时间
        状态
        调料
    方法:
        被烤
            用户, 设定烤的时间
            修改时间状态
        添加调料
    显示对象信息 -> __str__()魔术方法



"""

# 开始书写代码.
# 定义类, 初始化属性, 烤的时间, 状态 和添加调料的方法,

class SweetPotato():
    def __init__(self):
        # 被烤的时间
        self.cook_time = 0
        # 考的状态
        self.cook_status = "row"
        # 调料列表
        self.condiments = list() # 生成空列表.

    # 定义烤地瓜的方法:
    def cook(self, time): # time就是烤的时间. 用户拿出来看一眼的时间.
        """烤地瓜的方法"""
        self.cook_time += time # 累加烤过的时间
        # 判断状态:
        if 0 <= self.cook_time < 3:
            self.cook_status = 'row'
        elif 3 <= self.cook_time < 5:
            self.cook_status = 'half ripe'
        elif 5 <= self.cook_time < 8:
            self.cook_status = 'ripe'
        elif self.cook_time >= 8:
            self.cook_status = 'over ripe'
    # 添加调料:
    def add_condiments(self, condiment):
        """添加调料"""
        self.condiments.append(condiment)

    # 书写str魔术方法: 输出用户对象状态
    def __str__(self):
        # 使用f'' 快速格式化字符串.形式.
        return f'该地瓜被烤过的时间是{self.cook_time}, 状态是{self.cook_status}, 添加的调料是{self.condiments}'

# 创建都西昂, 测试实例属性和实例方法.
# 创建对象.
digua1 = SweetPotato()
print(digua1) # 该地瓜被烤过的时间是0, 状态是row, 添加的调料是[]

digua1.add_condiments("辣椒面儿")


digua1.cook(2)
print(digua1)

digua1.add_condiments("香辣酱")

digua1.cook(2)
print(digua1)











