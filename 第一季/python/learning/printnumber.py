'''
#打印1-Num数字
range(101)可以产生一个0到100的整数序列。
range(1, 100)可以产生一个1到99的整数序列。
range(1, 100, 2)可以产生一个1到99的奇数序列，其中2是步长，即数值序列的增量。
'''
Num = int(input("choose a number:"))

'''
方式一：
for i in range(Num):
    i = i + 1
    print(i)

'''

'''
方式二：
打印偶数
#(1):
for i in range(2, Num + 1, 2):
    print(i)
#(2):i = i + 1
   
'''

'''
方式二：
打印奇数
#(1):
for i in range(1, Num + 1, 2):
    print(i)
#(2):i = i + 1
   
'''

'''
方式三：
打印偶数
'''
for i in range(Num):
    if i % 2 != 0:
        print(i)
