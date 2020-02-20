from tkinter import *

window = Tk()

window.title('Entry')

window.geometry('400x300+1000+150')

entry1 = Entry(window, show="*")
entry1.pack()
entry2 = Entry(window, show=None, font=('Arial', 20))
entry2.pack()

window.mainloop()
