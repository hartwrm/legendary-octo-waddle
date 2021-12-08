## lesson 47 - Checking your emial inbox Internet Message Access Protocol - IMAP

##IMAP from early days of internet, a bit complex so we are going to use imap client and pyzmail

import imapclient
import pyzmail

##set up connection object - similar to smtp, ssl for encryption
conn = imapclient.IMAPClient('imap.gmail.com', ssl=True)
##login
conn.login('myemail@email.com)', 'password123')

##select folder - read only so you dont delete anything by accident
conn.select_folder9('INBOX', readonly=True)

##find emails - protocol has special syntax for search, list of strings, special search syntax
#grab all email since 11/20/2021 - returns a list of unique IDs -integers
UIDs = conn.search(['SINCE 20-Nov-2021'])
## 2 arguments to get an email - ID + what part of email - ie body, etc - store in an object
rawMessage = conn.fetch([12345], ['Body[]', 'FLAGS'])

##use pyzmail to parse message - UID + email
message = pyzmail.PyzMessage.factory(rawMessage[12345] [b'BODY[]'])

##now we can work with object a bit - grab basic info
message.get_subject()
message.get_addresses('from')
message.get_addresses('to')
message.get_addresses('bcc')

##working with the email body

##check text part - if "none" no body or if html = none, will populate length if present
message.text_part
message.html_part
##get payload and decode
message.text_part.get_payload().decode('UTF-8')

##log out
conn.logout()
