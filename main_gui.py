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
# Set the initial size (width x height)
window.geometry("800x600")  # Set your desired width and height

# Create a frame to center the buttons
frame = tk.Frame(window)
frame.pack(expand=True, fill='both')

# Set grid weights and row configurations for the frame
frame.grid_rowconfigure(0, weight=1)
frame.grid_columnconfigure(0, weight=1)
frame.grid_columnconfigure(1, weight=1)

# Create buttons to launch the scripts
button1 = tk.Button(frame, text="DCIM Download", command=run_script1)
button2 = tk.Button(frame, text="Camera Folder Clean-up", command=run_script2)

# Use grid to center the buttons in the frame
button1.grid(row=0, column=0, padx=10, pady=10)
button2.grid(row=0, column=1, padx=10, pady=10)

# Start the Tkinter event loop
window.mainloop()



