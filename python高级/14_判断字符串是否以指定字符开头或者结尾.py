# 判断字符串是否以指定字符开头或结尾.

# 使用startswith()和endswith()方法, 一个判断开头, 一个判断结尾. 返回bool类型.
# 如果需要判断多个字符串, 则使用一个元组包裹起来.

import os

code = ['a.sh', 'b.java', 'c.cpp', 'd.go', 'e.py']

# 让.sh和.py文件具有可执行权限.
print([codename for codename in code if codename.endswith((".sh", ".py"))])
# ['a.sh', 'e.py']



