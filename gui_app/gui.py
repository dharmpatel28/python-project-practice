# create gui app using tkinter in python

#starter code : this 3 is compulsary ..
# import tkinter    # 0r import tkinter from * : it import everything

#starter code : this 3 is compulsary ..
import tkinter as tk #1 # preferable
from tkinter import ttk # more designing than dk
from csv import DictWriter
import os

win1 = tk.Tk() #2 # class
win1.title('first GUI app')


# create label----------------------------------------------------------------------------
name_label = ttk.Label(win1, text='enter your name: ')
name_label.grid(row=0, column=0, sticky=tk.W) #position, ttk.W: stick pos. of label in west
# .pack() is also used for position but it print in center

email_label = ttk.Label(win1, text = 'enter your email: ', foreground='green')
email_label.grid(row=1, column=0, sticky=tk.W)

age_label = ttk.Label(win1, text = 'Enter your age: ')
age_label.grid(row=2, column=0, sticky=tk.W)

gender_label = ttk.Label(win1, text='select gender:')
gender_label.grid(row=3, column=0, sticky=tk.W)

occupation_label = ttk.Label(win1, text = 'select occuapation: ')
occupation_label.grid(row=4, column=0, sticky=tk.W)


# create entry box and focus,text-colour------------------------------------------------------------
name_store = tk.StringVar() # it store user input
name_entrybox = ttk.Entry(win1, width=20, textvariable=name_store, foreground = '#2C3539')
name_entrybox.grid(row=0, column=1)
name_entrybox.focus() # to set cursor by default..........................

email_store = tk.StringVar() # it store user input
email_entrybox = ttk.Entry(win1, width=20, textvariable=email_store)
email_entrybox.grid(row=1, column=1)

age_store = tk.IntVar() # it store user input
age_entrybox = ttk.Entry(win1, width=20, textvariable=age_store)
age_entrybox.grid(row=2, column=1)


#combo box:male ,female-------------------------------------------------------------------
gender_store = tk.StringVar()
gender_combobox = ttk.Combobox(win1, width=18, textvariable=gender_store, state='readonly') # readonly means, it stop user to write in combobox
gender_combobox['values'] = ('male','female', 'other')
gender_combobox.current(0) # to show something on combobox by default
gender_combobox.grid(row=3,column=1)


# radio button------------------------------*(variable)----------------------------------
occupation_store = tk.StringVar()
radio1 = ttk.Radiobutton(win1, text='student', value='student', variable=occupation_store)
radio1.grid(row=4,column=1)

radio2 = ttk.Radiobutton(win1, text='teacher', value='teacher', variable=occupation_store)
radio2.grid(row=4,column=2)


# check button_-------------------------------*(columnspan)-----------------------------
select_store = tk.IntVar()
select = ttk.Checkbutton(win1, text='please accept terms and condition of app', variable = select_store)
select.grid(row=5, columnspan=2) # 2 column selected


# buttons---------------------------------------------------------------------------------
# def submit(): # working submit button
#     username = name_store.get()  # get method
#     userage = age_store.get()
#     useremail = email_store.get()
#     usergender = gender_store.get()
#     useroccupation = occupation_store.get()
    
#     if select_store.get() == 0:
#         subscribed = 'no'
#     else:
#         subscribed = 'yes'  

#     print(f'{username} is {userage} years old')
#     print(f'gender is {usergender} and occupation is {useroccupation}')
#     print(f'subscription status: {subscribed}')
#     print(f'mail id: {useremail}')

# how to write in text file
    # with open('file1.txt','a') as f:
    #     f.write(f'{username},{userage},{usergender},{useroccupation},{subscribed},{useremail}\n')

# how to clear input from app after click submit button
    # name_entrybox.delete(0, tk.END)
    # email_entrybox.delete(0, tk.END)
    # age_entrybox.delete(0, tk.END)

# how to change colour of label after click submit button
#     name_label.configure(foreground= '#2C3539')

# submit_button = ttk.Button(win1, text = 'Submit', command=submit)
# submit_button.grid(row=6, column=0)


# how to write in csv file

def submit(): # working submit button
    username = name_store.get()  # get method
    userage = age_store.get()
    useremail = email_store.get()
    usergender = gender_store.get()
    useroccupation = occupation_store.get()
    
    if select_store.get() == 0:
        subscribed = 'no'
    else:
        subscribed = 'yes'

    with open('file2.csv', 'a', newline='') as f:
        dict_writer = DictWriter(f, fieldnames=['USERNAME', 'USERAGE','USERGENDER','USEROCCUPATION', 'SUBSCRIBED', 'USEREMAIL'])
        if os.stat('file2.csv').st_size == 0: # to check if file is empty or not, because repetition of header
            dict_writer.writeheader()

        dict_writer.writerow({
            'USERNAME': username,
            'USERAGE':userage,
            'USERGENDER':usergender,
            'USEROCCUPATION':useroccupation, 
            'SUBSCRIBED':subscribed, 
            'USEREMAIL' : useremail
        })    

        name_entrybox.delete(0, tk.END)
        email_entrybox.delete(0, tk.END)
        age_entrybox.delete(0, tk.END)
        
        
submit_button = ttk.Button(win1, text = 'Submit', command=submit)
submit_button.grid(row=6, column=0)    

win1.mainloop() #3 # used to prevent windows , closed automatically