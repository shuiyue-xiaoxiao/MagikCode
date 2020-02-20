from tkinter import *

window = Tk()

window.title('Radiobutton demo1')

lbl = Label(window, text="你的教育背景：")
lbl.pack(anchor=W)

var = StringVar()

rb1 = Radiobutton(window, text="大学", variable=var, value="A")
rb1.pack(anchor=W)

rb2 = Radiobutton(window, text="硕士", variable=var, value="B")
rb2.pack(anchor=W)

rb3 = Radiobutton(window, text="博士", variable=var, value="C")
rb3.pack(anchor=W)

window.mainloop()
