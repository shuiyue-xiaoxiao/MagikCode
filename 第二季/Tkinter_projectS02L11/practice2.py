from tkinter import *

window = Tk()

window.title("输入框与按钮程序")

Label(window, text="作品:").grid(row=0, column=0)
Label(window, text="作者:").grid(row=1, column=0)

entry1 = Entry(window)
entry2 = Entry(window)

entry1.grid(row=0, column=1, padx=10, pady=5)
entry2.grid(row=1, column=1, padx=10, pady=5)


def show():
    print("作品:《%s》" % entry1.get())
    print("作者: %s" % entry2.get())


Button(window, text="获取信息", width=10, command=show)\
    .grid(row=3, column=0, sticky=W, padx=10, pady=5)
Button(window, text="点击退出", width=10, command=window.quit)\
    .grid(row=3, column=1, sticky=E, padx=10, pady=5)

window.mainloop()
