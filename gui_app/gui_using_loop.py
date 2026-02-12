import tkinter as tk
from tkinter import ttk

win2 = tk.Tk()
win2.title('loop')

# labels
labels = ['name:', 'age:', 'city:', 'gender:']

for i in range(len(labels)):
    # currentlabel= 'label' + str(i)
    # print(currentlabel)    

    currentlabel = ttk.Label(win2, text=labels[i])
    currentlabel.grid(row=i,column=0,sticky=tk.W)

# empty box
storage = {
    'name':tk.StringVar(),
    'age':tk.StringVar(),
    'city':tk.StringVar(),
    'gender':tk.StringVar()
}

count =0
for i in storage:
    
    current_entrybox = ttk.Entry(win2, width=20, textvariable=storage[i])
    current_entrybox.grid(row=count,column=1)
    count += 1

# button
def submit():
    # print(storage['name'].get())
    # print(storage.get('age').get())
    # print(storage['gender'].get())
    # print(storage['city'].get())
            # or
    for j in storage:
        print(storage[j].get())


button1 = ttk.Button(win2, text='submit', command= submit)
button1.grid(row=5,columnspan=2)

win2.mainloop()