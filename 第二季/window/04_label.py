from tkinter import *

Jason = Tk()

Jason.title('生成标签')

Jason.resizable(0, 0)

Jason.geometry('400x300+1000+150')

lbl = Label(Jason, text='这是一个标签')
# lbl = Label(Jason, test="这是一个标签", font=("Arial Bold", 50), fg="red", bg="green") # 试着加上一些属性
lbl.pack()

Jason.mainloop()

'''
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
'''

