# 1-12-4 Guess Number
# 经典猜数字


# 方法1:只用循环
import random
x = random.randint(1, 100)
i = 0
while i < 100:
    y = int(input("请输入你猜的数字"))
    i += 1 # i = i + 1(计算机猜的次数)
    if x == y:
        print("太棒了，你猜对了！")
        print("你总共猜了" + str(i) + "次")
        break # 中断，跳出循环
    elif y < x:
        print("太小了！")
    else:
        print("太大了！")
        
