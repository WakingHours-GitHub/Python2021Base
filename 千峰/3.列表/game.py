## 综合案例: 游戏:
'''
游戏功能:
1.选择人物
2.可以使用金币购买武器
3.可以进行对战,  可以赢得金币
4.可以选择删除武器, 返还金币
5.可以查看武器
6.退出游戏

'''
import random

# menu菜单界面
print('#'*30)
print('#\t  欢迎进入游戏\t     #')
print('#'*30)

if input('开始游戏(y/n)') == 'y':
    print('!!!进入游戏!!!')
    role = input('请选择你的游戏人物[1.马儿扎哈 2.后裔 3.李白 4.韩信 5.貂蝉 6.诸葛亮]')
    coins = 1000 # 初始金币
    my_weapon = [] # 初始武器
    print(f'欢迎{role}进入游戏,初始金币:{coins}没有武器') # f'{}...'

    while True:
        choice = int(input('''
        请选择:
            1.购买武器
            2.攻击
            3.卖掉武器
            4.查看当前武器
            5.退出游戏
            '''
        ))
        # 开始进行判断选择
        if choice == 1: # 购买武器
            # pass
            print('欢迎来到购买武器界面')
            weapons = [['三相之力',500],['樱花枪', 400],['98K狙击枪',900,],['手榴弹',800],['饮血剑', 300],['大刀',100]]
            # 打印武器列表:
            for weapon in weapons:
                print(f"武器: {weapon[0]}     \t金额: {weapon[1]}")
            weapon_name = input("请输入您要购买的武器:")
            jdage = 'y'
            while jdage == 'y':
            # 判断金币是否够, 并且判断是否已经购买
                if weapon_name not in my_weapon: # 没有购买过武器
                    # 输入的武器是否在列表里面,并且金币需要大于金额
                    for weapon in weapons:
                        if weapon_name == weapon[0]: # 说明存在
                            # 是否可以购买
                            if coins >= weapon[1]: # 大于, 可以购买
                                my_weapon.append(weapon[0])
                                coins -= weapon[1]
                                print(f"[{weapon[0]}]购买成功")
                                jdage = 'n'
                                break
                            else:
                                print('金币不足, 可以通过打怪赚取金币')
                                jdage = 'n'
                                break
                    else:
                        jdage = input('没有您输入的武器, 是否要重新输入(y/n)')
                        if jdage == 'n':
                            break
                        weapon_name = input("请重新输入您要购买的武器:")
                else:
                    jdage = input('您已经拥有该武器, 是否要继续购买其他武器?(y/n)')
                    if jdage == 'n':
                        break
                    weapon_name = input("请重新输入您要购买的武器:")
        elif choice == 2: # 进攻
            pass
        elif choice ==32:
            pass
        elif choice == 4:
            pass
        elif choice == 5:
            pass
        else:
            pass
        


else:
    print('退出游戏')