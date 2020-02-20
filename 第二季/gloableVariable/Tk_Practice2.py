from tkinter import *

i = 0

window = Tk()

window.title('Label and Button')

window.geometry('400x300+1000+150')

# 将Label标签的内容设置成字符串类型，用var来接收click_me函数传出的内容，用于显示在标签上。
labelText = StringVar()

labelText.set("you click me " + str(i) + " time")

lbl = Label(window, textvariable=labelText, bg="blue", fg="white", width=20, height=3, font=("Arial", 20))
lbl.pack()


def click_me():
    global i
    i = i + 1
    if i <= 1:
        labelText.set("you click me " + str(i) + " time")
    else:
        labelText.set("you click me " + str(i) + " times")


btn = Button(window, text=" click me!", height=2, width=12, command=click_me)
btn.pack()

window.mainloop()
