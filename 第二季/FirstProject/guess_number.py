from random import randint


def guess_number():
    computer_number = randint(1, 100)
    times = 0

    while True:
        input_number = int(input("请输入一个数字:\n"))
        times += 1  # times = input_number + 1

        if input_number == computer_number:
            print("恭喜你, 猜对了！")
            print("你总共猜了" + str(times) + "次。")
            break

        if input_number > computer_number:
            print("太大了！")
            continue

        if input_number < computer_number:
            print("太小了！")
            continue


guess_number()
