# def div42by(divideBy):
#     try:
#         return 42 / divideBy
#     except ZeroDivisionError:
#         print('Error, you tried to divide by 0')

# print(div42by(2))
# print(div42by(10))
# print(div42by(0))
# print(div42by(1))

print('how many cats do you have?')
numCats = input()
try:
    if int(numCats) >= 4:
        print('that is a lot of cats')
    elif int(numCats) < 0:
        print("you can't have negative cats")
    else:
        print('that is not that many cats')
except ValueError:
    print('You did not enter a number')
