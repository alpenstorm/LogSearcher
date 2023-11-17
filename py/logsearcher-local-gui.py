import os
import ctypes
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from tkinter import *

ctypes.windll.shcore.SetProcessDpiAwareness(True)

#tk window
root = tk.Tk()
root.geometry("1280x720")
root.title("LogSearcher - Local Searcher")

# import buttons
widget_browse_def = PhotoImage(file='widgets/browse-def (Custom).png')
widget_browse_hover = PhotoImage(file='widgets/browse-hover (Custom).png')
widget_browse_pressed = PhotoImage(file='widgets/browse-pressed (Custom).png')
widget_submit_def = PhotoImage(file='widgets/submit-def (Custom).png')
widget_submit_hover = PhotoImage(file='widgets/submit-def (Custom).png')
widget_submit_pressed = PhotoImage(file='widgets/submit-click (Custom).png')
#widget_searchbar = PhotoImage(file='widgets/search.png') #commented out because searchbar doesn't work - might readd later?

# button functions
def changeOnHover(button, imgonhover, imgonleave):
    button.bind("<Enter>", func=lambda e: button.config(image=imgonhover))
    button.bind("<Leave>", func=lambda e: button.config(image=imgonleave))

def browseFiles():
    fp_button.config(image=widget_browse_pressed)
    global filename
    cwd = os.getcwd()
    filename = filedialog.askopenfilename(
        initialdir= cwd,
        title= "Select a File",
        filetypes= (("Log Files","*.log"),
                     ("Text Files", "*.txt"),
                     ("all files","*."))
    )
    submit_searcht()

def savefiles():
    w2fp.config(image=widget_browse_pressed)
    global sfilename
    cwd = os.getcwd()
    sfilename = filedialog.asksaveasfilename(
        initialdir= cwd,
        title="Save As:",
        filetypes= (("Log Files","*.log"),
                     ("Text Files", "*.txt"),
                    ("LogSearcher Output","*.lsout")),
        initialfile= "output.log",
        defaultextension= "*.log"
    )
    print(sfilename)
    submit_filep()

def submit_filep():
    global fn
    fn = filename
    
    try:
        global fileHandle
        fileHandle = open(fn, "r", encoding="utf8", errors="ignore")
    except:
        messagebox.showerror("Warning", "Could not read file!")
        submit_filep(fn)

def submit_searcht():
    messagebox.showinfo("Notice", "LogSearcher GUI will create a file with the search terms!")

def submit_filenames():

    w3submit.config(image=widget_submit_pressed)

    trm = trm_entry.get()

    lc = 0
    tc = 0

    with open(sfilename, "w") as output:
        output.write("------OUTPUT FILE CREATED------"+ "\n\n")

        for line in fileHandle:
            line = line.rstrip()
            lc += 1
            if trm in line:
                tc += 1
                output.write(line + "\n\n")
            else:
                continue
    
        output.write("------OUTPUT FILE TERMINATED------")

        messagebox.showinfo('Terms Found', message= f'Found {tc} terms\nIn {lc} lines\nFrom: {fn}')
        res = messagebox.askquestion('Search Again?', 'Do you want to search another file?')

        if res == 'yes':
            root.deiconify()
        else:
            root.destroy()
            

#tk labels
lsl       = Label(root, text="Local Searcher", font=("Roboto,", 56))
fto       = Label(root, text="File To Open", font=("Roboto", 24))
sfl       = Label(root, text="File to Save", font=("Roboto", 24))
stl       = Label(root, text="Enter Search Term", font=("Roboto", 24))

#tk buttons
fp_button = Button(root, image=widget_browse_def, command=browseFiles, borderwidth=0)
w3submit  = Button(root, image=widget_submit_def, command=submit_filenames, borderwidth=0)
w2fp      = Button(root, image=widget_browse_def, command=savefiles, borderwidth=0)

# tk entry
trm_entry = tk.Entry(root, width=40, font=("Roboto", 16))

# top label
lsl.pack(side=tk.TOP)

#group 1
fto.pack(side=tk.LEFT, padx=10, pady=10, anchor=CENTER)
fp_button.pack(side=tk.LEFT, padx=10, pady=10, anchor=CENTER)

#group 2
sfl.pack(side=tk.LEFT, padx=10, pady=10, anchor=S)
w2fp.pack(side=tk.LEFT, padx=10, pady=10, anchor=S)

#group 3
stl.pack(side=tk.BOTTOM, padx=10, pady=10, anchor=S)
trm_entry.pack(side=tk.BOTTOM, padx=10, pady=10, anchor=S)
w3submit.pack(side=tk.BOTTOM, padx=10, pady=10, anchor=S)

#hovers
changeOnHover(fp_button, widget_browse_hover, widget_browse_def)
changeOnHover(w2fp, widget_browse_hover, widget_browse_def)
changeOnHover(w3submit, widget_submit_hover, widget_submit_def)

#main loop
root.mainloop()
