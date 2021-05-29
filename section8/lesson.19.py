# Advanced String Syntax - manipulating strings

# escape chartcters

# not ok
# 'This is Alice's cat'

# single inside double
"This is Alice's cat"

# escape \ + character
#  \n - new line
'Say hi to Bob\s mother.'

# print('hello there! \nHow are you? \nI\'m fine')

# raw string
# print(r'hello')
# print(r'that is Carol\'s cat')

# print("""Dear Alice, Eve's cat has been arrested for catnapping, cat burglary, and extortion, sincerely, Bob.""")

spam = 'hello world'

print(spam[0])
print(spam[1:5])
print(spam[-1])
print("hello" in spam)
print('x' in spam)