for i in range(4):
    print(i)


print(range(5))

print(list(range(5)))

# spam = (list(range(0, 100, 2)))
# print(spam)

supplies = ['pen', 'pencil', 'paper', 'binder', 'computer']

# use range + len to return both the index and the items in the array

for i in range(len(supplies)):
    print('Index ' + str(i) + " in supplies is: " + supplies[i])


# multiple assigment

cat =['fat', 'orange', 'loud']
size, color, behavior =  cat
print(size, color, behavior)

size2, color2, behavior2 =  'skinny', 'black', 'quiet'
print(size2, color2, behavior2)

a = "AAA"
b = 'BBB'
a, b = b, a
print(a, b)

# augmented assignment
sumNum = 55
sumNum += 1
print(sumNum)