from tkinter import *

window = Tk()

window.title('pack_side')

window.geometry('400x300')

Label(window, text='.pack(side=TOP)').pack(side=TOP)
Label(window, text='.pack(side=BOTTOM)',
      bg='orange', fg='white').pack(side=BOTTOM)
Label(window, text='.pack(side=LEFT)',
      bg='blue', fg='white').pack(side=LEFT)
Label(window, text='.pack(side=RIGHT)',
      bg='green', fg='white').pack(side=RIGHT)
window.mainloop()
