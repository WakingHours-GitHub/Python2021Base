"""
字符串常用函数：
如何学习： 函数名字, 函数功能, 函数参数, 函数返回值.

查找:
    所谓字符串查找就是字串在字符串中的位置或者出现的次数.

    find(): 检查某个字串是否包含在这个字符串中, 如果在, 返回第一次字串开始的位置下标, 否则返回-1
        语法: str.find(subStr, startIndex, endIndex)
        开始, 结束下标可以省略, 表示在整个字符串序列中查找.

    rfind(): 和find()功能相同, 但是查找方向从右侧开始, 返回第一个字串开始的位置.



    index(): 用法与find()相同,
        只不过找不到字串则报错.

    rindex()和index()功能相同, 从右侧开始查找

    count(): 返回某个⼦串在字符串中出现的次数
        语法: str.count(subStr: str, start, end)


修改: 所谓修改字符串, 值得就是通过函数, 去修改字符串中的数据
    replace(): 替换, 不会对原字符串修改, 而是返回新的字符串
        new_str = str.replace(oldStr, newStr, num)
        replace(旧字串, 新字串, 替换次数)
        从左往右开始替换, 替换次数可以省略, 表示全部替换.

    说明:
    replace()有返回值, 不修改原来的字符串, 返回新的字符串
        说明, str是不可变类型, 对其操作, 是返回新的str, 而不是对原有的str进行修改
        而列表, 字典, 对其进行操作, 直接修改的是原来的数据, 这种数据就称之为可变数据类型.

    split(): 按照指定字符串分割字符串, 返回一个list
        list = str.split(分割字符, num)
            num表示分割字符出现的次数, 即返回列表中元素的个数为num+1个
            丢失分割字符, 只有分割字符两边.

    join(): 合并列表中的字符串, 返回一个组合好的字符串
        new_str = "拼接字符".join(列表)

    其他修改函数:
    capitalize(): 将字符串第一个字母转换为大写, 其他字符全为小写, 符合capitalize规范
    title(): 将字符串每个单词首字母转换大写, 符合title格式
    lower(): 将字符串中大写转换为小写
    upper(): 将字符串中小写转换为的大写


    删除首尾特定字符:
        str.strip(需要去除的字符串): 去除开头和结尾的子字符串
        str.strip(): 默认情况下, 首尾均去除空白空格, 包括\t, \n 空格.

    设置字符串对齐.


    判断相关的字符串函数: 返回True, False
        str.startwith(字串, 开始位置下标, 结束位置下标)
        判断给定范围的字符串是否以 字串 开头.
        开始和结束可以省略, 表示从头到尾

        str.endwith(字串, 开始位置下标, 结束位置下标)
        判断给定范围的字符串是否以 字串 结尾.

        str.isalpha(): 检查是否为字母 字母字符串.
        如果字符串至少有一个字符并且所有字符都是字母则返回True, 否则返回False









"""
myStr = "Hello World and itcast and itheima and python"

# 1. find()
print(myStr.find("and"))  # 12 # 返回第一个字串开始的下标.
print(myStr[myStr.find("and")]) # a, 就是第一个开始的下标.
# 通过指定start, end来确定搜索范围.
print(myStr.find("and", 15, 30)) # 23 #
print(myStr.find("lipu")) # -1 # 没有找到就返回-1. lipu字串不存在

# 2. index()
# 用法与find()相同, 只不过找不到字串则报错.
print(myStr.index("and"))
print(myStr.index("and", 15, 30))
# myStr.index("lipu") # 如果index查找字串不存在, 是会报错的.
# ValueError: substring not found


# 3. count()
print(myStr.count("and")) # 3 # and在字符串中出现了三次.
print(myStr.count("lipu")) # 0, 0就表示没有找到.

# 4. rfind()
print(myStr.rfind("and")) # 35 # 从右侧开始找第一次出现的字串.

# 5. rindex()



# replace(), 原来字符串不发生改变, 返回修改过后的str.
new_str = myStr.replace("and", "he")
print(new_str) # Hello World he itcast he itheima he python
print(myStr) # Hello World and itcast and itheima and python
print(myStr.replace("and", "he", 1)) # Hello World he itcast and itheima and python

# 2. split(): 分割, 返回一个列表
list1 = myStr.split("and")
print(list1) # ['Hello World ', ' itcast ', ' itheima ', ' python'] # 4个

list1 = myStr.split("and", 2)
print(list1) # ['Hello World ', ' itcast ', ' itheima and python'] # 3个

# 3. join(): 合并列表中的字符串, 返回一个组合好的字符串
# 使用拼接字符串, 将列表中的字符串数据进行拼接.
mylist = ['a', 'b', 'c']
new_str = '...'.join(mylist)
print(new_str)  # a...b...c


# 字符串大小写相关函数

my_str = "hello World And itcast and itheima and python"
new_str = my_str.capitalize()
print(new_str) # Hello world and itcast and itheima and python
# 可见, 将首字母进行大写. 并且后面字符均为小写, 符合cap规范.



