from tkinter.filedialog import *
from tkinter import *

window = Tk()

window.title("filedialog demo")


def open_file():
    fileName = askopenfilename()
    print(fileName)


Button(window, text='open file', command=open_file).pack()

window.mainloop()
