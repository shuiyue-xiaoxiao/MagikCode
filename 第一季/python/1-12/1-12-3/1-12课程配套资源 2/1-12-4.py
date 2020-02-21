# 1-12-4_Guess_number
# 经典猜数字


# 方法一：只用循环
import random
x = random.randint(1, 100) # 命名一个变量“电脑的数字”
i = 0
while i < 100:
    y = int(input("请输入你猜的数字:"))
    i += 1 # i = i + 1 (计算猜的次数)
    if x == y:
        print("太棒了！你猜对了！")
        print("你总共猜了" + str(i) + "次")
        break # 中断，跳出循环。
    elif y < x:
        print("太小了！")
    else:
        print("太大了！")
        

'''
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
        print("恭喜你！猜对了！")
        return True


b = random.randint(1, 100) # 电脑随机给出的数字
compare_results = False # 将变量 compare_results 的数据类型定义为布尔值
guess_number = 0  # 这是猜的总次数
while compare_results == False:
    a = int(input("plsase input number:"))
    compare_results = number_right(a, b)
    guess_number += 1
print("你总共猜了" + str(guess_number) + "次")
'''
