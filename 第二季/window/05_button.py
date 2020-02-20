from tkinter import *

Jason = Tk()

Jason.title('生成标签')

Jason.resizable(0, 0)

Jason.geometry('400x300+1000+150')

lbl = Label(Jason, text='这是一个标签')
lbl.pack()

btn = Button(Jason, text='这是一个按钮')
btn.pack()

Jason.mainloop()

'''
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
'''