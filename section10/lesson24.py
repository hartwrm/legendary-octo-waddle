# Regex groups and pipe character

import re

phoneNumregex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumregex.search('my number is 669-996-6969')
print(mo.group())


# parantheses used to group text patterns
phoneNumregex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumregex.search('my number is 669-996-6969')
print(mo.group(1, 2))

# escape parantheses - use \ to escape
phoneNumregex = re.compile(r'\(\d\d\d\) \d\d\d-\d\d\d\d')
mo = phoneNumregex.search('my number is (669) 996-6969')
print(mo.group())

# | pipe is used to match several patters - ie OR
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())