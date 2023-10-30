import tkinter as tk
import subprocess
import os

def run_script1():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    script_path = os.path.join(script_dir, 'main.py')
    subprocess.run(['python', script_path])

def run_script2():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    script_path = os.path.join(script_dir, 'remove_folders_main.py')
    subprocess.run(['python', script_path])

# Create the main window
window = tk.Tk()
window.title("Script Launcher")

# Create buttons to launch the scripts
button1 = tk.Button(window, text="DCIM Download", command=run_script1)
button2 = tk.Button(window, text="Camera Folder Clean-up", command=run_script2)

# Pack the buttons in the window
button1.pack()
button2.pack()

# Start the Tkinter event loop
window.mainloop()


