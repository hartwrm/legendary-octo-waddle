## Controlling the Mouse from Python - GUI Automation

## x, y coordinates - 0,0 at the very top left corner

import pyautogui
##get screen size
print(pyautogui.size())
#assign width and height size values
width, height = pyautogui.size()

##show mouse position
##print(pyautogui.position())

##move mouse to set coordinates
#pyautogui.moveTo(40, 300, duration=2)

##takes coordinates - offsets
#pyautogui.moveRel(400, 0, duration=2)
#pyautogui.moveRel(0, -150, duration=2)

##perform actions
#click
pyautogui.click(-1469, -204)

##draw a spiral
pyautogui.click() #bring draw window into focus
distance = 200
 while distance > 0:
        pyautogui.drag(distance, 0, duration=0.5)   # move right
        distance -= 5
        pyautogui.drag(0, distance, duration=0.5)   # move down
        pyautogui.drag(-distance, 0, duration=0.5)  # move left
        distance -= 5
        pyautogui.drag(0, -distance, duration=0.5)  # move up




## Run from command line
#python3
#import pyautogui
#pythonautogui.displayMousePosistion()
    #track your mouse coordinates
