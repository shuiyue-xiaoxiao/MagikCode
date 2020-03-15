from tkinter import *

window = Tk()

window.title("显示图片")

width = 600
height = 600

screenwidth = window.winfo_screenwidth()
screenheight = window.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
window.geometry(alignstr)

photo = PhotoImage(file="logo.png")
labelImg = Label(window, image=photo)
labelImg.pack(side=TOP)

window.mainloop()
