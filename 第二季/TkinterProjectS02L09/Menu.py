from tkinter import *

window = Tk()

window.title('Menu demo')

window.geometry('400x300')

menu_all = Menu(window)

menu_file = Menu(menu_all,
                 tearoff=0)
menu_all.add_cascade(label='file',
                     menu=menu_file)
menu_file.add_command(label='New')
menu_file.add_command(label='Open')
menu_file.add_command(label='Save')
menu_file.add_separator()
menu_file.add_command(label='Exit')

menu_help = Menu(menu_all,
                 tearoff=0)
menu_all.add_cascade(label='Help',
                     menu=menu_file)
menu_help.add_command(label='Help')
menu_help.add_command(label='About')

window.config(menu=menu_all)

window.mainloop()
