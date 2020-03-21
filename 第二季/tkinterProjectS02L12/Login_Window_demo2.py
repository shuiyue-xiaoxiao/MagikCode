from tkinter import *
from tkinter.messagebox import *

window = Tk()

window.title('Login Window demo')

width = 300
height = 200

screenwidth = window.winfo_screenwidth()
screenheight = window.winfo_screenheight()
print(str(screenwidth) + "x" + str(screenheight))

alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)

window.geometry(alignstr)


class Login_Page(Frame):
    def __init__(self):
        super().__init__()
        self.username = StringVar()
        self.password = StringVar()
        self.pack()
        self.Create_from()

    def Create_from(self):
        Label(self).grid(row=0, stick=W, pady=10)

        Label(self, text="账户:").grid(row=1, stick=W, pady=10)
        Entry(self, textvariable=self.username).grid(row=1, column=1, stick=E)

        Label(self, text='密码:').grid(row=2, stick=W, pady=10)
        Entry(self, show="*", textvariable=self.password).grid(row=2, column=1, stick=E)

        Button(self, text='登录', command=self.loginCheck).grid(row=3, stick=W, pady=10)
        Button(self, text='退出', command=self.quit).grid(row=3, column=1, stick=E)

    def loginCheck(self):
        name = self.username.get()
        secret = self.password.get()
        if name == 'scratch' and secret == 'Jason_li':
            self.destroy()
        elif name != 'scratch':
            showwarning(title="错误", message='账号错误！')
        else:
            showwarning(title="错误", message='密码错误！')


page1 = Login_Page()

window.mainloop()
