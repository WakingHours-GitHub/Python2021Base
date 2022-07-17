"""
while遍历列表 -> 适用于需要修改列表时候
for遍历列表 -> 适用于遍历

"""

# while遍历:
name_list = ['tom', 'lilt', 'rose']
i = 0
while i < len(name_list):
    print(name_list[i])
    i += 1



# for遍历:
for ele in name_list:
    print(ele)

