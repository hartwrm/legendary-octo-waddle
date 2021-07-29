
print('Enter the first number to add:')
first = input()
print('enter second number to add:')
second = input()
print('enter third number to add:')
third = input()
print('the sum is ' + first + second + third)


#input returns a sting value - this is string cat not numerical

import random

heads = 0

for i in range(1, 1001):
    if random.randint(0,1) == 1:
        heads = heads + 1
    if i == 500:
        print('halfway done!')

print('heads came up ' + str(heads) + 'times.')
