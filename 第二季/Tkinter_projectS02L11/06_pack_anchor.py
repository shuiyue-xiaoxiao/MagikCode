from tkinter import *

window = Tk()

window.title("pack_padx_pady")

window.geometry('600x600')

Label(window, text=".pack(anchor=NE)",
      width=20, height=3,
      bg="#FFB6C1", fg="white").pack(anchor=NE)
Label(window, text=".pack(anchor=N)",
      width=20, height=3,
      bg="#DDA0DD", fg="white").pack(anchor=N)
Label(window, text=".pack(anchor=NW)",
      width=20, height=3,
      bg="#7B68EE", fg="white").pack(anchor=NW)

Label(window, text=".pack(anchor=E)",
      width=20, height=3,
      bg="#FF4500", fg="white").pack(anchor=E)
Label(window, text=".pack(anchor=CENTER)",
      width=20, height=3,
      bg="#000080", fg="white").pack(anchor=CENTER)
Label(window, text=".pack(anchor=W)",
      width=20, height=3,
      bg="#00FFFF", fg="white").pack(anchor=W)

Label(window, text=".pack(anchor=SE)",
      width=20, height=3,
      bg="#7FFFAA", fg="white").pack(anchor=SE)
Label(window, text=".pack(anchor=S)",
      width=20, height=3,
      bg="#FFD700", fg="white").pack(anchor=S)
Label(window, text=".pack(anchor=SW)",
      width=20, height=3,
      bg="#7FFF00", fg="white").pack(anchor=SW)

window.mainloop()
