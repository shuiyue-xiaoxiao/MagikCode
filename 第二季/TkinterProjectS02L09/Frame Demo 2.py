from tkinter import *

window = Tk()

window.title('Frame Demo')

window.geometry('400x300+500+250')

Label(window,
      text='主窗口',
      bg='#AACCDD', fg='#90FA82',
      font=('Arial', 16)).pack()

frame = Frame(window, bg='#990449',
              width=400, height=300)
frame.grid_propagate(0)
frame.pack()
Label(frame, text="主框架",
      bg='#ED4D4D').pack()

# 在主框架中设置左侧子框架
frame_left = Frame(frame)
frame_left.pack(side='left')
Label(frame_left,
      text='左侧子框架标签1', bg='#DA8603').pack()
Label(frame_left,
      text='左侧子框架标签2', bg='#DD9966').pack()

# 在主框架中设置右侧子框架
frame_right = Frame(frame)
frame_right.pack(side='right')
Label(frame_right,
      text='右侧子框架标签1',
      bg='Cyan').pack()
Label(frame_right,
      text='右侧子框架标签2', bg='#7FFFAA').pack()

window.mainloop()
