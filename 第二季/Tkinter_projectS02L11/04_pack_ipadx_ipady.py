from tkinter import *

window = Tk()

window.title("pack_ipadx_ipady")

# window.geometry('400x300')

Label(window, text=".pack(side=TOP)",
      bg="orange", fg="white",
      relief='solid', bd=5).pack(side=TOP,
                                 fill=X,
                                 padx=20,
                                 pady=10,
                                 ipady=10,
                                 ipadx=20)
Label(window, text=".pack(side=BOTTOM)",
      bg="red", fg="white").pack(side=BOTTOM,
                                 fill=X,
                                 padx=10,
                                 pady=10,
                                 ipady=10)
Label(window, text=".pack(side=LEFT)",
      bg="blue", fg="white").pack(side=LEFT,
                                  fill=Y,
                                  padx=10,
                                  ipadx=10,
                                  ipady=10)
Label(window, text=".pack(side=RIGHT)",
      bg="green", fg="white").pack(side=RIGHT,
                                   fill=Y,
                                   padx=10,
                                   ipadx=10,
                                   ipady=10)

window.mainloop()
