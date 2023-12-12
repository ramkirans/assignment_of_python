
import os

folders = input("Please provide a list of folders names with spaces in between:").split()
for folder in folders:
   try:

     files =  os.listdir(folder)
    except FileNotFoundError:
        print("Please provide a valid folder name")
        print("Please provide a valid folder name ,this folder does not exist: " + folder)
        break 
   #to ignore the wrong folder and proceed with the next folders use continue instead of break
    except PermissionError:
        print("No access to this folder " + folder)

        print(" === listing files for the folder - " + folder)
    
    for file in files:
        print(file)






