import os
import ctypes
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from winsound import *
from tkinter import *

try:
    ctypes.windll.shcore.SetProcessDpiAwareness(True)
except:
    pass

#tk window
root = tk.Tk()
root.geometry("1280x720")
root.title("LogSearcher - Local Searcher")


# import buttons
widget_browse_def     = PhotoImage(file='widgets/browse-def (Custom).png')
widget_browse_hover   = PhotoImage(file='widgets/browse-hover (Custom).png')
widget_browse_pressed = PhotoImage(file='widgets/browse-pressed (Custom).png')
widget_submit_def     = PhotoImage(file='widgets/submit-def (Custom).png')
widget_submit_hover   = PhotoImage(file='widgets/submit-hover (Custom).png')
widget_submit_pressed = PhotoImage(file='widgets/submit-click (Custom).png')
widget_banner         = PhotoImage(file="widgets/banner-local.png")
#widget_searchbar     = PhotoImage(file='widgets/search.png') #commented out because searchbar doesn't work - might readd later?

# button functions
def playSound():
    PlaySound('sound/sound_btn.wav', SND_FILENAME)

def changeOnHover(button, imgonhover, imgonleave):
    button.bind("<Enter>", func=lambda e: button.config(image=imgonhover))
    button.bind("<Leave>", func=lambda e: button.config(image=imgonleave))

def delTempText(e):
    trm_entry.delete(0, "end")
    trm_entry.config(fg="black")

def browsefiles():
    playSound()
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
    ifp_entry.insert(0, filename)

def savefiles():
    playSound()
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
    ofp_entry.insert(0, sfilename)
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

def submit_filenames():
    playSound()
    w3submit.config(image=widget_submit_pressed)
    trm = trm_entry.get()

    if trm == '':
        messagebox.showwarning("Warning", "No Search Term!")

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
        again = messagebox.askquestion('Search Again?', 'Do you want to search again?')
        
        if again == "yes":
            same = messagebox.askquestion('Same File?', 'Same file?')
            if same == "yes":
                pass
            else:
                ifp_entry.delete(0, "end")
                ofp_entry.delete(0, "end")
        else:
            root.destroy()

#tk labels
lsl       = Label(root, image=widget_banner)
fto       = Label(root, text="File To Open", font=("Roboto", 24))
sfl       = Label(root, text="File to Save", font=("Roboto", 24))
stl       = Label(root, text="Enter Search Term:", font=("Roboto", 24))
ifp       = Label(root, text="Input File Path:", font=("Roboto", 16))
ofp       = Label(root, text="Output File Path:", font=("Roboto", 16))

#tk buttons
fp_button = Button(root, image=widget_browse_def, command=browsefiles, borderwidth=0)
w2fp      = Button(root, image=widget_browse_def, command=savefiles, borderwidth=0)
w3submit  = Button(root, image=widget_submit_def, command=submit_filenames, borderwidth=0)

#tk entries
trm_entry = tk.Entry(root, width=24, font=("Roboto", 24))
ifp_entry = tk.Entry(root, width=18, font=("Roboto", 16))
ofp_entry = tk.Entry(root, width=16, font=("Roboto", 16))

# top label
lsl.pack(side=tk.TOP)

# group 1
fto.place(x=178, y=225, anchor=W, bordermode=OUTSIDE)
fp_button.place(x=380, y=225, anchor=W, bordermode=OUTSIDE)
ifp.place(x=177, y=280, anchor=W, bordermode=OUTSIDE)
ifp_entry.place(x=325, y=280, anchor=W, bordermode=OUTSIDE)

#group 2
sfl.place(x=730, y=225, anchor=W, bordermode=OUTSIDE)
w2fp.place(x=926, y=225, anchor=W, bordermode=OUTSIDE)
ofp.place(x=730, y=280, anchor=W, bordermode=OUTSIDE)
ofp_entry.place(x=895, y=280, anchor=W, bordermode=OUTSIDE)

#group 3
stl.place(x=178, y=425, anchor=W, bordermode=OUTSIDE)
trm_entry.place(x=465, y=425, anchor=W, bordermode=OUTSIDE)
w3submit.place(x=910, y=425, anchor=W, bordermode=OUTSIDE)

#trm_entry cfig
trm_entry.insert(0, "Search Term...")
trm_entry.config(fg="gray")
trm_entry.bind("<FocusIn>", delTempText)

#hovers
changeOnHover(fp_button, widget_browse_hover, widget_browse_def)
changeOnHover(w2fp, widget_browse_hover, widget_browse_def)
changeOnHover(w3submit, widget_submit_hover, widget_submit_def)

#main loop
root.mainloop()
