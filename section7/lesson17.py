# dictionary data type - key value pairs


myDog = {
    'size': 'medium',
    'color': 'black',
    'behavior': 'shy'
}

print('my dog has ' + myDog['color'] + ' fur')

print(list(myDog.keys()))
print(list(myDog.values()))
print(list(myDog.items()))

for k in myDog.keys():
    print(k)

for v in myDog.values():
    print(v)

for k, v in myDog.items():
    print(k, v)

# pretty print
import pprint
message = "it was  bright cold day in april, and the clocks were striking thirteen."
count = {}

for character in message.upper():
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pprint(count)