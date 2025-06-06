# # Import the required libraries
# import os

# # Define the location of the directory
# path =r"g:\My Drive\2025 Techs\L3 DTSD - Mrs. Strauss\Main code"

# # Change the directory
# os.chdir(path)

# def read_files(file_path):
#    with open(file_path, 'r') as file:
#       print(file.read())

# # Iterate over all the files in the directory
# for file in os.listdir():
#    if file.endswith('.txt'):
#       # Create the filepath of particular file
#       file_path =f"{path}/{file}"

# read_files(file_path)

import tkinter as tk
from tkinter import filedialog
import os

root = tk.Tk()
root.withdraw()  # Hide the main window.

folder_path = r"g:\My Drive\2025 Techs\L3 DTSD - Mrs. Strauss\Main code"

if folder_path:
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r') as file:
                contents = file.read()
                print(contents)