from tkinter import *

window = Tk()

window.title('Entry')

window.geometry('400x300+1000+150')

entry1 = Entry(window, show="*")
entry1.pack()
entry2 = Entry(window, show=None, font=('Arial', 20))
entry2.pack()

window.mainloop()

'''
属性参数          意思
master          代表了父窗口
bg              设置背景颜色，如bg=‘red’
fg              设置前景颜色
font            设置字体大小，如font=('Helvetica 10 bold')
relief          指定外观装饰边界附近的标签,默认是平的,可以设置的参数;flat、groove、raised、ridge、solid、sunken,如relief=‘groove’
bd              设置Button的边框大小;bd(bordwidth)缺省为1或2个像素
textvariable    设置Button与textvariable属性
'''
