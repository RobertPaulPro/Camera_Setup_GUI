import os
import shutil
import logging

def copy_files(source_folder, folder_name, desktop_path, E_path, F_path, custom_text=""):
    # Add the custom text to the folder names
    folder_name = f"{folder_name}_{custom_text}"

    destination_folders = [
        os.path.join(desktop_path, f"{folder_name}_DNG"),
        os.path.join(E_path, f"{folder_name}_DNG"),
        os.path.join(F_path, f"{folder_name}_DNG")
    ]

    for destination_folder in destination_folders:
        if not os.path.exists(destination_folder):  # Corrected the condition
            os.makedirs(destination_folder)
            logging.info(f"Folder '{destination_folder}' created.")

    for root, dirs, files in os.walk(source_folder):
        for dir in dirs:
            source_subfolder = os.path.join(root, dir)
            for destination_folder in destination_folders:
                destination_subfolder = os.path.join(destination_folder, os.path.relpath(source_subfolder, source_folder))
                os.makedirs(destination_subfolder, exist_ok=True)
                for file in os.listdir(source_subfolder):
                    source_file = os.path.join(source_subfolder, file)
                    destination_file = os.path.join(destination_subfolder, file)
                    try:
                        shutil.copy2(source_file, destination_file)
                        logging.info(f"File copied: {source_file} -> {destination_file}")
                    except Exception as e:
                        logging.error(f"Error copying {source_file}: {str(e)}")

