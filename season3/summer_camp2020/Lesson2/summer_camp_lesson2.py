"""graphic operation"""
from tkinter import *
from tkinter import colorchooser
import threading

root = Tk()
root.title("图形操作")

canvas = Canvas(root, bg="white", width=400, height=300)
canvas.pack(fill=BOTH, expand=YES)

root.mainloop()
