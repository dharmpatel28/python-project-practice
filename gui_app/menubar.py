import tkinter as tk
from tkinter import ttk

win2 = tk.Tk()
win2.title('menubar')

# simple menu
# def func():
#     print('function called')

# menu1 = tk.Menu(win2)
# menu1.add_command(label='file', command = func)
# menu1.add_command(label='edit', command = func)
# menu1.add_command(label='selection', command = func)
# menu1.add_command(label='view', command = func)
# win2.config(menu=menu1) # here we cannot use grid or pack

# dropdown menu
def func():
    print('function called')

menu2 = tk.Menu(win2)

dropdown1 = tk.Menu(menu2, tearoff=0) # tearoff prevent showing of "---" in dropdown menu
dropdown1.add_command(label='open file', command = func)
dropdown1.add_command(label='open folder', command = func)
dropdown1.add_command(label='save', command = func)
dropdown1.add_command(label='save as', command = func)
menu2.add_cascade(label='file', menu= dropdown1)

dropdown2 = tk.Menu(menu2, tearoff=0)
dropdown2.add_command(label='undo', command = func)
dropdown2.add_command(label='cut', command = func)
dropdown2.add_command(label='copy', command = func)
dropdown2.add_command(label='paste', command = func)
menu2.add_cascade(label='edit', menu = dropdown2)

win2.config(menu=menu2)

win2.mainloop()