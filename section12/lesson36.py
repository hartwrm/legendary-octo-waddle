#Logging

#5 levels of logging
#Debug
#Info
#Warning
#Error
#Critical

import logging
#can push log messages to a file name by adding it config
logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

#turn off all the log messages at critical level or lower (critical is the higest - debug the lowest)

# logging.disable(logging.CRITICAL)

logging.debug('start of program')

def factorial(n):
    logging.debug('start factorial')
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.warning(' i is %s, total is %s' % (i, total))
    logging.info('return value is %s' % (total))
    return total

print(factorial(5))

logging.debug('end of program')