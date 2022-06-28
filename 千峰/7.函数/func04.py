# 再写一个函数: 找最大值
# 找出列表中的最大值
# 自己封装一个求取最大值的函数

def myMax(iterable):
    max = iterable[0] # 哨兵
    for i in iterable:
        if i > max:
            max = i
    print(f"函数的最大值为:{max}")

# 调用: 测试是否能找出最大值
list1 = [4,1,4,5,3,2]
myMax(list1) # 调用函数

# 试试元组
tuple1 = (3,6,4,8,9,10)
myMax(tuple1)
# 都找到了最大值, 这样我们将查找最大值的函数封装起来, 这样就提高了代码的可复用性

# 可以实现我们之前上面应用过的代码
# 例如sort  reverse  max  min

# 那么我们函数需要传入一个可迭代对象, 那么我们如何判断是否为可迭代对象呢
# 使用Type() 嘛? 其实不行, Type仅仅只是查看类型
print(type(tuple1)) # 查看是什么类型
print(type(tuple1) == "<class 'tuple'>") # False
# 当然你也可以使用str()强转, 然后比较, 但是那样就太过于麻烦

# 那么判断比较类型: isinstance(变量, 类型关键字)
# 比较:_obj是否为object类型的, 返回一个bool类型

# isinstance()函数的使用
print(isinstance(2, int)) # True # 2是int类型的吗, 是

print(isinstance(tuple1, tuple)) # True

# 于是我们就有了一个判断思路
if isinstance(tuple1, tuple): 
    print("能排序和反转")
else:
    print("不能进行排序或者翻转")

# 练习：
# sort（） reverse() 模拟这两个函数
def sort(iterable):
    for i in range(len(iterable)-1):
        min = i
        for j in range(i, len(iterable)):
            if iterable[j] < iterable[min]:
                min = j
        if i != j:
            iterable[i], iterable[min] = iterable[min], iterable[i]


if __name__ == "__main__":
    list1 = [1,3,4,56,6,2,3,1]
    sort(list1)
    print(list1)