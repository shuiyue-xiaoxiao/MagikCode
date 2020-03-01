from tkinter import *

window = Tk()

window.title("Menu Practice")

window.geometry('400x300')

lbl = Label(window,
            text="Empty",
            bg='green', fg='white',
            width=20, height=2)
lbl.pack()


def click_file():
    lbl.config(text="You have selected New!")


def click_save():
    lbl.config(text="You have selected Save!")


def click_help():
    lbl.config(text="You have selected Help!")


def click_about():
    lbl.config(text="You have selected about!")


def click_python_file():
    lbl.config(text="You have selected python file!")


# 定义一个总菜单
menu_all = Menu(window)

# 定义一个子菜单'menu_file'，子菜单属于总菜单'menu_all'
menu_file = Menu(menu_all,
                 tearoff=0)
# 在主菜单'menu_all'里添加子选项'File'
menu_all.add_cascade(label="File",  # 子选项标签为"File"
                     menu=menu_file)  # 子选项属于子菜单'menu_file'
menu_file.add_command(label="New",
                      command=click_file)  # 在子菜单中添加按钮'Nww'
menu_open = Menu(menu_file,
                 tearoff=0)
menu_file.add_cascade(label='Open',
                      menu=menu_open)
menu_open.add_command(label='Python file',
                      command=click_python_file)
menu_file.add_command(label="Save",
                      command=click_save)  # 在子菜单中添加按钮'Save'
menu_file.add_separator()  # 在子菜单中添加分割线
menu_file.add_command(label="Exit",
                      command=window.quit)

menu_help = Menu(menu_all, tearoff=0)
menu_all.add_cascade(label='Help',  # 子选项标签为"Help"
                     menu=menu_help)  # 子选项属于子菜单'menu_help'
menu_help.add_command(label='Help',
                      command=click_help)
menu_help.add_command(label='About',
                      command=click_about)

window.config(menu=menu_all)  # 将总菜单配置到主窗口'window'
window.mainloop()  # 主窗口循环
