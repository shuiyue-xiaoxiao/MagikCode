from turtle import *
# 最重要的便是递归函数：要理解科赫曲线的原理：取一段直线的1/3长度，
# 以该长度的4条小直线拼成，其中中间两条小直线凸起（60度）
# 以此类推，每条小直线再接着细分
speed(8)
def koch(size,n):
    if n==0:
        fd(size)
    else:
        for angel in [0,60,-120,60]:
            left(angel)
            koch(size/3,n-1)
# 上面函数：在最外层的循环执行转角度后再调用下一阶及相应的直线长度（0、60、-120、60）
# 这些角度都是并列关系，每一层又包含着调用递归也是这四个角度
# 其实最里面的递归调用效果就是把每个小直线分成四段，中间突起
# 下面函数后面的代码是形成一个大三角，把每个边绘制成科赫曲线，三角形三个边通过角度进行转换连接
def main():
    setup(600,600)
    penup()
    goto(-200,100)
    pendown()
    pensize(2)
    level=3
    koch(400,level)
    right(120)
    koch(400,level)
    right(120)
    koch(400,level)
    hideturtle()
main()
