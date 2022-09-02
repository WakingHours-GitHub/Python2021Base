"""
目标:
    了解异常
    捕获异常
    异常的else
    异常finally
    异常的传递
    自定义异常

了解异常:
    异常就是运行时产生的bug
捕获异常就是, 将可能会出现bug的代码放到一个try中去执行, 可能会出现bug.
然后我们捕获bug, 进行处理, 从而不让程序中断, 继续运行.

捕获异常的写法:
    try:
        可能发生错误的代码
    except:
        如果出现异常执行的代码

    捕获指定异常:
    try:
        可能发生错误的代码
    except 异常类型:
        捕获到该类型异常后执行的代码
    except ...:
    ...
    这种写法, 只会捕获特定异常类型, 从而执行特定异常类型的代码.
    一般try下方, 只放一行尝试执行的代码.
    异常类型, 就是异常类, 每个异常都对应一个异常类.
    在拨错中, 我们就可以看到是哪个异常类

    捕获多个异常 -> 你不确定异常到底是哪一个时, 就需要这种形式
    except (异常类1, 异常类2, ...) as 别名:

    捕获异常描述信息:
        异常描述信息. 其实就是捕获异常后面的信息说明, 这样可以让我们更加清晰我们的错误描述.
        因此异常描述信息, 就是描述异常详细信息, 帮助我们了解异常发生的详细信息.

    捕获所有异常:
        Exception是所有程序异常类的父类. 结合多态的知识. 因此我们需要将所有异常类
        因此, 捕获所有异常, 就是捕获所有类的父类, 然后这个异常类由于多态, 其实就是子类.


    异常中的else:
        else表示如果没有异常, 那么要执行的代码

    异常当中的finally:
        finally代码块: 表示无论是否出现异常, 最终(最后)都要执行的代码.
        例如关闭文件流, 释放资源等操作上.


"""

try:
    # 可能报错的代码.
    open("test.txt", 'r').close()
except:
    # 出现异常执行的代码
    open("test.txt", 'w').close()


# 不同的异常, 有不同的异常类.
# print(num) # NameError: name 'num' is not defined
# print(1/0) # ZeroDivisionError: division by zero

# 因此我们需要捕获不同的异常值:
try:
    # print(num)
    print(1 / 0)
except NameError:
    print(NameError)
except ZeroDivisionError:
    print(ZeroDivisionError)
# 可见, 特定异常的捕获, 只能捕获到特定的异常类.
# 其他类型的异常类的处理代码不执行.

# 捕获多组异常.
# 当你不确定异常类型是什么类型时, 就可以使用捕捉多组异常类型.
try:
    print(num)
    print(1/0)
except (NameError, ZeroDivisionError) as error: # as捕获异常信息.
    # as后面是一个关键字, 用来显示异常信息
    print("error")
    # 打印异常信息.
    print(error) # name 'num' is not defined




# 捕获所有异常, 在不知道所写代码可能会报什么类型的异常时使用
try:
    print(num)
    print(2 / 0)
except Exception as error_info:
    # 打印具体的异常信息.
    print(error_info) # 这是多态的结果.


# 异常的else:
try:
    print(1)
except Exception as error:
    print(error_info)
else:
    print("没有发生错误")




