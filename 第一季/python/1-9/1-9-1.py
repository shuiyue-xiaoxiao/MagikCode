# 1-9-1 list and loop
# 列表和循环：在 python turtle 里的应用


# 回顾开头两个语句：
'''
from turtle import *

import turtle
'''


from turtle import *

'''
# 课程回顾：1-4-1 最简洁的正方形：

for i in range(4):
    forward(100)
    right(90)
'''

# 将 for 循环中的 range() 改成列表
for i in [1, 2, 3, 4]:
    forward(100)
    right(90)

