from tkinter import *

window = Tk()

window.title('Radiobutton demo 2')

lbl = Label(window,
            text='Empty',
            font=('Arial', 16),
            bg='green', fg='white',
            width=20, height=2)

lbl.pack(anchor=W)


def print_selection():
    lbl.config(text='you have selected ' + var.get())


var = StringVar()

rb1 = Radiobutton(window,
                  text="Option A",
                  variable=var,
                  value="A",
                  command=print_selection)
rb1.pack(anchor=W)

rb2 = Radiobutton(window,
                  text="Option B",
                  variable=var,
                  value="B",
                  command=print_selection)
rb2.pack(anchor=W)

rb3 = Radiobutton(window,
                  text="Option C",
                  variable=var,
                  value="C",
                  command=print_selection)
rb3.pack(anchor=W)


window.mainloop()
