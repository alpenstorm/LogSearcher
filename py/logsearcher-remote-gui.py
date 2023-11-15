import os
import ctypes
import urllib.request
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from tkinter import *

ctypes.windll.shcore.SetProcessDpiAwareness(True)

#tk window
root = tk.Tk()
root.geometry("1280x720")
root.title("LogSearcher - Remote Searcher")

# button functions
# def browseFiles():
#     global filename
#     cwd = os.getcwd()
#     filename = filedialog.askopenfilename(
#         initialdir= cwd,
#         title= "Select a File",
#         filetypes= (("Log Files","*.log"),
#                      ("Text Files", "*.txt"),
#                      ("all files","*."))
#     )
#     submit_searcht()

def savefiles():
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
    fn = file_path_entry.get()
    
    try:
        global fileHandle
        fileHandle = urllib.request.urlopen(fn)
    except:
        messagebox.showerror("Warning", "Could not read file!")
        file_path_entry.delete(0, END)
        submit_filep(fn)
    
    global w3
    w3 = tk.Toplevel(root)
    w2.withdraw()
    w3.focus
    w3.title("LogSearcher - Local Searcher")
    w3.geometry("1280x720")

    Label(w3, text="Enter Search Term", font=("Arial", 24)).pack(side=tk.TOP, padx=10, pady=10)
    global trm_entry
    trm_entry = tk.Entry(w3, width=40, font=("Arial", 16))
    trm_entry.pack(side=tk.TOP, padx=10, pady=10)
    Button(w3, text="Submit", font=("Arial", 18), command=submit_filenames).pack(side=tk.TOP, padx=10, pady=10)

def submit_searcht():
    messagebox.showinfo("Notice", "LogSearcher GUI will create a file with the search terms!")

    global w2
    w2 = tk.Toplevel(root)
    root.withdraw()
    w2.focus
    w2.title("LogSearcher - Local Searcher")
    w2.geometry("1280x720")

    Label(w2, text="Save File", font=("Arial", 24)).pack(side=tk.TOP, padx=10, pady=10)
    
    #filen_entry = tk.Entry(w3, width=40, font=("Arial", 16))
    #filen_entry.pack(side=tk.TOP, padx=10, pady=10)
    
    #foldern_entry = tk.Entry(w3, width=40, font=("Arial", 16))
    #foldern_entry.pack(side=tk.TOP, padx=10, pady=10)

    Button(w2, text="Browse Files", font=("Arial", 18), command=savefiles).pack(side=tk.TOP, padx=10, pady=10)
    #Button(w3, text="Submit", font=("Arial", 18), command=submit_filenames).pack(side=tk.TOP, padx=10, pady=10)


def submit_filenames():

    trm = trm_entry.get()

    lc = 0
    tc = 0

    with open(sfilename, "w") as output:
        output.write("------OUTPUT FILE CREATED------"+ "\n\n")

        for line in fileHandle:
            line = line.decode().strip()
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
Label(root, text="URL To Open", font=("Arial", 24)).pack(side=tk.TOP, padx=10, pady=10)
#fp_button = Button(root, text="Browse Files", font=("Arial", 18), command=browseFiles).pack(side=tk.TOP, padx=10, pady=10)
file_path_entry = tk.Entry(root, width=40, font=("Arial", 16))
file_path_entry.pack(side=tk.TOP, padx=10, pady=10)
Button(root, text="Submit", font=("Arial", 18), command=submit_searcht).pack(side=tk.TOP, padx=10, pady=10)


#main loop
root.mainloop()
