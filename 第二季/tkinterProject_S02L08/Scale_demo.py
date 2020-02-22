from tkinter import *

window = Tk()

window.title('Scale demo')

scale1 = Scale(window,
               from_=0.00,
               to=1,)
scale1.pack()

scale2 = Scale(window,
               from_=0, to=1000,
               orient=HORIZONTAL)  # 设置水平方向，如果不写这个参数默认为垂直。
scale2.pack()

window.mainloop()
