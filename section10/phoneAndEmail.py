#!

import re, pyperclip

#Create regex for phone numbers
phoneRegex = re.compile(r'''
#123-456-7890, 123-4567, (123) 555-0000, 555-0000 ext 12345, ext. 1234, x1234
(
    ((\d\d\d) | (\d(\d\d)))? #area code - optional
    (\s|-) #separator
    \d\d\d #3 digits
    - #separate
    (((ext(\.)?\s) |x) 
    (\d{2,5})) #extension optional
)
''', re.VERBOSE)

#create regex for email
emailRegex = re.compile(r'''
[a-zA-Z0-9_.+]+  #name
@  #@
[a-zA-Z0-9_.+]+ #domain
''', re.VERBOSE)
           
# get text off clipboard
text = '''PainterGreg Bradford262-820-4152gbradford77@verizon.netSalesIsmael Hood606-234-6374ihood41@comcast.netMediaJavier Robinson709-585-7066javierr@msn.comEngineerZack Marquez450-634-7241zmarquez48@live.comPayable/ReceivableBrice Compton580-596-6155bcompton58@mac.comEntryDamien Weaver464-308-4946dweaver90@aol.comGeologicalScott Gibbs918-309-9419sgibbs76@mac.comOfficerBenjamin Ferrell213-748-2704ziaqn32@live.comCoordinatorDelbert Morrison563-448-3826dmorrison48@verizon.net'''

#extract email/phone from text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)
print(extractedPhone)
print(extractedEmail)

           
#copy extracted email/phone to clipboard




