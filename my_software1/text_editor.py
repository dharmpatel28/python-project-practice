import tkinter as tk
from tkinter import ttk
from tkinter import font, colorchooser, filedialog, messagebox
import os

main_application = tk.Tk()
main_application.title('dharm\'s text editor')
main_application.wm_iconbitmap('icon.ico') # app icon
main_application.geometry('1200x800')

########################################--MENU--#########################################
main_menu = tk.Menu()

# file---------------------------------------
new_icon=tk.PhotoImage(file='icons/newfile.png') # add icons besides text
open_icon=tk.PhotoImage(file='icons/open.png')
save_icon=tk.PhotoImage(file='icons/save.png')
saveas_icon=tk.PhotoImage(file='icons/saveas.png')
exit_icon=tk.PhotoImage(file='icons/exit.png')

file = tk.Menu(main_menu, tearoff=False)
main_menu.add_cascade(label = 'file', menu=file)

# edit----------------------------------------------------------------------------------------
copy_icon=tk.PhotoImage(file='icons/copy.png')
paste_icon=tk.PhotoImage(file='icons/paste.png')
cut_icon=tk.PhotoImage(file='icons/cut.png')
clearall_icon=tk.PhotoImage(file='icons/clearall.png')
find_icon=tk.PhotoImage(file='icons/find.png')

edit = tk.Menu(main_menu, tearoff=False)

main_menu.add_cascade(label = 'edit', menu=edit)

# view------------------------------------------------------------------------
toolbar_icon=tk.PhotoImage(file='icons/toolbar.png')
statusbar_icon=tk.PhotoImage(file='icons/statusbar.png')

view = tk.Menu(main_menu, tearoff=False)

main_menu.add_cascade(label = 'view', menu=view)

# colortheme----------------------------------------------------------------
lightdefault_icon=tk.PhotoImage(file='icons/lightdefault.png')
lightplus_icon=tk.PhotoImage(file='icons/lightplus.png')
dark_icon=tk.PhotoImage(file='icons/dark.png')
red_icon=tk.PhotoImage(file='icons/red.png')
monokai_icon=tk.PhotoImage(file='icons/monokai.png')
night_icon=tk.PhotoImage(file='icons/night.png')

colortheme = tk.Menu(main_menu, tearoff=False)

theme_storage= tk.StringVar()
color_icons= (lightdefault_icon,lightplus_icon, dark_icon, red_icon, monokai_icon, night_icon)

color_dict= {
    'light deafault':('#000000', '#ffffff'), # text, background color
    'light plus':('#ffffff', '#474747'),
    'dark':('#c4c4c4', '#2d2d2d'), 
    'red':('#ffffff', '#ff0000'),
    'monokai':('#d3b774', '#474747'),
    'night#2C3539':('#ededed', '#6b9dc2')
}
main_menu.add_cascade(label='theme', menu=colortheme)

#################################----TOOLBAR----#################################
toolbar = ttk.Label(main_application)
toolbar.pack(side=tk.TOP, fill='x')

# fontbox
fonttuple=tk.font.families()
font_storage = tk.StringVar()
fontbox = ttk.Combobox(toolbar, width=30, textvariable = font_storage, state='readonly')
fontbox['values'] = fonttuple
fontbox.current(fonttuple.index('Arial'))
fontbox.grid(row=0,column=0, padx=5,pady=5)

#fontsize
fontsize_storage= tk.IntVar()
fontsize=ttk.Combobox(toolbar, width=5,textvariable=fontsize_storage,state='readonly')
fontsize['values']=tuple(range(2,200,2))
fontsize.current(6)
fontsize.grid(row=0,column=1,padx=5,pady=5)

# bold button
boldicon=tk.PhotoImage(file='icons/bold.png')
button1=ttk.Button(toolbar,image=boldicon)
button1.grid(row=0,column=2,padx=5,pady=5)

# italic button
italicicon=tk.PhotoImage(file='icons/italic.png')
button2=ttk.Button(toolbar,image=italicicon)
button2.grid(row=0,column=3,padx=5,pady=5)

# underline button
underlineicon=tk.PhotoImage(file='icons/underline.png')
button3=ttk.Button(toolbar,image=underlineicon)
button3.grid(row=0,column=4,padx=5,pady=5)

# alignleft button
alignlefticon=tk.PhotoImage(file='icons/alignleft.png')
button4=ttk.Button(toolbar,image=alignlefticon)
button4.grid(row=0,column=5,padx=5,pady=5)

# aligncenter button
aligncentericon=tk.PhotoImage(file='icons/aligncenter.png')
button5=ttk.Button(toolbar,image=aligncentericon)
button5.grid(row=0,column=6,padx=5,pady=5)

# alignright button
alignrighticon=tk.PhotoImage(file='icons/alignright.png')
button6=ttk.Button(toolbar,image=alignrighticon)
button6.grid(row=0,column=7,padx=5,pady=5)

# fontcolor
fontcoloricon=tk.PhotoImage(file='icons/fontcolor.png')
button7=ttk.Button(toolbar,image=fontcoloricon)
button7.grid(row=0,column=8,padx=5,pady=5)


#################################----TEXT EDITOR----#################################
texteditor = tk.Text(main_application)
texteditor.config(wrap='word', relief=tk.FLAT)

scrollbar = tk.Scrollbar(main_application)
texteditor.focus_set()
scrollbar.pack(side=tk.RIGHT, fill='y')
texteditor.pack(fill='both', expand=True)
scrollbar.config(command=texteditor.yview)
texteditor.config(yscrollcommand=scrollbar.set) # horizontal scrollbar


# font size and style functionality------------------------------------------------------
current_fontbox='Arial'
current_fontsize=14

def change_fontstyle(main_application):     # font style change
    global current_fontbox # to change the value of global variable
    current_fontbox=font_storage.get() # new selected font
    texteditor.configure(font=(current_fontbox, current_fontsize))
fontbox.bind('<<ComboboxSelected>>', change_fontstyle)    

def change_fontsize(main_application):
    global current_fontsize
    current_fontsize = fontsize_storage.get()
    texteditor.configure(font=(current_fontbox, current_fontsize))
fontsize.bind('<<ComboboxSelected>>',change_fontsize)   

# buttons functionality--------------*FONT CLASS--------------------------------------------------
# print(tk.font.Font(font=texteditor['font']).actual()) # original text
# property:{'family': 'Courier New', 'size': 11, 'weight': 'normal', 'slant': 'roman', 'underline': 0, 'overstrike': 0}

# bold button
def change_bold():
    textproperty=tk.font.Font(font=texteditor['font'])
    if textproperty.actual()['weight'] == 'normal': # weight means bold
        texteditor.configure(font=(current_fontbox, current_fontsize, 'bold'))
    if textproperty.actual()['weight'] == 'bold':
        texteditor.configure(font=(current_fontbox, current_fontsize, 'normal'))   
button1.configure(command=change_bold) 

# italic button
def change_italic():
    textproperty=tk.font.Font(font=texteditor['font'])
    if textproperty.actual()['slant'] == 'roman': # weight means bold
        texteditor.configure(font=(current_fontbox, current_fontsize, 'italic'))
    if textproperty.actual()['slant'] == 'italic':
        texteditor.configure(font=(current_fontbox, current_fontsize, 'roman'))   
button2.configure(command=change_italic)

# underline button
def change_underline():
    textproperty=tk.font.Font(font=texteditor['font'])
    if textproperty.actual()['underline'] == 0:
        texteditor.config(font=(current_fontbox,current_fontsize, 'underline'))
    if textproperty.actual()['underline'] == 1:
        texteditor.config(font=(current_fontbox,current_fontsize,'normal'))
button3.config(command = change_underline)   

# fontcolor button -----------*COLOR CHOOSER-------------------------------------
def change_fontcolor():
    color_selected=tk.colorchooser.askcolor()
# print(color_selected) # output: ((223, 164, 98), '#dfa462'), we need #dfa462 bcause easy
    texteditor.config(fg=color_selected[1]) # 1 is #dfa462
button7.configure(command = change_fontcolor)  

# align left button
def change_alignleft():
    texteditor_storage = texteditor.get(1.0, 'end')
    texteditor.tag_config('left', justify=tk.LEFT)
    texteditor.delete(1.0, tk.END)
    texteditor.insert(tk.INSERT, texteditor_storage, 'left')
button4.configure(command=change_alignleft)    

# align center button
def change_aligncenter():
    texteditor_storage= texteditor.get(1.0,'end')
    texteditor.tag_config('center', justify=tk.CENTER)
    texteditor.delete(1.0,tk.END)
    texteditor.insert(tk.INSERT, texteditor_storage, 'center')
button5.configure(command=change_aligncenter)

# align right button
def change_alignright():
    texteditor_storage=texteditor.get(1.0, 'end')
    texteditor.tag_config('right', justify=tk.RIGHT)
    texteditor.delete(1.0, tk.END)
    texteditor.insert(tk.INSERT, texteditor_storage, 'right')
button6.configure(command = change_alignright)    


#################################----STATUS BAR----#################################
statusbar = ttk.Label(text='status bar')
statusbar.pack(side=tk.BOTTOM)

textchanged=False
def change_statusbar(main_application):
    global textchanged
    if texteditor.edit_modified():
        words = len(texteditor.get(1.0,'end-1c').split()) #-1c means removing newlines
        characters = len(texteditor.get(1.0,'end-1c')) # count spaces
        # characters = len(texteditor.get(1.0,'end-1c').replace(' ','') # not count space 
        statusbar.configure(text=f'characters:{characters}, words:{words}')
    texteditor.edit_modified(False)
texteditor.bind('<<Modified>>',change_statusbar)        






############################----Main menu FUNCTIONALITY----#################################
url='' # global variable

#------------------------------------------1FILE--------------------------------------------

# new functionlaity----------------------------------------------------------------
def open_new(event=None):
    global url
    url=''
    texteditor.delete(1.0,tk.END)

file.add_command(label='new file',  image=new_icon,    compound=tk.LEFT, accelerator='Ctrl+n', command=open_new)

# file functionlaity-----------*FILEDIALOG,OS-----------------------------------------
def open_file(event=None):
    url= filedialog.askopenfilename(initialdir=os.getcwd(), title='please select file', filetypes=(('Text File', '*.txt'),('All Files', '*.*')))
    try:
        with open(url, 'r') as rf:
            texteditor.delete(1.0,tk.END)
            texteditor.insert(1.0,rf.read())
    except FileNotFoundError:
        return
    except:
        return    
    main_application.title(os.path.basename(url))    

file.add_command(label='open file', image=open_icon,   compound=tk.LEFT, accelerator='Ctrl+o', command =open_file)


# save file
def save_file(event=None):
    global url
    try:
        if url:
            content = str(texteditor.get(1.0, tk.END))
            with open(url,'w',encoding='utf-8') as wf:
                wf.write(content)
        else:
            url= filedialog.asksaveasfile(mode='w', defaultextension='.txt', filetypes=(('Text File', '*.txt'),('All Files', '*.*')))
            content2 = texteditor.get(1.0, tk.END)
            url.write(content2)
            url.close()
    except:
        return        
file.add_command(label='save file', image=save_icon,   compound=tk.LEFT, accelerator='Ctrl+s', command=save_file)

# save as file
def saveas_file(event=None):
    global url
    content3 = texteditor.get(1.0, tk.END)
    url= filedialog.asksaveasfile(mode='w', defaultextension='.txt', filetypes=(('Text File', '*.txt'),('All Files', '*.*')))
    url.write(content3)
    url.close()
file.add_command(label='save as',   image=saveas_icon, compound=tk.LEFT, accelerator='Ctrl+Alt+s', command= saveas_file)


# exit file
def exit_file(event=None):
    global url,textchanged
    try:
        if textchanged:
            mbox=messagebox.askyesnocancel('WARNING BOX', ' do you want to save this file')
            if mbox is True: # YES
                if url:
                    content4=texteditor.get(1.0,tk.END)
                    with open(url, 'w', encoding='utf-8') as wf1:
                        wf1.write(content4)
                        main_application.destroy()
                else:
                    content5=str(texteditor.get(1.0,tk.END))
                    url=filedialog.asksaveasfile(mode='w', defaultextension='.txt', filetypes=(('Text File', '*.txt'),('All Files', '*.*')))
                    url.write(content5)
                    url.close()
                    main_application.destroy()
            elif mbox is False: # NO
                main_application.destroy()
        else:
            main_application.destroy()                        
    except:
        return  

file.add_command(label='exit',image=exit_icon,   compound=tk.LEFT, accelerator='Ctrl+e', command= exit_file)

#------------------------------------------2EDIT----------------------------------------------

# edit commands
edit.add_command(label='copy',     image=copy_icon,     compound=tk.LEFT, accelerator='Ctrl+c',command=lambda:texteditor.event_generate("<Control c>"))
edit.add_command(label='paste',    image=paste_icon,    compound=tk.LEFT, accelerator='Ctrl+v',command=lambda:texteditor.event_generate("<Control v>"))
edit.add_command(label='cut',      image=cut_icon,      compound=tk.LEFT, accelerator='Ctrl+x',command=lambda:texteditor.event_generate("<Control x>"))
edit.add_command(label='clearall', image=clearall_icon, compound=tk.LEFT, accelerator='Ctrl+/b',command=lambda:texteditor.delete(1.0,tk.END))

# find functinality
def find_func(event=None):

    def find():
        word=find_entry.get()
        texteditor.tag_remove('match',1.0,tk.END)
        matches=0
        if word:
            startpos=1.0
            while True:
                startpos=texteditor.search(word,startpos,stopindex=tk.END)
                if not startpos: 
                    break
                endpos=f'{startpos}+{len(word)}c'
                texteditor.tag_add('match',startpos,endpos)
                matches=+1
                startpos=endpos
                texteditor.tag_config('match',foreground='red',background='yellow')

    def replace(event=None):
        word=find_entry.get()
        newword=replace_entry.get()
        content=texteditor.get(1.0,tk.END)
        newcontent=content.replace(word,newword)
        texteditor.delete(1.0,tk.END)
        texteditor.insert(1.0,newcontent)


    find_dialogue=tk.Toplevel()
    find_dialogue.geometry('450x200+500+200')
    find_dialogue.title('dharm')
    find_dialogue.resizable(0,0) # cannot change size

    label_frame = ttk.LabelFrame(find_dialogue  ,text='find/replace')
    label_frame.pack(pady=20)

    find_label = ttk.Label(label_frame,text='find: ')
    find_label.grid(row=0,column=0,padx=5,pady=5)
    replace_label = ttk.Label(label_frame,text='replace: ')
    replace_label.grid(row=1,column=0,padx=5,pady=5)

    find_entry = ttk.Entry(label_frame,width=20)
    find_entry.grid(row=0,column=1,padx=5,pady=5)
    replace_entry = ttk.Entry(label_frame,width=20)
    replace_entry.grid(row=1,column=1,padx=5,pady=5)

    find_button= ttk.Button(find_dialogue,text='find', command=find)
    find_button.pack(side=tk.LEFT , padx=60)
    replace_button= ttk.Button(find_dialogue,text='replace',command=replace)
    replace_button.pack(side=tk.RIGHT,padx=60)

edit.add_command(label='find', image=find_icon,compound=tk.LEFT, accelerator='Ctrl+f',command=find_func)

#----------------------------------------3VIEW---------------------------------------------

# view commands
toolbar_storage=tk.BooleanVar()
toolbar_storage.set(True)

def hide_toolbar():
    global toolbar_storage
    if toolbar_storage: # for hide
        toolbar.pack_forget()
        toolbar_storage=False
    else: # here you have to set again all things
        texteditor.pack_forget()
        statusbar.pack_forget()
        toolbar.pack(side=tk.TOP, fill=tk.X)
        texteditor.pack(fill=tk.BOTH, expand=True)
        statusbar.pack(side=tk.BOTTOM)
        toolbar_storage=True   

view.add_checkbutton(label='toolbar',onvalue=True,offvalue=0,variable=toolbar_storage,image=toolbar_icon,compound=tk.LEFT,accelerator='Ctrl+t',command=hide_toolbar)

#status bar
statusbar_storage=tk.BooleanVar()
statusbar_storage.set(True)

def hide_statusbar():
    global statusbar_storage
    if statusbar_storage:                                           
        statusbar.pack_forget()
        statusbar_storage=False
    else:
         statusbar.pack(side=tk.BOTTOM)
         statusbar_storage=True

view.add_checkbutton(label='statusbar',onvalue=1,offvalue=False,variable=statusbar_storage,image=statusbar_icon,compound=tk.LEFT, accelerator='Ctrl+q',command=hide_statusbar)

#----------------------------------------4.color theme------------------------------
# color theme functionality

def change_theme():
    chosentheme=theme_storage.get()
    availabletheme=color_dict.get(chosentheme)
    foregroundcolor,backgroundcolor=availabletheme[0],availabletheme[1]
    texteditor.config(background=backgroundcolor,fg=foregroundcolor)


# colorthemes commands
count= 0
for i in color_dict.keys():
    colortheme.add_radiobutton(label=i, image=color_icons[count], compound=tk.LEFT, variable =theme_storage,command=change_theme)
    count += 1

#----------------------------------------bind shortcut key------------------------------
main_application.bind('<Control-n>',open_new)
main_application.bind('<Control-o>',open_file)
main_application.bind('<Control-s>',save_file)
main_application.bind('<Control-Alt-s>',saveas_file)
main_application.bind('<Control-q>',exit_file)
main_application.bind('<Control-f>',find_func)
#----------------------------------------------------------------------------------------

main_application.config(menu=main_menu)
main_application.mainloop()

#-----------------------convert file into exe--------------------

# https://www.lfd.uci.edu/~gohlke/pythonlibs/#cx_freeze #1
# download link from cx_freeze #2
# save downloaded link to anywhere and copy path #3
# windows r,cmd, open cmd and write this--> pip install copied path and press enter #4
# relocate downloaded link to someehere else or delete ,but not in main app folder #5
# create setup.py file #6 
# open python file location-->setup(open file location)--> tcl folder--> copy path of tcl8.6  and paste in setup.py file
# open python file location-->setup(open file location)--> tcl folder--> copy path of tk8.6 and paste in setup.py file
# open python file location-->setup(open file location)-->DLLs--> copy '2' tcl86t.dll and tk86t.dll 
    #  and paste it where main python file and setup file is located
    # main_application.iconbitmap('icon.ico') write this in main file to add icon
# edit setup file according folder name  and application name  
# remove every other from main app folder 

# from folder open cmd by write in place of path
# in cmd : python setup.py bdist_msi(for windows), for mac(bdist_dmg)
