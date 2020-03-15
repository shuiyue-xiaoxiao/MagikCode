from tkinter import *

window = Tk()

window.title("place_layout")

window.geometry('400x400')

Label(window, text="North-West", font=('Arial bold', 20),
      bg="#FFB6C1", fg="white").place(x=0, y=0, anchor=NW)
Label(window, text="North", font=('Arial bold', 20),
      bg="#DDA0DD", fg="white").place(x=200, y=0, anchor=N)
Label(window, text="North-East", font=('Arial bold', 20),
      bg="#7B68EE", fg="white").place(x=400, y=0, anchor=NE)

Label(window, text="West", font=('Arial bold', 20),
      bg="#FF4500", fg="white").place(x=0, y=200, anchor=W)
Label(window, text="Center", font=('Arial bold', 20),
      bg="#000080", fg="white").place(x=200, y=200, anchor=CENTER)
Label(window, text="East", font=('Arial bold', 20),
      bg="#00FFFF", fg="white").place(x=400, y=200, anchor=E)

Label(window, text="South-West", font=('Arial bold', 20),
      bg="#7FFFAA", fg="white").place(x=0, y=400, anchor=SW)
Label(window, text="South", font=('Arial bold', 20),
      bg="#FFD700", fg="white").place(x=200, y=400, anchor=S)
Label(window, text="South-East", font=('Arial bold', 20),
      bg="#7FFF00", fg="white").place(x=400, y=400, anchor=SE)

window.mainloop()
