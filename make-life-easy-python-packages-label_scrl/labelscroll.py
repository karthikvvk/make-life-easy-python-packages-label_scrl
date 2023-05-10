"""
This module provides vertical scroll in tkinter.
"""
from tkinter import *
from tkinter import ttk

n = 0
no = 0


def button_scroll(tkinter_win, text=[], bg="#f3f3f3", fg='black', txt_row=1, txt_col=0, bt_down_row=0, bt_up_row=0,
                  bt_top_row=0, bt_down_col=0, bt_up_col=1, bt_top_col=2, justify='LEFT'):
    global n, no
    root_w = tkinter_win.winfo_screenwidth()
    root_h = tkinter_win.winfo_screenheight()
    tkinter_win.geometry(f'{root_w}x{root_h}')
    tkinter_win.configure(bg=bg)
    no = int(root_h / 50 + 17)
    lis = []

    no = no - txt_row
    len_txt = len(text)
    exist_diff = len_txt - ((int(len_txt / no)) * no)
    diff = no - exist_diff

    for i in range(diff):
        text.append('')

    for iii in range(no):
        lis.append(f'a{iii}')
        lis[iii] = StringVar(tkinter_win, value='')
        lis[iii] = Label(tkinter_win, text=text[iii], bg=bg, fg=fg, justify=eval(justify.upper()))
        lis[iii].grid(row=txt_row, column=txt_col)
        txt_row += 1

    def dw():
        global n, no
        f = 0
        if n+exist_diff < len_txt:
            for ig in range(n, n + no):
                try:
                    lis[f].configure(text=text[ig + no])
                except:
                    n = len_txt
                f += 1
            n += no

    def up():
        global n, no
        f = 0
        li = [h for h in range(n - no, n + 1)]
        if f < n:
            for it in li:
                try:
                    lis[f].configure(text=text[it])
                except:
                    None
                f += 1

            n -= no

    def top():
        global n, no
        n = 0
        f = 0
        for ih in range(n, n + no):
            lis[f].configure(text=text[ih])
            f += 1
        n += no

    ttk.Button(tkinter_win, text='\/.', command=dw).grid(row=bt_down_row, column=bt_down_col)
    ttk.Button(tkinter_win, text='/\.', command=up).grid(row=bt_up_row, column=bt_up_col)
    ttk.Button(tkinter_win, text='BACK TO TOP.', command=top).grid(row=bt_top_row, column=bt_top_col)
    tkinter_win.mainloop()
