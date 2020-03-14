from tkinter import *

window = Tk()

window.title('pack_expand')

window.geometry('150x150')

Label(window, text='label-1', bg='yellow').pack()
Label(window, text='label-2', font=('Times', 20, 'italic'),
      bg='green').pack(expand="yes")
Label(window, text='label-3', bg='yellow').pack(expand="no")

window.mainloop()
