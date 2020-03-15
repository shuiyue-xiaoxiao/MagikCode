from tkinter import *

window = Tk()

window.title("最简单的登录窗口：合并")

Label(window, text="用户名").grid(row=0, column=0,
                               sticky=W)
Label(window, text="密码").grid(row=1, column=0,
                              sticky=W)

Entry(window).grid(row=0, column=1)
Entry(window, show="*").grid(row=1, column=1)

photo = PhotoImage(file="logo.gif")
Label(window, image=photo).grid(row=0, column=2,
                                rowspan=2,
                                padx=5, pady=5)

Button(text="提交", width=10, command=window.quit).grid(row=2,
                                                      columnspan=3,
                                                      pady=5)

window.mainloop()

