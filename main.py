import os
import shutil
import datetime
import logging
import pyperclip
from create_folders import create_folders
from copy_files import copy_files
from user_input import source_folder_input, custom_text_input

# Prompt the user for the SD card drive letter
source_folder = source_folder_input()
custom_text = custom_text_input()
current_date = datetime.datetime.now().strftime("%y%m%d")
folder_name = f"{current_date}"
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
E_path = 'E:\\Media\\Camera_Archive'  # Change to the correct E drive path
F_path = 'F:\\Media\\Camera_Archive'  # Change to the correct F drive path
pyperclip.copy(f"{current_date}_{custom_text}_LR")

if __name__ == "__main__":
    # Call functions from other scripts and pass custom_text as an argument
    create_folders(folder_name, desktop_path, E_path, F_path, custom_text)
    copy_files(source_folder, folder_name, desktop_path, E_path, F_path, custom_text)


