# Regular Expressions Basics

# Below is a lot of code to look for phone number patterns/messages - text pattern is so common that Regex is used to shorten this type of behavior

# def isPhoneNumber(text):
#     if len(text) != 12:
#         return False #not phone number size
#     for i in range(0,3):
#         if not text[i].isdecimal():
#             return False
#     if  text[3] != '-':
#         return False
#     for i in range(4,7):
#         if not text[i].isdecimal():
#             return False
#     if text[7] != '-':
#         return False
#     for i in range(8,12):
#         if not text[i].isdecimal():
#             return False
#     return True


# print(isPhoneNumber('hello'))

message = 'call me at 555-332-2939 or you can reach me on my cell at 123-456-7890'
# foundNumber = False
# for i in range(len(message)):
#     chunk = message[i:i+12]
#     if isPhoneNumber(chunk):
#         print('Phone number found: ' + chunk)
#         foundNumber = True
# if not foundNumber:
#     print('could not find any phone numbers')




# import the re module
import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search(message)
mo1 = phoneNumRegex.findall(message)
print(mo.group())
print(mo1)