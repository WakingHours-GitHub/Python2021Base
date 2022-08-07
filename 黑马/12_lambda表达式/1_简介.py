"""
lambda表达式的引用场景:
    如果一个函数只有一个返回值, 并且只有一句代码, 可以使用lambda简化
    一句话, lambda就是简化代码用的.

lambda语法:
    lambda 参数列表: return表达式(必须是要有返回值的)

注意:
    lambda表达式的参数可有可无, 函数的参数在lambda表达式中完全使用
    lambda表达式能够接收任何数量的参数但只能返回一个表达式的值.





"""

# lambda快速入门:

def fn1():
    return 200 # 直接返回200.


print(fn1) # <function fn1 at 0x000001C718C4F040>, 返回函数的句柄
print(fn1()) # 调用函数
# 函数名只是一个地址, 指向函数入口, 只有加上()才是待用函数



# lambda: 匿名函数, 也就是一次性函数.
fn2 = lambda : 100 # 保留函数句柄
print(fn2) # <function <lambda> at 0x000002560E064940> # 其实也就是lambda的函数地址.
print(fn2()) # 100 # 函数名()就是调用函数.
# 当函数调用时, 才能获得返回值.



# lambda计算a+b并返回结果

# 使用函数实现:
def add(a, b):
    return a + b






























