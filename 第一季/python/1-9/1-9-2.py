# 1-9-2 Number of loop
# 列表和循环：列表循环的次数。
# 循环的次数只和列表中的数据项/元素的数量有关，与其类型无关。

from turtle import *

'''
# 将 for 循环中的 range() 改成列表形式
for i in [1, 2, 3, 4]:# range(4)
    forward(100)
    right(90)
'''


# 试着将列表中的数据项改成任意不同数据类型的元素
# 改变后再查看结果
for i in[1, 'hello', True, 43.65]:
    forward(100)
    right(90)

# 把列表中再增加一个数据项会怎样？
for i in[1, 'hello', True, 43.65, 'hello Jason!']:
    forward(100)
    right(72)

# 把列表中再增加一个数据项会怎样？
for i in[1, 'hello', True, 43.65, 'hello Jason!',3 , 'ok']:
    forward(100)
    right(45)

# 把列表中再增加一个数据项会怎样？
for i in[1, 'hello', True, 43.65, 'hello Jason!', 'ox', 8.9608, 3543, 43, 4]:
    forward(100)
    right(40)
