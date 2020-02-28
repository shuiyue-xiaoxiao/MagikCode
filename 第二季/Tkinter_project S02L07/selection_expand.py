from tkinter import *


def choice_1():
    d = Label(window,
              text="83 x 51 = ? ",
              font=('Arial', 25))
    d.pack(side=TOP)

    rb1_1 = Radiobutton(window,
                        text="4633",
                        variable=var1,
                        value="A",
                        font=('Arial', 25))
    rb1_1.pack(side=TOP)

    rb1_2 = Radiobutton(window,
                        text="3233",
                        variable=var1,
                        value="B",
                        font=('Arial', 25))
    rb1_2.pack(side=TOP)

    rb1_3 = Radiobutton(window,
                        text="4233",
                        variable=var1,
                        value="C",
                        font=('Arial', 25))
    rb1_3.pack(side=TOP)


def choice_2():
    d = Label(window,
              text="65 x 37 = ? ",
              font=('Arial', 25))
    d.pack(side=TOP)

    rb2_1 = Radiobutton(window,
                        text="2305",
                        variable=var2,
                        value="A",
                        font=('Arial', 25))
    rb2_1.pack(side=TOP)

    rb2_2 = Radiobutton(window,
                        text="2405",
                        variable=var2,
                        value="B",
                        font=('Arial', 25))
    rb2_2.pack(side=TOP)

    rb2_3 = Radiobutton(window,
                        text="2485",
                        variable=var2,
                        value="C",
                        font=('Arial', 25))
    rb2_3.pack(side=TOP)


window = Tk()

var1 = StringVar()
var2 = StringVar()

window.title('Radiobutton demo1')

window.geometry('400x400+500+250')

lbl = Label(window,
            text="Empty",
            font=('Arial', 16),
            bg='yellow', fg="blue",
            width=24, height=2)
lbl.pack()


def print_selection():
    if (var1.get() == "C") & (var2.get() == "B"):
        lbl.config(text="You did great!")
    else:
        lbl.config(text="oh oh, try again!")


choice_1()

lbl_empty = Label(window,
                  text="")
lbl_empty.pack(side=TOP)

choice_2()

lbl_empty2 = Label(window,
                   text="")
lbl_empty2.pack(side=TOP)

btn = Button(window,
             text='提交',
             font=('Arial', 20),
             background='blue', fg='red',
             command=print_selection)
btn.pack(anchor=N)

window.mainloop()
