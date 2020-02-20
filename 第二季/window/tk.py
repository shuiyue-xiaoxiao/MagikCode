
from tkinter import *
from PIL import ImageTk, Image
jason = Tk()

jason.title("万花筒（自创题目）")

jason.geometry("400x300")

lbl = Label(jason, text='标签1', fg='red', bg='blue', font=("华文行楷", 20))
lbl.pack()

def bg():
    image2 = Image.open(r'/Users/xiao/魔力小孩-编程大师/第二季/window/2202cbef38006d7e9e69d9ec466a6a99a9fd4ff06f678-TStVz9.gif')
    background_image = ImageTk.PhotoImage(image2)
    w = background_image.width()
    h = background_image.height()
    jason.geometry('%dx%d+0+0' % (w, h))

    background_label = Label(jason, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # photo = PhotoImage(file='2202cbef38006d7e9e69d9ec466a6a99a9fd4ff06f678-TStVz9.gif')
    # canvas = Label(jason, text='', image=photo, compound=CENTER)
    # canvas.pack()


btn = Button(jason, text='按下有惊喜!', command=bg, activebackground='blue')
btn.pack()

jason.mainloop()

"""
---- label常用属性 ---- (x处要写参数, 字符串, 颜色以及单词)
属性：       属性解析：                      实例：
text        需要在界面显示的Label标签内容      Label(root, text='xxx')
height      组件的高度（所占行数）             Label(root, text='xxx', height=x）
width       组件的宽度（所占字符个数）          Label(root, text='xxx', height=x, width=x）
fg          前景字体颜色                     Label(root, text='xxx', fg='xxx')
bg          字体颜色                        Label(root, text='xxx', bg='xxx')
justify     多行文本的对齐方式                Label(root, text='xxx', justify=tk.xxx)
padx        文本左右两侧的空格数（默认为1）     Label(root, text='xxx', padx=x)
pady        文本上下两侧的空格数（默认为1）     Label(root, text='xxx', pady=x)
font        设置字体格式和大小                Label(root, text='xxx', fond=("xxx", x))

---- button常用属性 ---- (x处要写参数, 字符串, 颜色, 单词以及函数)
属性：              属性解析：                      实例：
text               需要在界面显示的Label标签内容      button(root, text='xxx')
height             组件的高度（所占行数）             button(root, text='xxx', height=x）
width              组件的宽度（所占字符个数）          button(root, text='xxx', height=x, width=x）
fg                 前景字体颜色                     button(root, text='xxx', fg='xxx')
bg                 字体颜色                        button(root, text='xxx', bg='xxx')
activebackground   按钮按下时的背景颜色              button(root, text='xxx', activebackground='xxx')
activeforeground   按钮按下时的前景字体颜色           button(root, text='xxx', activeforeground='xxx')                         
justify            多行文本的对齐方式                button(root, text='xxx', justify=tk.xxx)  
padx               文本左右两侧的空格数（默认为1）     button(root, text='xxx', padx=x)
pady               文本上下两侧的空格数（默认为1）     button(root, text='xxx', pady=x)
command            按钮出发执行的命令（函数）          button(root, text='xxx', command=xxx)

# python之父在tkinter库中给出的案例如下：
import tkinter

from tkinter.constants import *

tk = tkinter.Tk()

frame = tkinter.Frame(tk, relief=RIDGE, borderwidth=2)

frame.pack(fill=BOTH,expand=1)

label = tkinter.Label(frame, text="Hello, World")

label.pack(fill=X, expand=1)

button = tkinter.Button(frame,text="Exit",command=tk.destroy)

button.pack(side=BOTTOM)

tk.mainloop()

"""