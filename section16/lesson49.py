##Pyautogui controlling keyboard

import pyautogui

##typewrite sends virutal keystrokes
##multiple shell commands separated by ;

#click into window and type hello world
pyautogui.click(100, 100); pyautogui.typewrite('hello world')

#add delay
pyautogui.typewrite('hello world', interval=0.5)

#move cursor left or right
pyautogui.typewrite(['a', 'b', 'left', 'right', 'X', 'Y'], interval = 1)

#keypress - will vary on OS
pyautogui.press('F1')
pyautogui.press('f2')
pyautogui.hotkey('crtl', 'o')
