import os
import shutil

# specify the path to your desktop
path = os.path.join(os.path.expanduser("~"), "path")

# iterate over all files on the desktop
for filename in os.listdir(path):
    # construct full file path
    file_path = os.path.join(path, filename)
    # check if it's a file
    if os.path.isfile(file_path):
        # get the file extension
        extension = os.path.splitext(filename)[1]
        # construct the directory path
        dir_path = os.path.join(path, extension)
        # create directory if it doesn't exist
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        # construct the destination file path
        dest_path = os.path.join(dir_path, filename)
        # move the file
        shutil.move(file_path, dest_path)
