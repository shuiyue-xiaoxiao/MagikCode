from tkinter import *

window = Tk()

window.title('Scale demo 2')

scale1 = Scale(window,
               label='demo1',
               from_=0, to=10,
               tickinterval=2)
scale1.set(6)
scale1.pack()

scale2 = Scale(window,
               from_=0, to=10,
               resolution=20,
               tickinterval=2,
               length=300,
               orient=HORIZONTAL,
               activebackground='green')
scale2.set(60)
scale2.pack()

window = mainloop()
