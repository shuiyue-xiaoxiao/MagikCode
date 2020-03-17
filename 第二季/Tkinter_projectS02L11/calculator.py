from tkinter import *

window = Tk()

window.title('practice3')

frame = Frame(window)
frame.pack(padx=10, pady=10)

v1 = StringVar()
v2 = StringVar()
v3 = StringVar()


def test(content):
    return content.isdigit()


testCOD = frame.register(test)

entry1 = Entry(frame,
               width=10,
               textvariable=v1,
               validate='key',
               validatecommand=(testCOD, '%P')).grid(row=0, column=0)

Label(frame, text='+').grid(row=0, column=1)

entry2 = Entry(frame,
               width=10,
               textvariable=v2,
               validate='key',
               validatecommand=(testCOD, '%P')).grid(row=0, column=2)

Label(frame, text='=').grid(row=0, column=3)

entry3 = Entry(frame,
               width=10,
               textvariable=v3,
               state='readonly',
               validatecommand=(testCOD, '%P')).grid(row=0, column=4)


def calc():
    result = int(v1.get()) + int(v2.get())
    v3.set(str(result))


Button(frame, text='计算结果', command=calc).grid(row=1, column=2, pady=5)

window.mainloop()
