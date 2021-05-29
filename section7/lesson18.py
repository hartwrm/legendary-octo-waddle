#  lesson 18 Data Structures

# dictionary
cat = {"name": 'nakama', 'age': '12', 'color': 'black'}

# list
allCats = []
allCats.append(cat)

allCats.append({'name': 'kuma', 'age': '10', 'color': 'white'})
allCats.append({'name': 'mary', 'age': '14', 'color': 'brown,white, black'})

# print(allCats)

# tic tac toe board
# store key-value in dictionary
import pprint

theBoard = {
    'top-L': ' ',
    'top-M': ' ', 
    'top-R': ' ',
    'mid-L': ' ',
    'mid-M': ' ',
    'mid-R': ' ',
    'low-L': ' ',
    'low-M': ' ',
    'low-R': ' '
     }

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-----')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-----')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])


# pprint.pprint(theBoard)

printBoard(theBoard)

print(type(theBoard))
print(type(theBoard["top-R"]))