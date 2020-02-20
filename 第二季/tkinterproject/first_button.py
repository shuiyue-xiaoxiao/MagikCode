import tkinter

jason = tkinter.Tk()


def hello():
    print("hello, world")


btn = tkinter.Button(jason, text="点我！", command=hello)  # 参数（master, text="",command=)
btn.pack()

tkinter.mainloop()
