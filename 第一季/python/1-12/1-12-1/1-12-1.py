# 1-12-1 for 38 to 100
# 精典练习：从 38 加到 100

numSum = 0 # 将 0 赋值给变量 numSum (numSum的初始和为 0 )

for i in range(38, 101): # 循环63次，但是 i 的值是从 0 到 62
    
    numSum = numSum + i # 因此从第一次循环开始，累加的值需加上一个 1 ，否则就成了从 0 加到 99。

print(numSum)
'''

# sum = 1 + 2 + 3 + 4 + 5


sum = 0

for i in range(1, 6):
    sum = sum + i

print(sum)
'''
