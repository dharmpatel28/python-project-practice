import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title('tab control notebook')

nb = ttk.Notebook(win) # notebook class
page1 = ttk.Frame(nb)
page2 = ttk.Frame(nb)

nb.add(page1, text='page-1')
nb.add(page2, text='page-2')

#here we cannot use grid because we need frame in whole page 
nb.pack(expand=True, fill='both') # both:x and y, x: horizontally, y: vertically

# labels
labels = ['name:', 'age:', 'city:', 'gender:']

for i in range(len(labels)):
    currentlabel = ttk.Label(page1, text=labels[i]) # label frame.................
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
    
    current_entrybox = ttk.Entry(page1, width=20, textvariable=storage[i])
    current_entrybox.grid(row=count,column=1) 
    count += 1


#page -2
label1 = ttk.Label(page2, text='enter your hobby: ')
label1.grid(row=0, column=0)

answer1 = ttk.Entry(page2, width=20)
answer1.grid(row=0, column=1)

win.mainloop()