#walk through the directory tree

import os

#os.walk('/folder_to_check')
for folderName, subFolders, fileNames in os.walk('/Users/achiv/Documents/devStuff/pythonCourses/AutomateTheBoringStuff/legendary-octo-waddle/section11'):
    print('The folder is: ' + folderName)
    print('subfolders are: ' + str(subFolders))
    print('filenames are: ' + str(fileNames))