from random import randint
from tkinter.messagebox import askquestion
from turtle import *


def Guess_number():
    pen_goto = -250, -150
    computer_number = randint(1, 100)
    times = 0
    my_font = ('Ariel', 25, 'normal')
    while True:
        input_number = numinput('Guess number', 'Please enter Numbers from 1 to 100')
        times = times + 1
        if input_number == computer_number:
            clear()
            goto(pen_goto)
            write('恭喜你，猜对了！你总共猜了' + str(times) +
                  '答案是:' + str(int(computer_number)),
                  font=my_font)
            break

        if not input_number:
            clear()
            goto(pen_goto)
            result = askquestion(title='message', message='ARE YOU SURE TO CANCEL?')
            if result == 'yes':
                write('你放弃了，游戏结束(答案是：' + str(int(computer_number)) + '）', font=my_font)
                break
            else:
                continue

        if 0 < input_number - computer_number <= 20:
            clear()
            goto(pen_goto)
            write('大了一点，已经很接近了，加油！！💪',
                  font=my_font)
            continue

        if input_number - computer_number > 21:
            clear()
            goto(pen_goto)
            write('太大了吧！对了才怪😜',
                  font=my_font)
            continue

        if 0 < computer_number - input_number <= 20:
            clear()
            goto(pen_goto)
            write('小了一点，已经很接近了，加油！！💪',
                  font=my_font)
            continue

        if computer_number - input_number >= 21:
            clear()
            goto(pen_goto)
            write('太小了吧！对了才怪😜',
                  font=my_font)
            continue


def main():
    title(textinput('window', 'Please enter your title'))
    setup(800, 600)
    hideturtle()
    pencolor('green')
    penup()
    goto(-250, -150)
    my_font = ('Ariel', 25, 'normal')
    write('I came up with the number 1 to 100, please guess！', font=my_font)
    Guess_number()


if __name__ == '__main__':
    main()
    mainloop()
