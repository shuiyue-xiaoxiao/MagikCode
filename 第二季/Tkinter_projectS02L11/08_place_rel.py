from tkinter import *

window = Tk()

window.title("place_layout")

window.geometry('600x600')

Label(window, text="North-West", font=('Arial bold', 20),
      bg="#FFB6C1", fg="white").place(relx=0, rely=0, relwidth=0.33, relheight=0.33)
Label(window, text="North", font=('Arial bold', 20),
      bg="#DDA0DD", fg="white").place(relx=(1/3), rely=0, relwidth=0.33, relheight=0.33)
Label(window, text="North-East", font=('Arial bold', 20),
      bg="#7B68EE", fg="white").place(relx=(2/3), rely=0, relwidth=0.33, relheight=0.33)

Label(window, text="West", font=('Arial bold', 20),
      bg="#FF4500", fg="white").place(relx=0, rely=(1/3), relwidth=0.33, relheight=0.33)
Label(window, text="Center", font=('Arial bold', 20),
      bg="#000080", fg="white").place(relx=(1/3), rely=(1/3), relwidth=0.33, relheight=0.33)
Label(window, text="East", font=('Arial bold', 20),
      bg="#00FFFF", fg="white").place(relx=(2/3), rely=(1/3), relwidth=0.33, relheight=0.33)

Label(window, text="South-West", font=('Arial bold', 20),
      bg="#7FFFAA", fg="white").place(relx=0, rely=(2/3), relwidth=0.33, relheight=0.33)
Label(window, text="South", font=('Arial bold', 20),
      bg="#FFD700", fg="white").place(relx=(1/3), rely=(2/3), relwidth=0.33, relheight=0.33)
Label(window, text="South-East", font=('Arial bold', 20),
      bg="#7FFF00", fg="white").place(relx=(2/3), rely=(2/3), relwidth=0.33, relheight=0.33)

window.mainloop()
