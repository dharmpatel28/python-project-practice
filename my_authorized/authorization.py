import tkinter as tk
from tkinter import ttk
from tkinter import *
import webbrowser # for button link
from tkinter import messagebox as mb
from tkcalendar import DateEntry # for dob1
from PIL import Image

loginscreen=tk.Tk()
loginscreen.title('Login Page')
loginscreen.geometry('1940x1080')

labelframe=ttk.LabelFrame(loginscreen,text='Login')
labelframe.place(x=600,y=200,width=300,height=400)  

def open_signin():
    loginscreen.destroy()
    import signup

# id pass functionality----------------------------------------------------------------
def validatelogin():
    currentid=idstorage.get()
    currentpassword=passwordstorage.get()
    if currentid == '' or currentpassword == '':
        mb.showerror('Invalid Input', 'Please enter correct id and password')
    else:
        mb.showinfo('successful', 'Login successful')
        print(f'id:{currentid}, password:{currentpassword}')

idlabel=ttk.Label(labelframe,text='Id:')
idlabel.grid(row=0,column=0,padx=15,pady=10)

passwordlabel=ttk.Label(labelframe,text='Password:')
passwordlabel.grid(row=1,column=0,padx=15,pady=10)

idstorage=tk.StringVar()
identry= ttk.Entry(labelframe,width=20,textvariable=idstorage)
identry.grid(row=0,column=1,padx=5,pady=10)

# password functionality----------------------------------------------------------------
img1= Image.open('openeye.png')
size = (18,18)
img1.thumbnail(size)
img1.save('openeye1.png')

img2= Image.open('closeeye.png')
size = (18,18)
img2.thumbnail(size)
img2.save('closeeye1.png')

def hide_pass():
    openeyeimage.config(file='closeeye1.png')
    passwordentry.config(show='*')
    openeyebtn.configure(command=show_pass)

def show_pass():
    openeyeimage.config(file='openeye1.png')
    passwordentry.config(show='')
    openeyebtn.config(command=hide_pass)

passwordstorage=tk.StringVar()

openeyeimage=tk.PhotoImage(file='openeye1.png')
closeeyeimage=tk.PhotoImage(file='closeeye1.png')

passwordentry= ttk.Entry(labelframe,width=20,textvariable=passwordstorage)
passwordentry.grid(row=1,column=1,padx=5,pady=10)

openeyebtn=ttk.Button(labelframe,image=openeyeimage,command=hide_pass)
openeyebtn.place(x=240,y=50,width=30,height=30)
3
continuebtn= ttk.Button(labelframe, text='Continue', width=35,command=validatelogin)
continuebtn.grid(row=2,columnspan=2,padx=15,pady=10)


# social app functionality----------------------------------------------------------------
sociallabel=ttk.Label(labelframe,text='or connect with social media')
sociallabel.grid(row=3,columnspan=2,padx=15,pady=10)

url1='https://www.facebook.com/login/'
def fb_click():
    webbrowser.open_new(url1)
facebookbtn= ttk.Button(labelframe, text='Sign in with Facebook', width=35,command=fb_click)
facebookbtn.grid(row=4,columnspan=2,padx=15,pady=10)

url='https://accounts.google.com/v3/signin/identifier?dsh=S-200725741%3A1687330417557190&continue=https%3A%2F%2Fmyaccount.google.com%2F&sacu=1&flowName=GlifWebSignIn&flowEntry=AddSession'
def on_click():
    webbrowser.open_new(url)
googlebtn= ttk.Button(labelframe, text='Sign in with Google', width=35,command=on_click)
googlebtn.grid(row=5,columnspan=2,padx=15,pady=10)

# signup functionality------------------------------------------------------------------    

signuplabel=ttk.Label(labelframe,text='or sign up')
signuplabel.grid(row=6,columnspan=2,padx=15,pady=10)

signupbtn= ttk.Button(labelframe, text='Sign up',width=35,command=open_signin)
signupbtn.grid(row=7,columnspan=2,padx=15,pady=10)

loginscreen.mainloop()
