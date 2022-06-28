# 案例与总结

# break案例
for i in range(3):
    if i == 1:
        print('黑店')
        break # 跳出循环
        # break后面的语句，不会执行，也不会引发语法错误
    else:
        print('真好吃')
        

# 总结

'''
总结:

range()

range(m)
range(n,m)
range(n,m,step)

         0,1,2...n-1
for i in raneg(n): # 循环n次
    # 语句
    或者 pass

for i in 集合:
    pass
else:
    pass

break, pass
break 用于跳出循环
pass 用于在缩进中占位

'''