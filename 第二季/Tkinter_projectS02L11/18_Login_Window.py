from tkinter import *
from tkinter.messagebox import *
import webbrowser as web
"""import webbrowser as web"""
window = Tk()

window.title('Login Window demo')

# width = 300
# height = 200
#
#
# screenwidth = window.winfo_screenwidth()
# screenheight = window.winfo_screenheight()
#
# print(str(screenwidth) + "x" + str(screenheight))
#
# alignstr = '%dx%d+%d+%d' % (width, height, (screenheight - width) / 2, (screenheight - height) / 2)
# # alignstr = '300x200+570+350

# window.geometry(alignstr)

window.geometry('300x200+570+350')

username = StringVar()
password = StringVar()


def login_Check():
    name = username.get()
    secret = password.get()
    if name == '学而思' and secret == 'Jason_li_hello_2020':
        window.destroy()
        web.open("https://www.xueersi.com")
    elif name != '学而思':
        showwarning(title="错误", message='账号错误！')
    else:
        showwarning(title="错误", message='密码错误！')


Label(window).grid(row=1, stick=W, pady=10)

Label(window, text="账户:").grid(row=1, stick=W, padx=20, pady=10)
Entry(window, textvariable=username).grid(row=1, column=1, stick=E)

Label(window, text='密码:').grid(row=2, stick=W, padx=20, pady=10)
Entry(window, show="*", textvariable=password).grid(row=2, column=1, stick=E)

Button(window, text='登录', command=login_Check).grid(row=3, stick=W, padx=20, pady=10)
Button(window, text='退出', command=window.quit).grid(row=3, column=1, stick=E)
window.mainloop()
