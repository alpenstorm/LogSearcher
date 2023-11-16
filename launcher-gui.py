import os
import ctypes
import subprocess
import tkinter as tk

ctypes.windll.shcore.SetProcessDpiAwareness(True)
cwd = os.getcwd()

# root window
root = tk.Tk()
root.title("LogSearcher - Launcher")
root.geometry("1280x720")

#functions
def local_down():
    subprocess.run(["python", "py/logsearcher-local-gui.py"])

def remote_down():
    subprocess.run(["python", "py/logsearcher-remote-gui.py"])

# buttons
button1 = tk.Button(root, text="Local", height=2, width=12, font=("Arial", 16), command=local_down)
button2 = tk.Button(root, text="Remote", height=2, width=12, font=("Arial", 16), command= remote_down)

# label
label = tk.Label(root, text="LogSearcher", font=("Arial", 36, "bold"))

# gui packing
label.pack(side=tk.TOP, padx=10, pady=10)
button1.pack(side=tk.TOP, anchor=tk.CENTER, padx=10, pady=10)
button2.pack(side=tk.TOP, anchor=tk.CENTER, padx=10, pady=10)

# main loop
root.mainloop()