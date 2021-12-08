## EMAIL and SMTP (simple mail transfer protocol)

##import smpt lib - library for smtp
import smtplib

## connection object + function for calling mail server.  funciton takes domain + port
conn = smtplib.SMTP('smtp.gmail.com', 587)

##connect to the server - sends out internet traffic - ehlo function, previously 'helo' - returns tuple - response code and bytes object.
print(conn.ehlo())

##after connecting - start TLS encryption so password is encrypted
conn.starttls()

## log in with email + pw - 2F auth and google default security settings blocks this
conn.login('someemail@gmail.com', 'password123')

## send emails - from user A to user B, followed by body of email - crammed into a string -
conn.sendmail('myemail@email.com', 'youremail@email.com', 'Subject: This is a Test \n\nDear Major Tom, This is Ground Control.  Do you hear me Major Tom?\n\n-Ground Control')
##return object of sendmail - dictionary of all the mails it failed to send.

##disconnect
conn.quit()
