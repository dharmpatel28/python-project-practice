import tkinter as tk
from tkinter import ttk

win2 = tk.Tk()
win2.title('lable frame')

label_frame = ttk.LabelFrame(win2, text='enter your details below: ')
label_frame.grid(row=0,column=0, padx= 50,pady=10)

# labels
labels = ['name:', 'age:', 'city:', 'gender:']

for i in range(len(labels)):
    # currentlabel= 'label' + str(i)
    # print(currentlabel)    

    currentlabel = ttk.Label(label_frame, text=labels[i]) # label frame.................
    currentlabel.grid(row=i,column=0,sticky=tk.W)

# entry box
storage = {
    'name':tk.StringVar(),
    'age':tk.StringVar(),
    'city':tk.StringVar(),
    'gender':tk.StringVar()
}

count =0
for i in storage:
    
    current_entrybox = ttk.Entry(label_frame, width=20, textvariable=storage[i])
    current_entrybox.grid(row=count,column=1) 
    count += 1

def submit():
    for j in storage:
        print(storage[j].get())

button1 = ttk.Button(win2, text='submit', command= submit)
button1.grid(row=5,columnspan=2)

# another method for adding padding for all widgets
for widgets in label_frame.winfo_children():
    widgets.grid_configure(padx=4,pady=4)

win2.mainloop()