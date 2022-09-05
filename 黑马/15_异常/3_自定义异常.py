"""
自定义异常, 我们可以自定义异常类, 然后抛出异常
python中抛出异常的语法: raise 异常类对象.


需求:
    密码长度不足, 则报异常

自定义异常可以帮助我们去报错, 如果程序不满足逻辑异常时,
我们可以设定自定义异常来捕获该异常信息.




"""


# 自定义异常类, 继承Exception. 异常类最终的父类都是Exception类.
class ShortInputError(Exception):
    def __init__(self, length, min_len):
        # 留出接口, 方便后续修改.
        self.length = length
        self.min_len = min_len

    # 设置异常信息
    def __str__(self):
        return f"input char length: {self.length}, at least need:{self.min_len} char"


def main():
    try:
        content = input("please input passwd: ")
        if len(content) < 3:  # 最少密码长度
            # 抛出异常对象, 这里就是抛出了对象.
            raise ShortInputError(len(content), 3)
    except Exception as result:  # 打印详细信息
        print(result)  # 打印的就是__str__()这样就可以设置异常信息了.
    else: # 如果没有异常的时候, 则打印密码.
        print("complete passwd input")


if __name__ == '__main__':
    main()
