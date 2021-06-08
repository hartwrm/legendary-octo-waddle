import re

# ? = match once or none
batRegex = re.compile(r'Bat(wo)?man')
mo = batRegex.search("The Adventures of Batman")
print(mo.group())

mo = batRegex.search("the Adventures of Batwoman")
print(mo.group())

phoneRegex =re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo = phoneRegex.search('My number is 555-345-3939')
mo = phoneRegex.search('My number is 345-3939')
print(mo)

# * = match 0 or more times
batRegex = re.compile(r'Bat(wo)*man')
mo = batRegex.search("the adventures of Batwowowowowowowoman")
print(mo)

#  + = match one more times
batRegex = re.compile(r'Bat(wo)+man')
# won't match
('The Adventures of Batman')
# will match
('The Adventures of Batwoman')
('The Adventures of Batwowowowowowowowoman')

regex = re.compile(r'\+\*\?')
mo = regex.search('I learned about +*? regex syntax')
print(mo)

# match a specific number of repititions of a group
haRegex = re.compile(r'(Ha){3}')
mo = haRegex.search('He said "HaHaHa"')
print(mo)
phoneRegex = re.compile(r'((\d\d\d-)?\d\d\d-\d\d\d\d(,)?){3}')
mo = phoneRegex.search('my numbers are 555-555-5555,233-323-4445,666-666-6666')
print(mo)

# match a range - can have more but will only match upper limit, need at least lower limit, will match everything in between
haRegex = re.compile(r'(Ha){3,5}')
mo = haRegex.search("He said HaHaHaHaHa")
print(mo)

