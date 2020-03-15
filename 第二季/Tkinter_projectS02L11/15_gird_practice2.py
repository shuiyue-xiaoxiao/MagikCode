from tkinter import *

window = Tk()

window.title('最简单的登录窗口')

Label(window, text='用户名').grid(row=0, column=0,
                               sticky=W)
Label(window, text='密码').grid(row=1, column=0,
                              sticky=W)
Entry(window).grid(row=0, column=1)
Entry(window, show="*").grid(row=1, column=1)

window.mainloop()
