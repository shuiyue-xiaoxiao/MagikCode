from tkinter import *

jason = Tk()


def say_hello():
    print("hello, world!")


btn = Button(jason, text="点我！", command=say_hello)
btn.pack()


mainloop()
