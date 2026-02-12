import tkinter as tk
from tkinter import ttk
from tkinter import *
import webbrowser # for button link
from tkinter import messagebox as mb
from tkcalendar import DateEntry # for dob1

signupscreen=tk.Tk()
signupscreen.title('Sign up page')
signupscreen.geometry('1940x1080')

labelframe1=ttk.LabelFrame(signupscreen,text='Sign Up')
labelframe1.place(x=600,y=200,width=300,height=400) 

def open_login():
    signupscreen.destroy()
    import authorization


def validatesignup():
    n =namestorage.get()
    s=surnamestorage.get()
    c=contactstorage.get()
    d=calendarstorage.get()
    print(f'{n},{s},{c},{d}')

    if n == '' or s==''or c=='' or d=='':
        mb.showerror('error', ' Invalid Details')
    else:
        mb.showinfo('success', 'Account created')

namelabel=ttk.Label(labelframe1,text='Name:')
namelabel.grid(row=0,column=0,padx=15,pady=10)

surnamelabel=ttk.Label(labelframe1,text='surname:')
surnamelabel.grid(row=1,column=0,padx=15,pady=10)

contactlabel=ttk.Label(labelframe1,text='contact:')
contactlabel.grid(row=2,column=0,padx=15,pady=10)

doblabel=ttk.Label(labelframe1,text='dob:')
doblabel.grid(row=3,column=0,padx=0,pady=10)

doblabel1=ttk.Label(labelframe1,text='dob1:')
doblabel1.grid(row=4,column=0,padx=15,pady=10)

namestorage=tk.StringVar()
nameentry= ttk.Entry(labelframe1,width=20,textvariable=namestorage)
nameentry.grid(row=0,column=1,padx=5,pady=10)

surnamestorage=tk.StringVar()
surnameentry= ttk.Entry(labelframe1,width=20,textvariable=surnamestorage)
surnameentry.grid(row=1,column=1,padx=5,pady=10)

contactstorage=tk.IntVar()
contactentry= ttk.Entry(labelframe1,width=20,textvariable=contactstorage)
contactentry.grid(row=2,column=1,padx=5,pady=10)

calendarstorage=tk.StringVar()
calendar=DateEntry(labelframe1,selectedmode='day',width=15,textvariable=calendarstorage)
calendar.grid(row=4,column=1)

createbutton=ttk.Button(labelframe1,text='Create Account',width=20,command=validatesignup)
createbutton.place(x=70,y=230,width=150,height=30)


loginbutton=ttk.Button(labelframe1,text='Already have account , Login',width=20,command=open_login)
loginbutton.place(x=50,y=270,width=180,height=30)
signupscreen.mainloop()