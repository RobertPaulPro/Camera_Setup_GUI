import shutil
import os
from send2trash import send2trash

# Define the source folder path on your desktop
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
folder_name_1 = input("Enter the name of the LR folder to move: ")

# Ask the user if they want to provide a second folder
copy_second_folder = input("Do you want to move a second folder? (yes/no): ")

if copy_second_folder.lower() == "yes":
    folder_name_2 = input("Enter the name of the DRV folder to move: ")
    source_folder_2 = os.path.join(desktop_path, folder_name_2)
    copy_folder_2 = True
else:
    copy_folder_2 = False

# Ask the user if they want to provide a third folder
copy_third_folder = input("Do you want to move a third folder? (yes/no): ")

if copy_third_folder.lower() == "yes":
    folder_name_3 = input("Enter the name of the DNG to move: ")
    source_folder_3 = os.path.join(desktop_path, folder_name_3)
    copy_folder_3 = True
else:
    copy_folder_3 = False

source_folder_1 = os.path.join(desktop_path, folder_name_1)

# Define the destination paths for the two hard drives
destination_drive_1 = 'E:\\Media\\Camera_Archive'
destination_drive_2 = 'F:\\Media\\Camera_Archive'

try:
    # Copy the first folder to the first hard drive
    shutil.copytree(source_folder_1, os.path.join(destination_drive_1, folder_name_1))
    print(f"Folder '{folder_name_1}' copied to {destination_drive_1}")

    # Copy the first folder to the second hard drive
    shutil.copytree(source_folder_1, os.path.join(destination_drive_2, folder_name_1))
    print(f"Folder '{folder_name_1}' copied to {destination_drive_2}")

    # Move the first folder to the recycle bin
    send2trash(source_folder_1)
    print(f"Folder '{folder_name_1}' moved to the recycle bin")

    if copy_folder_2:
        # Copy the second folder to the first hard drive
        shutil.copytree(source_folder_2, os.path.join(destination_drive_1, folder_name_2))
        print(f"Folder '{folder_name_2}' copied to {destination_drive_1}")

        # Copy the second folder to the second hard drive
        shutil.copytree(source_folder_2, os.path.join(destination_drive_2, folder_name_2))
        print(f"Folder '{folder_name_2}' copied to {destination_drive_2}")

        # Move the second folder to the recycle bin
        send2trash(source_folder_2)
        print(f"Folder '{folder_name_2}' moved to the recycle bin")

    if copy_folder_3:
        # Move the third folder to the recycle bin
        send2trash(source_folder_3)
        print(f"Folder '{folder_name_3}' moved to the recycle bin")

except shutil.Error as e:
    print(f"Error: {e}")

except Exception as e:
    print(f"An error occurred: {e}")
