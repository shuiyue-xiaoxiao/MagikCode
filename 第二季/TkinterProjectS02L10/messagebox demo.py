from tkinter import *
from tkinter.messagebox import *

window = Tk()

window.title('messagebox demo')

window.geometry('400x300+500+250')


def click_me():
    showinfo(title='showinfo', message='点'
                                       '击'
                                       'o'
                                       'k'
                                       '有'
                                       '惊'
                                       '喜'
                                       '！')
    showinfo(title='showinfo', message='哈'
                                       '哈'
                                       '，'
                                       '你'
                                       '中'
                                       '计'
                                       '了'
                                       '！')
    showinfo(title='showinfo', message='再'
                                       '点'
                                       '一'
                                       '下'
                                       '试'
                                       '试'
                                       '！')
    showinfo(title='showinfo', message='哈'
                                       '哈'
                                       '，'
                                       '你'
                                       '又'
                                       '中'
                                       '计'
                                       '了'
                                       '！')
    showinfo(title='showinfo', message='点'
                                       '击'
                                       'O'
                                       'K'
                                       '以'
                                       '继'
                                       '续'
                                       '！')
    showinfo(title='showinfo', message='不'
                                       '好'
                                       '意'
                                       '思'
                                       '，'
                                       '你'
                                       '再'
                                       '次'
                                       '中'
                                       '计'
                                       '了'
                                       '！')
    showerror(title='showinfo', message='错'
                                        '误'
                                        '！'
                                        '错'
                                        '误'
                                        '！'
                                        '点'
                                        '击'
                                        '次'
                                        '数'
                                        '过'
                                        '多'
                                        '！'
                                        '\n'
                                        '错'
                                        '误编'
                                        '码'
                                        '：'
                                        '4'
                                        '2'
                                        '6'
                                        '7'
                                        '4')
    showwarning(title='showinfo', message='警'
                                          '告'
                                          '！'
                                          '警'
                                          '告'
                                          '！'
                                          '点'
                                          '击'
                                          '次'
                                          '数'
                                          '过'
                                          '多'
                                          '！'
                                          '警'
                                          '告'
                                          '！'
                                          '警'
                                          '%'
                                          '¥'
                                          '#'
                                          '…'
                                          '…'
                                          '%'
                                          '¥'
                                          '&'
                                          '%'
                                          '#'
                                          '¥'
                                          '#'
                                          '%'
                                          '@'
                                          '…'
                                          '…'
                                          '&'
                                          '*'
                                          '（'
                                          '¥'
                                          '#'
                                          ''
                                          '¥'
                                          '@'
                                          '¥'
                                          '#'
                                          '@'
                                          '系'
                                          '统'
                                          '#'
                                          '…'
                                          '…'
                                          '¥'
                                          '*'
                                          '&'
                                          '内'
                                          '存'
                                          '不'
                                          '%'
                                          '¥'
                                          '…'
                                          '…'
                                          '#'
                                          '¥'
                                          '…'
                                          '…'
                                          '%'
                                          '%'
                                          '&'
                                          '%'
                                          '*'
                                          '&'
                                          '&'
                                          '*'
                                          '…'
                                          '…'
                                          '%'
                                          '&'
                                          '足'
                                          '！'
                                          '系'
                                          '¥'
                                          '@'
                                          '¥'
                                          '&'
                                          '统'
                                          '即'
                                          '¥'
                                          '@'
                                          '¥'
                                          '%'
                                          '将'
                                          '崩'
                                          '¥'
                                          '#'
                                          '%'
                                          'Y'
                                          '('
                                          '^'
                                          '_'
                                          '^'
                                          ')'
                                          'Y'
                                          '端'
                )


Button(window,
       text='测'
            '试'
            '按'
            '钮',
       command=click_me
       ).pack()

window.mainloop()
