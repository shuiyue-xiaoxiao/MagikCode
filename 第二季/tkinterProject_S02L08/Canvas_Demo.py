from tkinter import *

window = Tk()

window.title("canvas_Demo")

canvas = Canvas(window,
                width=400,height=30)
canvas.pack()

canvas.create_line(0, 100, 400, 100, fill="#4169E1")

mainloop()

"""
Canvas常用参数如下：
master           代表了父窗口
bg               背景色，如bg=”red”， bg="#FF56EF"
fg               前景色，如fg=”red”， fg="#FF56EF"
height           设置显示高度、如果未设置此项，其大小以适应内容标签
relief           指定外观装饰边界附近的标签,默认是平的,可以设置的参数：flat、groove、raised、ridge、solid、sunken
width            设置显示宽度，如果未设置此项，其大小以适应内容标签
state            设置组件状态;正常(normal),激活(active),禁用(disabled)
bd               设置Button的边框大小;bd(bordwidth)缺省为1或2个像素

除了option，Canvas还有一些专属的函数，列表如下：

create_arc       绘制圆弧
create_bitmap    绘制位图，支持XBM，bitmap= BitmapImage(file = filepath)
create_image     绘制图片，支持GIF(x,y,image,anchor); image= PhotoImage(file="../xxx/xxx.gif") ,目前仅支持gif格式
create_line      绘制支线
create_oval;     绘制椭圆；
create_polygon   绘制多边形(坐标依次罗列，不用加括号，还有参数，fill,outline)；
create_rectangle 绘制矩形((a,b,c,d),值为左上角和右下角的坐标)；
create_text      绘制文字(字体参数font,), 如font=("Arial", 8)，font=("Helvetica 16 bold italic")
create_window    绘制窗口；
delete           删除绘制的图形；
itemconfig       修改图形属性，第一个参数为图形的ID，后边为想修改的参数
move             移动图像
coords(ID)       返回对象的位置的两个坐标（4个数字元组）
"""


