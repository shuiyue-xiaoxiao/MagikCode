# 1-12-1_For_vs_While
# for循环和while循环

'''
# 经典练习：从1加到100
num_sum = 0 # 将0赋值给变量num_sum (num_sum的初始和为0)
for i in range(100): # 循环100次，但是 i 的值是从 0 到 99
    num_sum = num_sum + (i + 1) # 因此从第一次循环开始，累加的值需加上一个 1，否则就成了从 0 加到 99

print(num_sum)
'''
'''
num_sum = num_sum + (i + 1)
# 第1次循环：1 = 0 + (0 + 1)
# 第2次循环：3 = 1 + (1 + 1)
# 第3次循环：6 = 3 + (2 + 1)
# 第4次循环：10 = 6 + (3 + 1)
# 第5次循环：15 = 10 + (4 + 1)
......
# 第99次循环：4950 = 4851 + (98 + 1)
# 第100次循环：5050 = 4950 + (99 + 1)
'''

# 经典练习拓展：从37加到39
num_sum = 0 # 将0赋值给变量num_sum (num_sum的初始和为0)
for i in range(3): # 循环 39-37+1 = 3次，但是 i 的值是从 0 到 2
    num_sum = num_sum + (i + 37) # 因此从第一次循环开始，累加的值需加上一个 1，否则就成了从 0 加到 99

print(num_sum)

'''
num_sum = num_sum + (i + 37)
# 第1次循环：37 = 0 + (0 + 37)
# 第2次循环：75 = 37 + (1 + 37)
# 第3次循环：114 = 75 + (2 + 37)
......

'''
