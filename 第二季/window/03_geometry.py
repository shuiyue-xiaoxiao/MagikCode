from tkinter import *

Jason = Tk()

Jason.title('窗口属性')

Jason.resizable(0, 0)


# 01：
# 设置宽高：
Jason.geometry('400x300')
'''
# 02：
# 设置位置：
Jason.geometry("+0+0") # 先运行这个
# Jason.geometry("+1000+150") # 再运行这个


# 03：
# 同时设置位置和宽高：
Jason.geometry("400x300+1000+150")
'''
Jason.mainloop()  # 结束

