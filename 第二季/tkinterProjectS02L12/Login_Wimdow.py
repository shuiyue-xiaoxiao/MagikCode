import pickle
from tkinter import *
from tkinter import messagebox

window = Tk()

window.title('Welcome to Scratch Website')

width = 405
height = 350

screenwidth = window.winfo_screenwidth()
screenheight = window.winfo_screenheight()
print(str(screenwidth) + "x" + str(screenheight))

alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)

window.geometry(alignstr)

canvas = Canvas(window, width=400, height=135, bg='#40789A')
image_file = PhotoImage(file='logo_white.gif')
image = canvas.create_image(200, 18, anchor=N, image=image_file)
canvas.pack(side=TOP)
Label(window, text='Welcome', font=('Arial', 16)).pack()

Label(window, text='User name:', font=('Arial', 16)).place(x=40, y=180)
Label(window, text='Password:', font=('Arial', 16)).place(x=40, y=220)

var_user_name = StringVar()
var_user_name.set('example@python.com')
entry_user_name = Entry(window, textvariable=var_user_name, font=('Arial', 16))
entry_user_name.place(x=130, y=175)

var_user_pwd = StringVar()
entry_user_pwd = Entry(window, textvariable=var_user_pwd, font=('Arial', 16), show="*")
entry_user_pwd.place(x=130, y=218)


def usr_login():
    usr_name = var_user_name.get()
    usr_pwd = var_user_pwd.get()

    try:
        with open('usrs_info.pickle', 'rb') as usr_file:
            usrs_into = pickle.load(usr_file)
    except FileNotFoundError:
        with open('usrs_info.pickle', 'rb') as usr_file:
            usrs_into = {'admin': 'admin'}
            pickle.dump(usrs_into, usr_file)
            usr_file.close()

    if usr_name in usrs_into:
        if usr_pwd == usrs_into[usr_name]:
            messagebox.showinfo(title='welcome', message='How are you?' + usr_name)
        else:
            messagebox.showerror(message='Error, your password is wrong, try again？')
    else:
        is_sign_up = messagebox.askyesno('Welcome! ', 'You hove not sign up yet, Sign up now?')
        if is_sign_up:
            usr_sign_up()


def usr_sign_up():
    def sign_to_Magikid_Website():
        np = new_pwd.get()
        npf = new_pwd_confirm.get()
        nn = new_name.get()

        with open('usrs_info.pickle', 'rb') as usr_file:
            exist_usr_info = pickle.load(usr_file)

        if np != npf:
            messagebox.showerror('Error', 'password confirm password must be the same!')
        elif nn in exist_usr_info:
            messagebox.showerror('Error', 'The user has already signed up!')
        else:
            exist_usr_info[nn] = np
            with open('usrs_info.pickle', 'wb') as usr_file:
                pickle.dump(exist_usr_info, usr_file)
            messagebox.showinfo('Welcome! ', 'You have successfully signed up!')
            window_sign_up.destroy()

    window_sign_up = Toplevel(window)
    window_sign_up.geometry('350x200')
    window_sign_up.title('sign up window')

    new_name = StringVar()
    new_name.set('example@python.com')
    Label(window_sign_up, text='User name:', font=('Arial', 16)).place(x=10, y=32)

    entry_new_name = Entry(window_sign_up, textvariable=new_name, font=('Arial', 16))
    entry_new_name.place(x=140, y=30)

    new_pwd = StringVar()
    Label(window_sign_up, text='Password:', font=('Arial', 16)).place(x=10, y=72)
    entry_user_pwd2 = Entry(window_sign_up, textvariable=new_pwd, show='*', font=('Arial', 16))
    entry_user_pwd2.place(x=140, y=70)

    new_pwd_confirm = StringVar()
    Label(window_sign_up, text='Confirm password:', font=('Arial', 16)).place(x=10, y=112)
    entry_user_pwd_confirm = Entry(window_sign_up, textvariable=new_pwd_confirm, show='*', font=('Arial', 16))
    entry_user_pwd_confirm.place(x=140, y=110)

    btn_confirm_sign_up = Button(window_sign_up, text='Sign up',
                                 font=('Arial', 16), command=sign_to_Magikid_Website)
    btn_confirm_sign_up.place(x=255, y=160)


btn_login = Button(window, text='Login', command=usr_login)
btn_login.place(x=130, y=260)
btn_sign_up = Button(window, text='sign_up', command=usr_login)
btn_sign_up.place(x=260, y=260)

window.mainloop()
