from tkinter import *

Jason = Tk()

Jason.title('生成标签')

Jason.resizable(0, 0)

Jason.geometry('400x300+1000+150')

# 标签组：
btn1 = Button(Jason, text='按钮1')
btn1.pack(side=TOP)
btn2 = Button(Jason, text='按钮2')
btn2.pack(side=LEFT)
btn3 = Button(Jason, text='按钮3')
btn3.pack(side=BOTTOM)
btn4 = Button(Jason, text='按钮4')
btn4.pack(side=RIGHT)

# 按钮组：
lbl = Label(Jason, text='标签1')
lbl.pack(side=TOP)
lbl = Label(Jason, text='标签2')
lbl.pack(side=LEFT)
lbl = Label(Jason, text='标签3')
lbl.pack(side=BOTTOM)
lbl = Label(Jason, text='标签4')
lbl.pack(side=RIGHT)

Jason.mainloop()