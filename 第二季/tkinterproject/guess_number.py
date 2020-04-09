from tkinter import *
from tkinter.messagebox import *
from random import randint

window = Tk()
window.title('guess_number')
window.geometry('400x300+1000+150')

input_number = IntVar()
CN = randint(1, 100)
i = 0


def guess_number():
    global i
    a = input_number.get()
    i += 1  # i = i + 1

    if a == CN:
        showinfo(message="恭喜你，猜对了！")
        showinfo(message="你总共猜了" + str(i) + "次。")

    if a > CN:
        showwarning(message='太大了!')

    if a < CN:
        showwarning(message='太小了!')


Label(window, text="请输入一个数字:").grid(row=1, stick=W, padx=20, pady=10)
Entry(window, textvariable=input_number).grid(row=1, column=1, stick=E)
Button(window, text='Quit', command=window.quit).grid(row=3, column=1, sticky=E)
Button(window, text='Enter', command=guess_number).grid(row=3, column=1, sticky=W)

window.mainloop()
    