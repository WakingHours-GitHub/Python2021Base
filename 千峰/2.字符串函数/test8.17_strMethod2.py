# 查找，替换相关的函数
# 函数：
# find(): find(str, beg=0, end=len(string))返回的是索引（位置）, start,end可以规定在指定区间内查找,查找失败返回-1
# rfind(): 从左侧开始查找
# lfind(): 从右侧开始查找(常用)
# index(): index(str, beg=0, end=len(string))   index与find方法一样, 只不过index找不到会直接报错
# rindex(): 从左边index
# lindex()   
# replace():  replace(old, new [, max]) 替换,.中找old然后替换成new,可选参数:指定次数


# 使用函数:
s1 = 'index lucy lucky goods'

# in操作符, 看字符串是否在目标字符串里, 返回True和Flase
result = 'R' in s1
print(result)  # Flase

# find(str, beg=0, end=len(string))返回的是索引（位置）,还可以指定start和end
# 查找失败则返回-1
position = s1.find('l')  # 如果可以找到则返回该自第一次出现的索引（位置）
print(position)  # 6

# 带多参数的find('找找的字串', 'start', 'end') 即可以指定查找的区间
p = s1.find('o', position + 1, len(s1) - 5)  #
print(p)  # -1

'''
开发场景:
我们想从一大堆文件中提取出我们想要的格式或者文本
例如: 一个图片的网址,我们想单独得到他的图片名字
'''
# https://www.baidu.com/img/bd_logo1.png
url = '# https://www.baidu.com/img/bd_logo1.png'

p = url.find('/')  # find()函数只能返回从左到右的第一个'/'的位置
print(p)  # 8
# 所有就有了rfind()和lfind() ,一个从右开始搜索, 一个从左开始搜索

p = url.rfind('/')  # 从right右开始查找, 返回'\'处的索引
print(p)  # 27

filename = url[p + 1:]  # 从找到的/+1,到最后就是图片的文件名
print(filename)  # bd_logo1.png

# 提取文件拓展名
p = url.rfind('.')
kuozhan = url[p + 1:]
print(kuozhan)  # png

'''
find(str, beg=0, end = len(string))
而index(str, beg=0, end=len(string))
根find()方法一样,都是从左到右找str, 只不过index如果str不存在字符串中会报一个异常
而find()找不到str则返回-1

p = 'hello'.index('x')s
print(p)

ValueError: substring not found # 变量错误: 字串没有找到

'''

# 有查找就有替换: replace: 取代;替换
# replace(old, new, [, max]) # 将old替换成new,可指定替换次数,最大不找过max次

s1 = 'index lucy lucky goods'

s2 = s1.replace(' ', '#')  # 将空格,全体换为#
print(s2)  # index#lucy#lucky#goods

s2 = s1.replace(' ', '')  # 将空格替换为空, 即去空格
print(s2)  # indexlucyluckygoods

s2 = s1.replace(' ', '', 2)  # 从左到右,将空格替换为空, 替换两次
print(s2)  # indexlucylucky goods

# 字符串你内建函数:
# edcode 编码   decode 解码
# 开发场景: 网络应用
'''
例如在百度时:汉字是如何存储的,其实汉字在网络应用中是作为一种字节码展示的
复制带中文的链接所显示的一些内容
https://www.baidu.com/s?wd=%E4%BB%8A%E6%97%A5%E6%96%B0%E9%B2%9C%E4%BA%8B&tn=SE_PclogoS_8whnvm25&sa=ire_dl_gh_logo&rsv_dl=igh_logo_pcs
wd = %E4%BB%8A%E6%97%A5%E6%96%B0%E9%B2%9C%E4%BA%8B # 这其实就是编码

所以介绍encode函数
encode(encoding='UTF-8',errors='strict')
以 encoding 指定的编码格式编码字符串，如果出错默认报一个ValueError 的异常，除非 errors 指定的是'ignore'或者'replace'

'''
# 几种编码形式: gbk 中文    gbk2312 简体中文    unicode万国码
msg = '上课! 开始认真听课!'

result = msg.encode('utf-8')
print(result)  # 一大堆中文对应的utf-8的字节码, 这其实就是将msg(中文),编码了(前面标了一个b)
# 这就可以将中文,转换成在网络上传输的编码了. 那么我把消费发给你, 你还需要解码,也是decode
# 那么我想看到你给我发的信息, 你用什么解码, 就用什么解码

# 此时result是一个字节码字符串,字节,decode
m = result.decode('utf-8')
print(m)  # '上课! 开始认真听课!' 这解码成了就是原来的msg中文

# 其他的字符串内建函数:
# starstwith()   endswith()   返回值都是布尔类型True  False
# startswish() 判断是否是以xxx开头的
# endswith() 判断是否以xxx结尾的

# 开发场景
# 应用: 文件上传 只能上传特定格式的文件(后缀名)
# 例如:只能上传图片, 以(jpg, png, bmp, gif)等结尾

filename = '笔记.doc'
result = filename.endswith('doc')  # filename是否以doc结尾的?
print(result)  # True

result = filename.endswith('txt')  # filename是否以txt结尾的
print(result)  # False

s = 'hello'
result = s.startswith('H')  # 判断s是否以'H'开头
print(result)  # False

result = s.startswith('he')  # 判断s是否以'he'开头
print(result)  # True

# 案例: 建议模拟文件上传  只能上传图片(jpg, png, bmp, gif)

path = input('请选择文件')  # C:\foo\bar\desk_background.jpg
# 分析: 要上传的顶文件路径:path->文件名->通过文件再判断是否特定类型
index = path.rfind('\\')  # 从右往左找'\'
filename = path[index + 1:]  # 从'\'后面一个字符到最后,就是文件名字
# 判断是否是图片类型
# 这个地方我们要写很长的表达式判断语句, 但是当我们学完正则表达式后就可以简化了
if filename.endswith('jpg') or filename.endswith('png') or filename.endswith('bmp'):
    print('上传成功')
else:
    print('不是图片类型, 所以上传失败')


# 然后这里有一个注意事项:
# 就是再\后面必须跟一个其他字符,否则就会报错
# 例如:
# print('ask\') # 报错, 因为\'是会被识别成转义字符, 此时就没有另一个'与之对应了, 自然会报错



'''
练习：
给定一个路径, 上传文件(记事本txt或者是图片jpg, png)
如果不是对应格式的, 允许重新指定上传文件
如果符合上传的规定则提示上传成功

'''
while True:
    path = input('请输入路径: ')
    index = path.rfind('\\') # 从右到左查找\的index
    filename = path[index + 1: ] # 获取文件名字

    if filename.endswith('jpg') or filename.endswith('png') or filename.endswith('txt'):
        print('允许上传, 成功!')
        break
    else:
        print('不符合图片格式和记事本格式, 上传错误!')











