#Raise and assert statements
#used for error handling

#traceback functions
import traceback

def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('"symbol" needs to be a string of length 1.')
    if (width < 2) or (height < 2):
        raise Exception("width and height must be greater or equal to 2.")
    print(symbol * width)

    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)
    print (symbol * width)

# boxPrint('*', 2, 1)
# # boxPrint('**', 1, 1)

try:
    raise Exception('this is an error message')
except:
    errorFile = open('error_log.txt', 'a')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('traceback info was written in error_log.txt') 


 #Assert - sanity check to make sure code is not doing something obviously wrong - use an assert statement

#  assert False, 'this is the assert error message'
#traffic thing

market_2nd = {'ns': 'green', 'ew': 'red'}
intersection = None

def switchLights(intersection):
    for key in intersection.keys():
        if intersection[key] == 'green':
            intersection[key] == 'yellow'
        elif intersection[key] == 'yellow':
            intersection[key] == 'red'
        elif intersection[key] == 'red':
            intersection[key] == 'green'
    assert 'red' in intersection.values(), 'neither light is red!' + str(intersection)

print(market_2nd)

switchLights(market_2nd)

print(market_2nd)