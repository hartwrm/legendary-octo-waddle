#Regex sub() method and verbose mode

import re

# use .sub() to find an replace pattern + arguments
namesRegex = re.compile(r'Agent \w+')
print(namesRegex.findall('Agent Alice gave the secret documents to Agent Bob'))
print(namesRegex.sub('REDACTED', 'Agent Alice gave the secret documents to Agent Bob'))

#pattern matches agent and group of word character
namesRegex = re.compile(r'Agent (\w)\w*')
print(namesRegex.findall('Agent Alice gave the secret documents to Agent Bob'))
print(namesRegex.sub(r'Agent \1****', 'Agent Alice gave the secret documents to Agent Bob'))


#re.VERBOSE readability, new lines, add comments
phoneRegex = re.compile(r'''
(\d\d\d-)  #area code
(\(\d\d\d\) ) # or area code with parenthese
-       #first dash
\d\d\d  #3 digits
-       #2nd dash
\d\d\d\d  #last 4 digits
\sx\d{2,4}  #extension, ie 123''', re.VERBOSE | re.DOTALL | re.IGNORECASE) #this is really just for the complie function - old fashioned but works

