from tkinter import *

window = Tk()

window.title('pack_side')


top_arrow = StringVar()
top_text = "上⬆️"
top_arrow.set(top_text)


def top():
    global top_text
    top_text += "\n上⬆️"
    top_arrow.set(top_text)


bottom_arrow = StringVar()
bottom_text = "下⬇️"
bottom_arrow.set(bottom_text)


def bottom():
    global bottom_text
    bottom_text += "\n下⬇️"
    bottom_arrow.set(bottom_text)


left_arrow = StringVar()
left_text = "左⬅️️"
left_arrow.set(left_text)


def left():
    global left_text
    left_text += " 左⬅️️"
    left_arrow.set(left_text)


right_arrow = StringVar()
right_text = "右➡️"
right_arrow.set(right_text)


def right():
    global right_text
    right_text += " 右➡️"
    right_arrow.set(right_text)


Label(window,
      text='这是一个控制键盘',
      bd=4,
      relief="ridge",
      cursor='question_arrow').pack(side=TOP)

Button(window,
       textvariable=top_arrow,
       cursor='top_side',
       command=top).pack(side=TOP, fill=Y, padx=10, pady=10)
Button(window,
       textvariable=bottom_arrow,
       cursor='bottom_side',
       command=bottom).pack(side=BOTTOM, fill=Y, padx=10, pady=10)
Button(window,
       textvariable=left_arrow,
       cursor='left_side',
       command=left).pack(side=LEFT, padx=20)
Button(window,
       textvariable=right_arrow,
       cursor='right_side',
       command=right).pack(side=RIGHT, padx=20)

Button(window,
       text='退出',
       bd=4,
       relief="raised",
       command=window.quit).pack(side=BOTTOM)

window.mainloop()
