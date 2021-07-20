#walk through the directory tree

import os

#os.walk('/folder_to_check')
for folderName, subFolders, fileNames in os.walk('/absoulte/directory/path'):
    print('The folder is: ' + folderName)
    print('subfolders are: ' + str(subFolders))
    print('filenames are: ' + str(fileNames))