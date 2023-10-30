import os
import logging


def create_folders(folder_name, desktop_path, E_path, F_path, custom_text=""):
    # Add the custom text to the folder names
    folder_name = f"{folder_name}_{custom_text}"

    folder_path = os.path.join(desktop_path, f"{folder_name}_DRV")

    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
        logging.info(f"Folder '{folder_name}' created on the desktop.")

    destination_folders = [
        os.path.join(desktop_path, f"{folder_name}_DNG"),
        os.path.join(E_path, f"{folder_name}_DNG"),
        os.path.join(F_path, f"{folder_name}_DNG")
    ]

    for destination_folder in destination_folders:
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)
            logging.info(f"Folder '{destination_folder}' created.")
