from tkinter import *

window = Tk()

window.title("List_box")

window.geometry('400x300+1000+150')

list1 = ['one', 'two', 'three', 'four']

var = StringVar()

var.set(list1)

lb = Listbox(window, listvariable=var)
lb.pack()

window.mainloop()
