# Character classes and findall() method

import re

# no groups in expression will return a list of strings - list is the text matching the pattern for Zero or One groups
phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
resume = '''
Madison, WI • 123-456-7891
cfredrickson@email.com
SUMMARY

Detail-oriented and reliable Data Entry Clerk with 15+ years of experience accurately recording, tracking, and analyzing mass data to achieve target goals.
EDUCATION

GREEN VALLEY STATE 575-404-3302
Aug '96 - May '00
Bachelor of Science in Applied Mathematics

CLOUD CLEARWATER 627-509-8892
Insurance Claims Data Entry Clerk
Aug '15 - Jul '19


RETAIL OCEAN 123-059-0040
Laboratory Data Entry Clerk
Jan '13 - Aug '15
'''

mo = phoneRegex.findall(resume)
print(mo)

# expression with group returns a teuple of strings - multiple string values that correspond with group inside the regex object
# two
phoneRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneRegex.findall(resume)
print(mo)



# character classv - numbers followed by a word
lyrics = '12 drummers drumming, 11 pipers piping, 10 lords a leaping, 9 ladies dancing, 8 maids a milking, 7 swans a swimming, 6 geese a laying, 5 golden rings, 4 calling birds, 3 french hens, 2 turtle doves, and 1 partridge in a pear tree'

xmasRegex = re.compile(r'\d+\s\w+')
mo = xmasRegex.findall(lyrics)
print(mo)

# create your own character class
vowelRegex = re.compile(r'[aeiouAEIOU]') #r'a|e|i|o|u' - needs capitals - exact matches
mo = vowelRegex.findall('Robo cop eats baby food')
print(mo)

# doublematch with brackets {}
vowelRegex = re.compile(r'[aeiouAEIOU]{2}')
mo = vowelRegex.findall('Robo cop eats baby food')
print(mo)

# negative character class with ^ -ie the opposite of the values in the expression - any character - digits, spaces, punctuation
vowelRegex = re.compile(r'[^aeiouAEIOU]')
mo = vowelRegex.findall('Robo cop eats baby food')
print(mo)