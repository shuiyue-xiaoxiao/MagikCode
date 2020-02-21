# 1-11-6_Eyes
# 奇异的公式！
# 椭圆形的专门练习
 
from turtle import *
 
def my_goto(x, y):
    penup()
    goto(x, y)
    pendown()
     
def eyes():
    fillcolor("#ffffff")
    begin_fill()
 
    # tracer(False) # 这两行代码是可以不要的
    a = 2.5
    for i in range(120):
        if 0 <= i < 30 or 60 <= i < 90: # 还有两个区间在下面的 else
            a -= 0.05 # a = a - 0.05
            lt(3) # 向左转3度
            fd(a) # 第一次循环的时候 a = 2.5 - 0.05
        else: # 这里包含的条件就是上面条件以外的部分：30 <= i < 60 和 90 <= i < 120
            a += 0.05 # a = a + 0.05
            lt(3)
            fd(a)
    # tracer(True) # 这两行代码是可以不要的
    end_fill()

#my_goto(63.56,218.24)
seth(90)
eyes()
# fillcolor("#FFDEAD")
# begin_fill()
# eyes()
# end_fill()
#seth(180)
#penup()
#fd(60)
#pendown()
#seth(90)
#eyes()
#penup()
#seth(180)
#fd(64)

