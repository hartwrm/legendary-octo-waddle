#Copying and moving files and folders

import shutil

#copy file into a directory
shutil.copy('/filename', '/directory')

#copy file and rename in directory
shutil.copy('filename', '/directory/renamedfiled')

#copy folder and it's contents
shutil.copytree('/source_directory', '/destination_directory')

# there is no rename function - just use move like cmd line
shutil.move('/directory/filename', '/directory/NewFileName')