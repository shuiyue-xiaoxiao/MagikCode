import tkinter  # import turtle

Jason = tkinter.Tk()


def hello():
    print("hello, world!")


btn = tkinter.Button(Jason, text="click me", command=hello)
btn.pack()

tkinter.mainloop()
