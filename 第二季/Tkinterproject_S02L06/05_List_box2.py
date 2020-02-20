"""
写代码就像盖房子一样, 共分为以下几步：
(1):盖地基, 写三板斧：
from tkinter import *
window = Tk()
window.mainloop()

(2):写基础装饰。(就像摆家具)
    例如：title, geometry, list, label, entry, text, button...

(3):写细节装饰。(就像摆生活用品)
    例如：justify, font, padx, command, activeforeground, width...

"""
from tkinter import *

window = Tk()

window.title("List box2")

window.geometry('400x300+1000+150')

list1 = ["item1", "item2", "item3", "item4", "item5"]

var = StringVar()
var.set(list1)

lb = Listbox(window, listvariable=var, selectmode=BROWSE)

lb.insert(END, ["Hello, world!", "Hello, Leo!", "Hello, Jason!", "Hello, alice!"])
lb.insert(END, [1, 2, 3, 4])
lb.delete(0, 2)
lb.select_set(1, 2)
lb.pack()

window.mainloop()
