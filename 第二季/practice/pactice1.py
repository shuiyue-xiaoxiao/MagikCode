from tkinter import *

window = Tk()

window.title("Label and Button")

window.geometry('400x300')

lbl = Label(window,text="you click me", bg="blue",
            fg="white",
            width=20,
            height=3,
            font=("Arial", 20))
lbl.pack()

i = 0


def click_me():
    global i

    i = i + 1
    print("you click me " + str(i) + " time")


btn = Button(window, text=" click me!", height=2, width=12, command=click_me)
btn.pack()

window.mainloop()
