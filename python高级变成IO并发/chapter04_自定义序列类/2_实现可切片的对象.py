# 模式[start: end: step]
"""
其中, 第一个数字start表示切片开始位置, 默认为0
第二个数字end表示切片戒指(但不包含)位置.
第三个数字step表示切片的步长(默认为1)
当start为0时可以省略, 当end为列表长度时可以省略,
当step为1时可以省略, 省略时可以省略最后一个冒号.
另外, 当step为负整数时, 表示反向切片, 这是start应该比end的值大才行.


切片操作是会返回一个新的列表的. 不会改变原来的list


"""
import numbers


def slice_test():
    aList = list(range(20))
    aList[::]  # 返回包含原列表中所有元素的新列表.
    aList[::-1]  # 返回包含原列表中所有元素的逆序列表

    aList[len(aList):] = [9]  # 在列表尾部增加元素.
    aList[: 0] = [1, 2]  # 在列表头部插入元素.
    # 实际上就是: aList = [1, 2] + aList一样的效果.

    aList[3:3] = [4]  # 实际上实在列表index=3中插入元素.
    aList[: 3] = [1, 2]  # 替换列表元素, 等号两边列表元素相等.
    aList[3:] = [4, 5, 6]  # 等号两边的列表长度可以不相等.
    aList[::2] = [0] * 3  # 隔一个修改一个.
    # alist[::2] = [0, 0, 0] # 个数要相同.

    del aList[: 3]  # 删除切片元素


# 上面我们看到了切片的功能
# 下面我们自己实现一个我们自己的对象支持如此灵活的切片对象


class Group:  # 组的概念
    # 支持切片操作.
    def __init__(self, group_name, company_name, staffs):
        self.group_name = group_name
        self.company_name = company_name
        self.staffs = staffs

    # 这些协议, 来自 Sequence这个基类.
    def __reversed__(self):
        self.staffs.reverse()

    def __getitem__(self, item):  # 实现切片的关键.
        # 这个item的类型:(int, slice).
        # print(item) # slice(0, 2, None) # 实际上就是一个slice对象.
        cls = type(self) # 软编码. 相对的.

        # 返回cls创建的对象.
        if isinstance(item, slice):
            return cls(group_name=self.group_name, company_name=self.company_name, staffs=self.staffs[item])

        elif isinstance(item, numbers.Integral):
            return cls(group_name=self.group_name, company_name=self.company_name, staffs=[self.staffs[item]])

        # return self.staffs[item] #

        pass

    def __len__(self):
        return len(self.staffs)

    def __iter__(self):
        return iter(self.staffs) # 这节课先不讲.

    def __contains__(self, item):
        if item in self.staffs:
            return True
        else:
            return False


def main() -> None:
    staffs = ["1", '2', '3', '4', '5']
    g = Group(group_name="user", company_name="imooc", staffs=staffs)
    print(g[0:2]) # 所以返回的还是一个group对象

    print("1" in g) # True, 实际上就是调用了__contains__方法.

    for user in g:
        print(user) # 调用了iter.

    reversed(g)
    print(g.staffs) # ['5', '4', '3', '2', '1'] # reversed了.



if __name__ == '__main__':
    main()
