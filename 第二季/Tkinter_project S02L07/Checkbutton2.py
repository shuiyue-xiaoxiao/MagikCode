from tkinter import *

window = Tk()

window.title('Checkbutton demo')

window.geometry('400x300')

lbl = Label(window,
            text="Empty",
            font=('Arial', 16),
            bg='yellow', fg="blue",
            width=24, height=2)
lbl.pack()


def print_selection():
    if (var1.get() == 0) & (var2.get() == 0) & (var3.get() == 0):
        lbl.config(text="I do not love either.")
    elif (var1.get() == 1) & (var2.get() == 0) & (var3.get() == 0):
        lbl.config(text="I love only python.")
    elif (var1.get() == 0) & (var2.get() == 1) & (var3.get() == 0):
        lbl.config(text="I love only JavaScript.")
    elif (var1.get() == 0) & (var2.get() == 0) & (var3.get() == 1):
        lbl.config(text="I love only C++.")
    elif (var1.get() == 1) & (var2.get() == 1) & (var3.get() == 0):
        lbl.config(text="I love python and JavaScript.")
    elif (var1.get() == 1) & (var2.get() == 0) & (var3.get() == 1):
        lbl.config(text="I love python and C++.")
    elif (var1.get() == 0) & (var2.get() == 1) & (var3.get() == 1):
        lbl.config(text="I love C++ and JavaScript.")
    else:
        lbl.config(text="I love both.")


var1 = IntVar()
cb1 = Checkbutton(window,
                  text="python",
                  font=('Arial', 16),
                  onvalue=1, offvalue=0,
                  variable=var1,
                  command=print_selection)
cb1.pack()

var2 = IntVar()
cb2 = Checkbutton(window,
                  text="JavaScript",
                  font=('Arial', 16),
                  onvalue=1, offvalue=0,
                  variable=var2,
                  command=print_selection)
cb2.pack()

var3 = IntVar()
cb3 = Checkbutton(window,
                  text="C++",
                  font=('Arial', 16),
                  onvalue=1, offvalue=0,
                  variable=var3,
                  command=print_selection)
cb3.pack()

window.mainloop()
