#the web browser module

import webbrowser, sys, pyperclip



#can launch a new broswer with a specified url

# webbrowser.open('https://automatetheboringstuff.com')

#check if command line arguments are passed

if len (sys.argv) > 1:
    #['mapit.py', '870', 'main' 'st.'] -> '870 main st'
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()


webbrowser.open('https://www.google.com/maps/place' + address)