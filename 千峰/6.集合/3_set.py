# 继续介绍运集合的关系运算
"""
difference_update() # 求差集并更新
    s1 = s1.difference (s2) # s1 = s1 - s2
    等价于:
    s1.difference_updata(s2) # s1 = s1 - s2

# 同理, 其他的关系运算也有同步:
set.intersection_update(set) # 取交集,并赋值(更新)
set.union_update(set) # 取并集,并赋值(给本身, 就是更新自己)
set.symmetric_difference_update(set) # 取对称差集, 并且更新 # 就是找不同的元素,然后更新
"""

l1 = [5,1,2,9,0,3]
l2 = [7,2,5,7,9]

s1 = set(l1)
s2 = set(l2)
s1.difference_update(s2) # 直接找差集, 并且同步给s1
print(s1)
# 其他函数同理


"""
总结:
    关键字: set
    作用: 去重
    声明: setObj = set() # 只能用这种方式声明集合, 因为是{单个元素}

    可以用的操作符: - & | ^
    说明:
    - difference() difference_update() 差集
    - intersection() intersection_update() 交集
    - union() union_update() 并集
    - symnetric_difference() 对称差集

    内置函数:
    增加:
    add() 增加一个元素
    update() 将一个列表或者集合添加

    删除:
    remove() 按照内容删除,如果没有该内容, 则报错
    descard() 同样是按照内容删除, 但是没有,不报错
    pop() 随机删除一个元素, 一般是最后一个
    clear() 直接清空整个列表

    运算:
    - & | ^
    差集, 交集, 并集, 对称差集
    以及他们的所对应的函数
    
    记住, 集合表示2个及以上的关系, 当需要用到关系的时候并且对象有多个时候, 我们就可以使用集合
"""

