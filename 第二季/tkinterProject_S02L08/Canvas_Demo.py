from tkinter import *

window = Tk()

window.title("canvas_Demo")

canvas = Canvas(window,
                width=400,height=30)
canvas.pack()

canvas.create_line(0, 100, 400, 100, fill="#4169E1")

mainloop()
