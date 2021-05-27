words = ['hello', 'hi', 'sup', 'ni-hao']
print(words.index('hello'))

# list data types have several useful methods

# add to the end of a list
words.append('phone')
print(words)

# add anywhere in the list - index then item to add
words.insert(2, 'mouse')
print(words)

# remove - not the same as del - del words[index] - remove will only remove the first instance of an item in a list
words.remove('sup')
print(words)

# sort - order a list - can not sort a list with integers + strings - uses ASCII order 
randomNums = [2,4,3,5,66,2,98,343,2,-54,-5,.5]
randomNums.sort()
print(randomNums)

randomNums.sort(reverse=True)
print(randomNums)

