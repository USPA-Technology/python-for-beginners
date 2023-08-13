# Import the os module
import os

# Define the path where the folders will be created
path = "/home/thomas/0-uspa/python-for-beginners/"

# Create a loop to iterate from 1 to 16
for i in range(1, 17):
    # Create a folder name using string formatting
    folder_name = "Chapter {}".format(i)
    # Join the path and the folder name
    folder_path = os.path.join(path, folder_name)
    # Create the folder using os.mkdir()
    os.mkdir(folder_path)
