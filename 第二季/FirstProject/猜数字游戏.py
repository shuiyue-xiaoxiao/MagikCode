from random import randint


def guess_number():
    CN = randint(1, 100)
    i = 0

    while True:
        a = int(input("请输入一个数字："))
        i += 1  # i = i + 1

        if a == CN:
            print("恭喜你，猜对了！")
            print("你总共猜了" + str(i) + "次。")
            break

        if a > CN:
            print("太大了！")
            continue

        if a < CN:
            print("太小了！")
            continue


# ----------- 主要代码 ----------
guess_number()
# ----------- 主要代码 ----------


# 第二种写法
'''
import random
def number_right(a, b):
    if a < b:
        print("你猜的数字太小了！")
        return False
    elif a > b:
        print("你猜的数字太大了！")
        return False
    else:
        print("恭喜你！猜对了！")
        return True


b = random.randint(1, 100) # 电脑随机给出的数字
compare_results = False # 将变量 compare_results 的数据类型定义为布尔值
guess_time = 0  # 这是猜的总次数
while compare_results == False:
    a = int(input("请你输入一个数字:"))
    compare_results = number_right(a, b)
    guess_time += 1 # guess_time = guess_time + 1
print("你总共猜了" + str(guess_time) + "次")
'''