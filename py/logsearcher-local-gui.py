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
widget_browse_def = PhotoImage(file='widgets/browse-def.png')
widget_browse_hover = PhotoImage(file='widgets/browse-hover.png')
widget_browse_pressed = PhotoImage(file='widgets/browse-pressed.png')
widget_submit_def = PhotoImage(file='widgets/submit-def.png')
widget_submit_hover = PhotoImage(file='widgets/submit-hover.png')
widget_submit_pressed = PhotoImage(file='widgets/submit-click.png')
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
        #file_path_entry.delete(0, END)
        submit_filep(fn)
    
    global w3
    w3 = tk.Toplevel(root)
    w2.withdraw()
    w3.focus
    w3.title("LogSearcher - Local Searcher")
    w3.geometry("1280x720")

    Label(w3, text="Enter Search Term", font=("Roboto", 24)).pack(side=tk.TOP, padx=10, pady=10)
    global trm_entry
    trm_entry = tk.Entry(w3, width=40, font=("Roboto", 16))
    trm_entry.pack(side=tk.TOP, padx=10, pady=10)
    global w3submit
    w3submit = Button(w3, image=widget_submit_def, command=submit_filenames, borderwidth=0)
    w3submit.pack(side=tk.TOP, padx=10, pady=10)
    changeOnHover(w3submit, widget_submit_hover, widget_submit_def)


def submit_searcht():
    messagebox.showinfo("Notice", "LogSearcher GUI will create a file with the search terms!")

    global w2
    w2 = tk.Toplevel(root)
    root.withdraw()
    w2.focus
    w2.title("LogSearcher - Local Searcher")
    w2.geometry("1280x720")

    Label(w2, text="Save File", font=("Roboto", 24)).pack(side=tk.TOP, padx=10, pady=10)
    
    #filen_entry = tk.Entry(w3, width=40, font=("Roboto", 16))
    #filen_entry.pack(side=tk.TOP, padx=10, pady=10)
    
    #foldern_entry = tk.Entry(w3, width=40, font=("Roboto", 16))
    #foldern_entry.pack(side=tk.TOP, padx=10, pady=10)

    global w2fp
    w2fp = Button(w2, image=widget_browse_def, command=savefiles, borderwidth=0)
    w2fp.pack(side=tk.TOP, padx=10, pady=10)
    changeOnHover(w2fp, widget_browse_hover, widget_browse_def)

    #Button(w3, text="Submit", font=("Roboto", 18), command=submit_filenames).pack(side=tk.TOP, padx=10, pady=10)


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
            w3.withdraw()
            root.deiconify()
        else:
            root.destroy()
            

#tk items
Label(root, text="File To Open", font=("Roboto", 24)).pack(side=tk.TOP, padx=10, pady=10)
fp_button = Button(root, image=widget_browse_def, command=browseFiles, borderwidth=0)
fp_button.pack(side=tk.TOP, padx=10, pady=10)
#Button(root, text="Submit", font=("Roboto", 18), command=submit_filep).pack(side=tk.TOP, padx=10, pady=10)
#file_path_entry = tk.Entry(root, width=40, font=("Roboto", 16))
#file_path_entry.pack(side=tk.TOP, padx=10, pady=10)

changeOnHover(fp_button, widget_browse_hover, widget_browse_def)

#main loop
root.mainloop()
