# Reading and writing plain text files

helloFile = open('testdoc.txt')
# print(helloFile.readlines())
content = helloFile.read()
print(content)
helloFile.close()

majorTom = open('testdoc2.txt', 'a+')
majorTom.write('Ground control to major tom, ur circuit/s dead is there something wrong? ')
groundControl = majorTom.read()
print(groundControl)
majorTom.close()

import shelve
shelfFile = shelve.open('mydata')
shelfFile['dogs'] = ['richard parker', 'kyle', 'swift']
shelfFile.close()

shelfFile = shelve.open('mydata')
print(shelfFile['dogs'])