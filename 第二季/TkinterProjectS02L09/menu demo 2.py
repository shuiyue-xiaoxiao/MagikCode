from tkinter import *


def add_My_PyCharm_Menu():
    menu_My_PyCharm = Menu(menu_all,
                           tearoff=0)
    menu_all.add_cascade(label="My PyCharm(模仿PyCharm菜单)",
                         font=('Arial', 16, 'bold'),
                         menu=menu_My_PyCharm)
    menu_My_PyCharm.add_command(label="About PyCharm")
    menu_My_PyCharm.add_command(label="Check for updates...")
    menu_My_PyCharm.add_separator()
    menu_My_PyCharm.add_command(label="Preferences...")
    menu_My_PyCharm.add_separator()

    menu_Services = Menu(menu_My_PyCharm,
                         tearoff=0)
    menu_My_PyCharm.add_cascade(label="Services", menu=menu_Services)
    menu_Services.add_command(label='       Activity Monitor')
    menu_Services.add_command(label='       Allocation & Leaks')
    menu_Services.add_command(label='       File Activity')
    menu_Services.add_command(label='       System Trace')
    menu_My_PyCharm.add_separator()
    menu_My_PyCharm.add_command(label="Hide PyCharm")
    menu_My_PyCharm.add_command(label="Hide Others")
    menu_My_PyCharm.add_command(label="Show all")
    menu_My_PyCharm.add_separator()
    menu_My_PyCharm.add_command(label="Quit PyCharm",
                                command=window.quit)


if __name__ == "__main__":
    window = Tk()

    window.title("Menu Practice")

    window.geometry('400x300')

    # 定义一个总菜单
    menu_all = Menu(window)

    add_My_PyCharm_Menu()

    window.config(menu=menu_all)  # 将总菜单配置到主窗口'window'

    window.mainloop()  # 主窗口循环
