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

# Search all the files for their usernames and print.
if folder_path:
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r') as file:
                for line in file:
                    if line.lower().startswith("username:"):
                        # Split at the colon and strip whitespace
                        usernames = line.split(":", 1)[1].strip()
                        print(usernames)

                        if username in usernames:
                            messagebox.showerror("Testing", "Invalid username that already exists. please choose another")

                # contents = file.read()
                # print(contents)

                # content = file.read().splitlines()
                # # Check if a line has username and password.
                # user_exists = any(f"Username: " for line in content)
                
                # if user_exists:
                #     print(f"Username: {username}\nPassword: {[password]}")
                