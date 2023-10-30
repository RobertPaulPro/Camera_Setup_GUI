import os


def source_folder_input():
    # Prompt the user for the SD card drive letter
    source_folder = None
    while source_folder is None:
        drive_letter = input("Enter the camera card drive letter (e.g., G, J, etc...): ")
        potential_source_folder = f"{drive_letter}:\\DCIM"
        if os.path.exists(potential_source_folder):
            source_folder = potential_source_folder
        else:
            print("Invalid drive letter or SD card not found. Please try again.")

    return source_folder


def custom_text_input():
    # Prompt the user for the custom text
    custom_text = input("Enter File Name: ")
    return custom_text

