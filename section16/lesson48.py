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
pyautogui.moveTo(40, 300, duration=2)
##takes coordinates - offsets
pyautogui.moveRel(400, 0, duration=2)
pyautogui.moveRel(0, -150, duration=2)

##perform actions
#click
pyautogui.click(-1469, -204)
