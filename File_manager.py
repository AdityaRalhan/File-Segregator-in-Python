import os, shutil

path = r"/Users/adityapc/Desktop/"
file_name = os.listdir(path)

folder_names = ['pdf files', 'word files', 'iso files', 'jpeg files', 'text files']

for loop in range(0, len(folder_names)):
    
    if not os.path.exists(path + folder_names[loop]): # if this folder DOES 'NOT' EXIST, it wil create it
        print(path + folder_names[loop])
        os.makedirs(path + folder_names[loop])

for file in file_name: 
    if ".docx" in file and not os.path.exists(path + 'word files/' + file): # if we have a .docx file in the listed files but not in the folder
        shutil.move(path + file, path + 'word files/') # this is how we move the file -> shutil.move(where it is rn, where u want it to go)
    
    elif ".iso" in file and not os.path.exists(path + 'iso files/' + file):
        shutil.move(path + file, path + 'iso files/')

    elif ".pdf" in file and not os.path.exists(path + 'pdf files/' + file):
        shutil.move(path + file, path + 'pdf files/')

    elif ".jpeg" in file and not os.path.exists(path + 'jpeg files/' + file):
        shutil.move(path + file, path + 'jpeg files/')

    elif ".txt" in file and not os.path.exists(path + 'text files/' + file):
        shutil.move(path + file, path + 'text files/')




