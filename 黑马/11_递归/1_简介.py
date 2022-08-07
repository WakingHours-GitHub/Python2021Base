"""
递归的应用场景：
    递归是一种编程思想, 是函数式编程的体现:
    便利文件夹, 及其下面的所有文件, 通常会使用递归来实现
    在后续的算法课程中, 很多算法都离不开递归, 例如快速排序

递归的特点:
    函数内部自己调用自己, 并且每次需要将'规模'减小
    必须有出口.

"""


# 回顾返回值的知识点
def return_num():
    return 100  # 只有调用的时候, 才能得到返回值100


result = return_num()  # return返回值返回到函数调用该的位置.
print(result)


# 3以内数字累加和. -> 3 + 2 + 1
# 3的累加和=3 + 2以内的累加和
# 2累加和=2+1的累加和
# 1的累加和=1 -> 出口,
#
# 递归特点: 函数内部自己调用自己: 必须要有出口

def sum_numbers(num):
    # 当前数字 + 当前数字-1的累加和
    if num != 1:
        return num + sum_numbers(num - 1)  # num + num-1的累加和
    else:  # 出口 当num==1时, 返回1
        return 1


print(sum_numbers(3))  # 6 正确的.
# 每次调用函数时, 程序就会保留当前状态, 然后将函数入栈,又有函数时, 函数再次入栈
# 然后当函数执行完毕后, 函数弹栈, 将返回值返还给调用处.

# 如果递归没有出口. 一直递归, 那么程序就会报错, 超出最大深度
# 其实也就是StackOverflow, 堆栈内存溢出


def recursion():
    recursion()

recursion() # RecursionError: maximum recursion depth exceeded
# 递归错误, 超过了最大递归深度.