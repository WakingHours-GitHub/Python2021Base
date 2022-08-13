"""

批量修改文件名, 既可以添加指定字符串, 又能删除指定字符串.



"""


import os

# 判断是增加重命名还是删除重命名
flag = 2 # 标志位

# 找到所有文件. 然后遍历所有文件
file_list = os.listdir("test")
print(file_list)

os.chdir('test') # 改变当前工作目录, 保持一直, 否则创建或者删除文件时会报错.

for file in file_list:
    if flag == 1: # 表示批量增加名字
        new_name = 'python_' + file
    elif flag == 2:
        # 删除前缀
        num = len('python_')
        new_name = file[num: ] # 只要后面的内容

    # 重命名:
    os.rename(file, new_name)




