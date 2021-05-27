# mutable and immuatable data types

name = 'zophie a cat'
print(name[7])

# can not add/modify the string - need to use slices

newName = name[0:7] + ' the ' + name[8:12]
print(newName)

# two separate references reference the same list so both are updated - not like variable assignments - you are not copying the list, you are copying the reference

spam = [0,1,2,3,4,5]
cheese = spam
cheese[1] = 'hello'
print(cheese)
print(spam)

def eggs(someParam):
    someParam.append('hello')
    
stuff = [1,2,3]
eggs(stuff)
print(stuff)

import copy

letters = ['a', 'b', 'c', 'd', 'e']
moreLetters = copy.deepcopy(letters)
moreLetters[2] =  57
print(letters)
print(moreLetters)