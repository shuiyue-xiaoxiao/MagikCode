from tkinter import *

colors = ['red', 'orange', 'yellow', 'green', 'cyan', 'blue', 'purple']
r1 = 0
for color in colors:
    Label(text=color, relief=RIDGE, width=15).grid(row=r1, column=0)
    Entry(bg=color, relief=SUNKEN, width=10).grid(row=r1, column=1)
    r1 = r1 + 1

colors_hex = ['#FF0000', '#FF8000', '#FFFF00', '#00FF00', '#00FFFF', '#0000FF', '#8000FF']
r2 = 0
for color_hex in colors_hex:
    Label(text=color_hex, relief=RIDGE, width=15).grid(row=r2, column=2)
    Entry(bg=color_hex, relief=SUNKEN, width=10).grid(row=r2, column=3)
    r2 = r2 + 1


mainloop()
