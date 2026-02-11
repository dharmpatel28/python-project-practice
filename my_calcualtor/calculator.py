import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import Image

#convert from jpg to ico
# img = Image.open('download.jpg')
# img.save('download.ico')

application = tk.Tk()
application.title('Dharm\'s calculator')
application.iconbitmap('download.ico')
application.configure(bg='#FDEEF4')
application.geometry('390x430')
application.resizable(0,0) # it stop minimizing and maximizing of windows

#---------------------------------------------entry box------------------------------

entry_storage=tk.StringVar()
entry = tk.Entry(application, textvariable=entry_storage,foreground='#2C3539',bg='#FFF9E3')
# entry.pack(side=tk.TOP, fill='x')
# entry.insert(0,'enter numbers') # placeholder
entry.place(x=10, y=0, width=370, height=60)

entry.focus()

# cursor towards right
position = entry.index(INSERT)
entry.icursor(position+1)



#------------------------------------buttons-----------------------------------------
def clear_all():
    entry.delete(0,tk.END)

ce = tk.Button(application,text='CE', command=clear_all, foreground='#2C3539',bg='#FAF0DD',activebackground='#1589FF')
ce.place(x=10,y=80, width=80, height=60)

def backspace():
    input = list(entry.get())
    input.pop()
    entry.delete(0,tk.END)
    entry.insert(tk.INSERT,input)

backspace=tk.Button(application,text='<--',command=backspace, foreground='#2C3539',bg='#FAF0DD',activebackground='#1589FF')
backspace.place(x=190, y=80, width=80, height=60)

def on_click(text):
    # entry.delete(0, tk.END)
    entry.insert(tk.INSERT,text)
    entry.focus()
    

one = tk.Button(application,text='1',command=lambda:on_click('1'), foreground='#2C3539',bg='#FAF0DD',activebackground='#1589FF')
one.place(x=10, y=150, width=80, height=60)

two = tk.Button(application,text='2',compound= tk.RIGHT,command=lambda:on_click('2'), foreground='#2C3539',bg='#FAF0DD',activebackground='#1589FF')
two.place(x=100, y=150, width=80, height=60)

three = tk.Button(application,text='3',command=lambda:on_click('3'), foreground='#2C3539',bg='#FAF0DD',activebackground='#1589FF')
three.place(x=190, y=150, width=80, height=60)

four = tk.Button(application,text='4',command=lambda:on_click('4'), foreground='#2C3539',bg='#FAF0DD',activebackground='#1589FF')
four.place(x=10, y=220, width=80, height=60)

five = tk.Button(application,text='5',command=lambda:on_click('5'), foreground='#2C3539',bg='#FAF0DD',activebackground='#1589FF')
five.place(x=100, y=220, width=80, height=60)

six= tk.Button(application,text='6',command=lambda:on_click('6'), foreground='#2C3539',bg='#FAF0DD',activebackground='#1589FF')
six.place(x=190, y=220, width=80, height=60)

seven = tk.Button(application,text='7',command=lambda:on_click('7'), foreground='#2C3539',bg='#FAF0DD',activebackground='#1589FF')
seven.place(x=10, y=290, width=80, height=60)

eight = tk.Button(application,text='8',command=lambda:on_click('8'), foreground='#2C3539',bg='#FAF0DD',activebackground='#1589FF')
eight.place(x=100, y=290, width=80, height=60)

nine = tk.Button(application,text='9',command=lambda:on_click('9'), foreground='#2C3539',bg='#FAF0DD',activebackground='#1589FF')
nine.place(x=190, y=290, width=80, height=60)

zero = tk.Button(application,text='0',command=lambda:on_click('0'), foreground='#2C3539',bg='#FAF0DD',activebackground='#1589FF')
zero.place(x=100, y=360, width=80, height=60)

add = tk.Button(application,text='+',command=lambda:on_click('+'), foreground='#2C3539',bg='#FAF0DD',activebackground='#1589FF')
add.place(x=290,y=80, width=80, height=60)

sub = tk.Button(application,text='-',command=lambda:on_click('-'), foreground='#2C3539',bg='#FAF0DD',activebackground='#1589FF')
sub.place(x=290, y=150, width=80, height=60)

mul = tk.Button(application,text='*',command=lambda:on_click('*'), foreground='#2C3539',bg='#FAF0DD',activebackground='#1589FF')
mul.place(x=290, y=220, width=80, height=60)

divide = tk.Button(application,text='/',command=lambda:on_click('/'), foreground='#2C3539',bg='#FAF0DD',activebackground='#1589FF')
divide.place(x=290, y=290, width=80, height=60)

def result():
    value=str(eval(entry_storage.get()))
    entry.delete(0,tk.END)
    entry.insert(0,value)

equal = tk.Button(application,text='=',command=result, foreground='#2C3539',bg='#FAF0DD',activebackground='#1589FF')
equal.place(x=290, y=360, width=80, height=60)

#-----------------------functionality------------------------------------




application.mainloop()