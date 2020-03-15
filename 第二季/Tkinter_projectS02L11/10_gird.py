from tkinter import *

window = Tk()

window.title("Place_Layout")

# window.geometry('600x600')

Label(window, text="第0行，第0列", font=('Arial bold', 20),
      bg="#FFB6C1", fg="white").grid(row=0, column=0)
Label(window, text="第0行，第1列", font=('Arial bold', 20),
      bg="#DDA0DD", fg="white").grid(row=0, column=1)
Label(window, text="第0行，第2列", font=('Arial bold', 20),
      bg="#7B68EE", fg="white").grid(row=0, column=2)

Label(window, text="第1行，第0列", font=('Arial bold', 20),
      bg="#FF4500", fg="white").grid(row=1, column=0)
Label(window, text="第1行，第1列", font=('Arial bold', 20),
      bg="#000080", fg="white").grid(row=1, column=1)
Label(window, text="第1行，第2列", font=('Arial bold', 20),
      bg="#00FFFF", fg="white").grid(row=1, column=2)

Label(window, text="第2行，第0列", font=('Arial bold', 20),
      bg="#7FFFAA", fg="white").grid(row=2, column=0)
Label(window, text="第2行，第1列", font=('Arial bold', 20),
      bg="#FFD700", fg="white").grid(row=2, column=1)
Label(window, text="第2行，第2列", font=('Arial bold', 20),
      bg="#7FFF00", fg="white").grid(row=2, column=2)

window.mainloop()



