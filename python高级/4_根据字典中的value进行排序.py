"""
根据字典中的value值的大小对字典元素进行排序。


"""
import random


def instance_0() -> None:
    # 使用内置函数: sorted(iter, key, reverse) # c语言驱动, 一般最快, 内置的优化的.

    int_list = [3, 1, 5, 3, 7, 8]
    int_list.sort()  # 使用list内置的排序算法
    print(int_list)  # 会对原列表产生影响.

    res = sorted(int_list)  # 创建了一个新列表. 对原列表没有影响.
    print(res)
    print(id(res), id(int_list))  # 2337677308672 2337677087872

    student_name: list = ["古力娜扎", "马儿扎哈", "双双"]
    student: dict = {name: random.randint(40, 100) for name in student_name}
    print(student)  # 字典数据了
    # 我们没办法直接使用sorted对元组进行排序. 只能对字典的key进行排序.
    # 方式1:
    # 先转换为元组:
    # student_tuple = tuple(student.items())
    zip_obj = zip(student.values(), student.keys())
    # 注意点: value放在前面, key放在后面. 这样比较的时候先比较value在比较key
    print(list(zip_obj))
    # eval("[(95, '古力娜扎'), (58, '马儿扎哈'), (89, '双双')]")
    res1 = sorted(tuple(zip_obj))
    print(res1)


    # 方法: 直接使用sorted进行排序, 指定key属性; 默认从小到大进行排序.
    res = sorted(student.items(), key=lambda x: x[1])
    # 什么意思呢: key就是指定里面是那个对那个元素进行排序.
    # items()的一个元素就是元组, 然后按照元组索引下标为1的位置进行排序.
    print(res)

    # 从到到小. reverse=True.
    res = sorted(student.items(), key=lambda x: x[1], reverse=True)
    print(res)






if __name__ == '__main__':
    instance_0()
