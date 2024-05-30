import os
import shutil #These are standard libraries

path = os.path.join(os.path.expanduser("~"),"path") #replace path with intendet folder

for filename in os.listdir(path): #list of directory
    file_path = os.path.join(path, filename)
    if os.path.isfile(file_path):#if it is a file
        extension = os.path.splitext(filename)[1] #gets extension(e.g: .png, .docx)
        dir_path = os.path.join(path, extension)
        if not os.path.exists(dir_path): #if there isn't a intendet directory, creates a new one
            os.makedirs(dir_path)
        dest_path = os.path.join(dir_path, filename)
        shutil.move(file_path, dest_path)#moves it into the folder
