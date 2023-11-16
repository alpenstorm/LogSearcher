import os
import ctypes
import subprocess
import tkinter as tk
from tkinter import PhotoImage

ctypes.windll.shcore.SetProcessDpiAwareness(True)
cwd = os.getcwd()

# root window
root = tk.Tk()
root.title("LogSearcher - Launcher")
root.geometry("1280x720")

# import buttons
widget_local_def         = PhotoImage(file='widgets/local-def.png')
widget_local_hover       = PhotoImage(file='widgets/local-hover.png')
widget_local_pressed     = PhotoImage(file='widgets/local-pressed.png')
widget_remote_def        = PhotoImage(file='widgets/remote-def.png')
widget_remote_hover      = PhotoImage(file='widgets/remote-hover.png')
widget_remote_pressed    = PhotoImage(file='widgets/remote-pressed.png')

# functions
def local_down():
    button1.config(image=widget_local_pressed)
    subprocess.run(["python", "py/logsearcher-local-gui.py"])

def remote_down():
    button2.config(image=widget_remote_pressed)
    subprocess.run(["python", "py/logsearcher-remote-gui.py"])

def changeOnHover(button, imgonhover, imgonleave):
    button.bind("<Enter>", func=lambda e: button.config(image=imgonhover))
    button.bind("<Leave>", func=lambda e: button.config(image=imgonleave))

# buttons
button1 = tk.Button(root, command=local_down, image=widget_local_def, borderwidth=0)
button2 = tk.Button(root, command= remote_down, image=widget_remote_def, borderwidth=0)

changeOnHover(button1, widget_local_hover, widget_local_def)
changeOnHover(button2, widget_remote_hover, widget_remote_def)

# label
label = tk.Label(root, text="LogSearcher", font=("Arial", 48, "bold"))

# gui packing
label.pack(side=tk.TOP, padx=10, pady=10)
button1.pack(side=tk.TOP, anchor=tk.CENTER, padx=10, pady=10)
button2.pack(side=tk.TOP, anchor=tk.CENTER, padx=10, pady=10)

# main loop
root.mainloop()