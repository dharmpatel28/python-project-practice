# type of popup boxes:
# 1: tk.showinfo
# 2: tk.showerror
# 3: tk.showwarning


import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mbox

win=tk.Tk()
win.title('popup box')

label_frame = tk.LabelFrame(win,text='details')
label_frame.grid(row=0,column=0,padx=60,pady=20)

#label
label_name= ttk.Label(label_frame,text='enter your name please: ', font = ('Helvetica', 14,'italic') )
label_name.grid(row=0,column=0,padx=5,pady=5)

label_age = ttk.Label(label_frame,text='enter your age please: ', font = ('Times new roman', 14,'italic'))
label_age.grid(row=0,column=1,padx=5,pady=5)

#entry
name_storage = tk.StringVar()
name_entry = ttk.Entry(label_frame,width=30,textvariable=name_storage)
name_entry.grid(row=1,column=0,padx=5,pady=5)
name_entry.focus()

age_storage = tk.StringVar()
age_entry = ttk.Entry(label_frame,width=30,textvariable=age_storage)
age_entry.grid(row=1,column=1,padx=5,pady=5)

#buttons
def submit():
    print('function called')

    # mbox.showinfo('title', 'meesage want to pass')
    # mbox.showerror('error', 'invalid input')
    # mbox.showwarning('warning', 'plug your device')

    name = name_storage.get()
    age = age_storage.get()    

    if name == '' or age == '':
        mbox.showerror('empty input', 'please provide input')
    else:
        try:
            age = int(age)
        except ValueError:
            mbox.showerror('age error', 'only digits are allowed in age field')
        else:
            if age < 18:
                mbox.showwarning('age error', 'you are not 18+') 
            else:
                mbox.showinfo('info', f'{name}, your age is {age}' )       


button1 = ttk.Button(win, text='submit', command=submit)
button1.grid(row=1,columnspan=2)    

win.mainloop()