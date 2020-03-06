from tkinter import *

window = Tk()

window.title('message demo 2')

the_zen_of_python = 'the_zen_of_python\n'\
                    'Beautiful is better than ugly.\n'\
                    'Explicit is better than implicit.\n'\
                    'Simple is better than complex.\n'\
                    'Complex is better than complicated.\n'\
                    'Flat is better than nested.\n'\
                    'Sparse is better than dense.'\
                    'Readability counts.\n'\
                    'Special cases aren’t special enough to break the rules.\n'\
                    'Although practicality beats purity.\n'\
                    'Errors should never pass silently.\n'\
                    'Unless explicitly silenced.\n'\
                    'In the face of ambiguity, refuse the temptation to guess.\n'\
                    'There should be one-- and preferably only one --obvious way to do it.\n'\
                    'Although that way may not be obvious at first unless you’re Dutch.\n'\
                    'Now is better than never.\n'\
                    'Although never is often better than right now.\n'\
                    'If the implementation is hard to explain, it’s a bad idea.\n'\
                    'If the implementation is easy to explain, it may be a good idea.\n'\
                    'Namespaces are one honking great idea – let’s do more of those!\n'

msg = Message(window, relief='solid', bd=2, width=500,
              text=the_zen_of_python)
msg.config(bg='cornflowerblue', font=('Times', 20, 'italic'))
msg.pack()

window.mainloop()
