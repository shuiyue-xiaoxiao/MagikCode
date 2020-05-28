import random

# 引入随机数模块。
print("-----猜数字游戏-----")

print("-----请猜出电脑产生的一个随机数范围(1~49)-----")

answer = random.randint(1, 49)
# 系统产生随机数并保存到answer变量中。
n = int(input("请输入一个数(1~49)"))
# 将用户输入的数保存到n变量中。
while n != answer:  # 条件成立进入while循环中，条件不成立跳出循环

    if n > answer:

        print("你输入的数大了！")

        n = int(input("请重新输入"))

    else:
        print("你输入的数小了")

        n = int(input("请重新输入"))

print("恭喜你才对了，电脑产生的随机数是%d" % n)
