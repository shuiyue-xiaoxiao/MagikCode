from tkinter import *

window = Tk()

window.title("Menu Practice")

window.geometry('400x300')

# 定义一个总菜单
menu_all = Menu(window)

# 定义一个子菜单'menu_file'，子菜单属于总菜单'menu_all'
menu_file = Menu(menu_all,
                 tearoff=0)
# 在主菜单'menu_all'里添加子选项'File'
menu_all.add_cascade(label="File",  # 子选项标签为"File"
                     menu=menu_file)  # 子选项属于子菜单'menu_file'
menu_file.add_command(label="New")  # 在子菜单中添加按钮'Nww'
menu_file.add_command(label="Open")  # 在子菜单中添加按钮'Open'
menu_file.add_command(label="Save")  # 在子菜单中添加按钮'Save'
menu_file.add_separator()  # 在子菜单中添加分割线
menu_file.add_command(label="Exit")

menu_help = Menu(menu_all, tearoff=0)
menu_all.add_cascade(label='Help',  # 子选项标签为"Help"
                     menu=menu_help)  # 子选项属于子菜单'menu_help'
menu_help.add_command(label='Help')
menu_help.add_command(label='About')

window.config(menu=menu_all)  # 将总菜单配置到主窗口'window'
window.mainloop()  # 主窗口循环


'''
参数：
bg                      背景色，如bg=”red”， bg="#FF56EF"
fg                      前景色，如fg=”red”， fg="#FF56EF"
font                    字体设置，如font=("Arial", 8)
relief                  指定外观装饰边界附近的标签,默认是平的,可以设置的参数：
                        flat、groove、raised、ridge、solid、sunken
selectcolor             设置选中区的颜色
activebackgound         点击时背景，同样有activeforeground，activeborderwidth，
                        disabledforeground
bd                      设置Checkbutton的边框大小;bd(bordwidth)缺省为1或2个像素
borderwidth    　       边框宽度
tearoff      　         分窗，0为在原窗，1为点击分为两个窗口
label                   标签，选项名
menu                    菜单
---------------------------------------------------------------------------
特有函数(方法)：
menu.add_cascade        添加子选项
menu.add_command        添加命令（label参数为显示内容）
menu.add_separator      添加分隔线
menu.add_checkbutton    添加确认按钮
delete                  删除
'''