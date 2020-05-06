from random import randint
from turtle import *


def guess_number():
    computer_number = randint(1, 100)
    times = 0
    my_font = ('Ariel', 22, 'normal')

    while True:
        input_number = numinput('猜数字游戏', "请输入1～100的数字:")
        times += 1  # times = input_number + 1

        if input_number == computer_number:
            clear()
            write("恭喜你, 猜对了！" + "你总共猜了" + str(times) + "次。答案是：" + str(int(computer_number)), font=my_font)
            break

        if not input_number:
            clear()
            write('你放弃了，游戏结束(答案是：' + str(int(computer_number)) + '）', font=my_font)
            break

        if input_number > computer_number:
            clear()
            write(str(input_number) + " 太大了！", font=my_font)
            continue

        if input_number < computer_number:
            clear()
            write("太小了！", font=my_font)
            continue


def main():
    title(textinput('title', '请输入标题 '))
    setup(600, 400)
    hideturtle()
    pencolor('blue')
    penup()
    goto(-250, -50)
    my_font = ('Ariel', 22, 'normal')
    write('我想到了1～100的数字， 请你猜猜看吧！', font=my_font)
    guess_number()


if __name__ == '__main__':
    main()
    mainloop()
