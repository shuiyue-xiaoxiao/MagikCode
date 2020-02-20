from tkinter import *

window = Tk()

window.title('Checkbutton demo')

lbl = Label(window,
            text="这是一个多选项：",
            font=('Arial', 16))
lbl.pack()

cb1 = Checkbutton(window,
                  text="python",
                  font=('Arial', 16))
cb1.pack()

cb2 = Checkbutton(window,
                  text="JavaScript",
                  font=('Arial', 16))
cb2.pack()

cb3 = Checkbutton(window,
                  text="C++",
                  font=('Arial', 16))
cb3.pack()

window.mainloop()

'''
常见的Checkbutton参数：
参数名称：             参数用途：
text---------------->显示文本内容
command------------->指定Checkbutton的事件处理函数
onvalue------------->指定Checkbutton处于On状态时的值，如，onvalue=“valueX”
offvalue------------>指定Checkbutton处于Off状态时的值
image--------------->可以使用gif图像，图像的加载方法img = PhotoImage(root,file = filepath)
bitmap-------------->指定位图，如bitmap= BitmapImage(file = filepath)
variable------------>控制变量，跟踪Checkbutton的状态，On(1)，Off(0)
master-------------->代表了父窗口
bg------------------>背景色，如bg=”red”， bg="#FF56EF"
fg------------------>前景色(字体色)，如fg=”red”， fg="#FF56EF"
font---------------->字体及大小，如font=("Arial", 8)，font=("Helvetica 16 bold italic")
height-------------->设置显示高度、如果未设置此项，其大小以适应内容标签
relief-------------->指定外观装饰边界附近的标签,默认是平的,可以设置的参数：flat、groove、raised、ridge、solid、sunken
width--------------->设置显示宽度，如果未设置此项，其大小以适应内容标签
wraplength---------->将此选项设置为所需的数量限制每行的字符,数默认为0
state--------------->设置组件状态;正常(normal),激活(active),禁用(disabled)
selectcolor--------->设置选中区的颜色
selectimage--------->设置选中区的图像，选中时会出现 
bd------------------>设置Checkbutton的边框大小;bd(bordwidth)缺省为1或2个像素
textvariable-------->设置Checkbutton的textvariable属性，文本内容变量
padx---------------->标签水平方向的边距, 默认为1像素
pady---------------->标签竖直方向的边距, 默认为1像素.
justify------------->标签文字的对齐方向, 可选值为 RIGHT, CENTER, LEFT, 默认为 Center
'''