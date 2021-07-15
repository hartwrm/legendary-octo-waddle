#Regex Dot-Star adn the Caret/Dollar Character

import re

#start of a string
beginsWithHelloRegex = re.compile(r'^Hello')
print(beginsWithHelloRegex.search("Hello there"))
#  beginsWithHelloRegex.search("He said Hello there") == None

#end of a string
endsWithWorldRegex = re.compile(r'world!')
print(endsWithWorldRegex.search('Hello world!'))

# \d+ means 1 or more digits - both ^ and $ - string must start and end with just this pattern
allDigitsRegex = re.compile(r'^\d+$')
print(allDigitsRegex.search('123454759859468933498439843'))
#could not use something like 12345x12345

# . - looks for single character + pattern - any character except the new line
atRegex = re.compile(r'.at')
print(atRegex.findall('The cat int he hat ssat on the flat mat.'))

#2 characters - could be anything including whitespace
atRegex = re.compile(r'.{1,2}at')
print(atRegex.findall('The cat int he hat sat on the flat mat.'))

# .* - basically means any pattern - this greedy - will try and match as much text as possible
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
print(nameRegex.findall('First Name: John Last Name: Smith'))

# .*? - matching pattern but not greedy
serve = '<To serve humans> for dinner.>'

nonGreedy = re.compile(r'<.*?>')
print(nonGreedy.findall(serve))

greedy = re.compile(r'<.*>')
print(greedy.findall(serve))

vowelRegex = re.compile(r'[aeiou]')
print(vowelRegex.findall('Al why does your book talk about Robocop so much'))