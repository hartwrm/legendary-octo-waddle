# def div42by(divideBy):
#     try:
#         return 42/(divideBy)
#     except ZeroDivisionError:
#         print('Error, you cannot divide by zero')


# print(div42by(2))
# print(div42by(12))
# print(div42by(0))
# print(div42by(1))

print('how many cats do you have')
numCats = input()
try:
    if int(numCats) >= 4:
        print('lotta cats')
    elif int(numCats) < 1:
        print('cant have negative cats')
    else:
        print('eh not a lot of cats')
except ValueError:
        print('not a number')
