from tkinter import *

window = Tk()

window.title("pack_padx_pady")

# window.geometry('400x300')

Label(window, text=".pack(side=TOP)",
      bg="orange", fg="white").pack(side=TOP, fill=X, padx=10, pady=10)
Label(window, text=".pack(side=BOTTOM)",
      bg="red", fg="white").pack(side=BOTTOM, fill=X, padx=10, pady=10)
Label(window, text=".pack(side=LEFT)",
      bg="blue", fg="white").pack(side=LEFT, padx=10)
Label(window, text=".pack(side=RIGHT)",
      bg="green", fg="white").pack(side=RIGHT, padx=10)


window.mainloop()
