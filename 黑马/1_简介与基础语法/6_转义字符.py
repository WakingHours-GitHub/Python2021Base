"""

'\'这种符号, 我们称之为反斜杠
'/'这种斜杠称之为斜杠
\n: 表示换行符
\t: 表示制表符, 有的地方表示固定间隔的位置

为什么print()默认是另起一行呢? 实际上是以print默认结束符有关.

print()函数的两个常用参数
    sqp: 表示多个打印变量的间隔符, 默认为','
    end: 表示结尾的结束符. 默认为'\n'

用户可以任意指定这两个参数
"""
print("test", sep=",", end="\n")
print("Print_end", end=">>>")
print("Python")

