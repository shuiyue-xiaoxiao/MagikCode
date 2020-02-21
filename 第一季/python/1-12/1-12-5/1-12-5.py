# 1-12-5_Guess_number_usdef
# 方法二：使用函数
import random
def number_right(a, b):
    if a < b:
        print("你猜的数字太小了！")
        return False
    elif a > b:
        print("你猜的数字太大了！")
        return False
    else:
        print("恭喜你，猜对了！")
        return True
    

b = random.randint(1, 100) # 电脑随机给出的数字
compare_results = False # 将变量 compare_results 的数据类型定义为布尔值
guess_number = 0 # 这是猜的总次数
while compare_results == False:
    a = int(input("请你输入一个数字："))
    compare_results = number_right(a, b)
    guess_number += 1 #  guess_number = guess_number + 1
print("你总共猜了" + str(guess_number) + "次")
