from tkinter import *

window = Tk()

window.title('Scale Practice')

window.geometry('400x300')

lbl = Label(window,
            bg="green", fg='white',
            width=20, height=2,
            text='Empty')
lbl.pack()


def print_selection(var):
    lbl.config(text='you have selected ' + var)


scale = Scale(window,
              label='try me!',
              from_=0, to=10,
              resolution=0.01,
              tickinterval=2,
              showvalue=1,
              length=300,
              orient=HORIZONTAL,
              command=print_selection,
              activebackground='yellow')
scale.pack()

window.mainloop()
