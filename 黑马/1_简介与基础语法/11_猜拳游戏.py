"""
游戏玩家:
    玩家和电脑

    玩家: 手动出拳
    电脑: 随机出拳
        我们先做电脑固定出拳,
        然后引入随机性质

判断输赢.
    玩家获胜
    平局
    电脑获胜

引入随机数功能:
import 模块名
然后使用random模块中的随机整数功能
random.randint(a, b) # 生成一个[a, b]返回内的伪随机整数

步骤: 导入模块, 然后使用模块




"""
# 导入模块
import random


# 1. 出拳
player = eval(input("请输入猜拳: 0-石头, 1-剪刀, 2-布子: "))
computer = random.randint(0, 2)  # 随机数
print(computer)

# 2. 判断输赢:
if (player==0 and computer==1) or (player==1 and computer==2) or (player==2 and computer==0):
    print("玩家胜利")
elif player == computer:
    print("平局")
else:
    print("电脑胜利")


# 优化: 判断输赢
# print(player + 1 % 3)
if player+1 % 3 == computer: # 优化玩家胜利的判断情况.
    print("玩家胜利")


































