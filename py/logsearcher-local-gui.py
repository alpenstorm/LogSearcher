import os
import tkinter as tk
from tkinter import messagebox
from tkinter import *

#tk window
root = tk.Tk()
root.geometry("1280x720")
root.title("LogSearcher - Local Searcher")

# button functions
def submit_filep():
    global fn
    fn = file_path_entry.get()
    
    try:
        global fileHandle
        fileHandle = open(fn, "r", encoding="utf8", errors="ignore")
    except:
        messagebox.showerror("Warning", "Could not read file!")
        file_path_entry.delete(0, END)
        submit_filep(fn)
    
    global w2
    w2 = tk.Toplevel(root)
    w2.focus
    w2.title("LogSearcher - Local Searcher")
    w2.geometry("1280x720")

    Label(w2, text="Enter Search Term", font=("Arial", 24)).pack(side=tk.TOP, padx=10, pady=10)
    trm_entry = tk.Entry(w2, width=40, font=("Arial", 16))
    trm_entry.pack(side=tk.TOP, padx=10, pady=10)
    Button(w2, text="Submit", font=("Arial", 18), command=submit_searcht).pack(side=tk.TOP, padx=10, pady=10)

    global trm
    trm = trm_entry.get()

def submit_searcht():
    messagebox.showinfo("Notice", "LogSearcher GUI will create a file with the search terms!")

    global w3
    w3 = tk.Toplevel(root)
    w3.focus
    w3.title("LogSearcher - Local Searcher")
    w3.geometry("1280x720")

    Label(w3, text="File Name", font=("Arial", 24)).pack(side=tk.TOP, padx=10, pady=10)
    
    filen_entry = tk.Entry(w3, width=40, font=("Arial", 16))
    filen_entry.pack(side=tk.TOP, padx=10, pady=10)

    Label(w3, text="File Location", font=("Arial", 24)).pack(side=tk.TOP, padx=10, pady=10)
    
    foldern_entry = tk.Entry(w3, width=40, font=("Arial", 16))
    foldern_entry.pack(side=tk.TOP, padx=10, pady=10)

    Button(w3, text="Submit", font=("Arial", 18), command=submit_filenames).pack(side=tk.TOP, padx=10, pady=10)

    global foldern
    global filen
    foldern = foldern_entry.get()
    filen = filen_entry.get()


def submit_filenames():
    
    global lc
    global tc
    lc = 0
    tc = 0

    try:
        with open(foldern + filen, "w") as output: #if you want to change the file format that the program exports to, define it here instead of ".lsout". 
            output.write("------OUTPUT FILE CREATED------"+ "\n\n")

            for line in fileHandle:
                line = line.rstrip()
                lc += 1
                if not trm in line:
                    continue
                tc += 1
                output.write(line + "\n\n")
        
            output.write("------OUTPUT FILE FINISHED------")
        
            #print("\nFound", tc, "terms \n In", lc, "lines \n From location", fn, "\n")
    
    except:
        os.mkdir(foldern)

        with open(foldern + filen, "w") as output:
            output.write("------OUTPUT FILE CREATED------"+ "\n\n")

            for line in fileHandle:
                line = line.rstrip()
                lc += 1
                if not trm in line:
                    continue
                tc += 1
                output.write(line + "\n\n")
        
            output.write("------OUTPUT FILE FINISHED------")
        
            #print("\nFound", tc, "terms \n In", lc, "lines \n From location", fn, "\n")



#tk items
Label(root, text="Enter File Path", font=("Arial", 36)).pack(side=tk.TOP, padx=10, pady=10)
file_path_entry = tk.Entry(root, width=40, font=("Arial", 16))
file_path_entry.pack(side=tk.TOP, padx=10, pady=10)
Button(root, text="Submit", font=("Arial", 24), command=submit_filep).pack(side=tk.TOP, padx=10, pady=10)

#main loop
root.mainloop()
