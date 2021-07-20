#Deleting files

import os
#unlink = delete
#without absolute path deletes file from current workign directory
os.unlink('filename.txt')

#remove directory - folder must be empty!
os.rmdir('/directory')

import shutil
#delete folder + all it's content
shutil.rmtree('/directory/filename.txt')

#dry run - comment out the actual delete commands and print instead
for filename in os.listdir():
    if filename.endswith('.txt')
    #os.unlink(filename)
    print(filename)