import PyPDF2
import os
os.chdir('/Users/achiv/Downloads')

####open the pdf file, by default is in read mode, need read binary mode 'rb'
##pdfFile = open('meetingminutes1.pdf', 'rb')
##
####pass file object ot pyPDF2 - returns new PDF reader object
##reader = PyPDF2.PdfFileReader(pdfFile)
##
####reader objects have number variable - numPages, stores page numbers
##reader.numPages
##print(reader.numPages)
##
#### reader method, returns page object - page can be read using extractText() method - returns a string
##page = reader.getPage(0)
##print(page.extractText())
##
####iterate through all the pages
#### pageNum as iterator, reader.numPages is integer of all pages in file
##for pageNum in range (reader.numPages):
##    ##extract the text from reader(object), getPage(pageNum) is iterating through all the pages)
##    print (reader.getPage(pageNum).extractText())


##combine the two pdf files
##open both files 
pdf1File = open('meetingminutes1.pdf', 'rb')
pdf2File = open('meetingminutes2.pdf', 'rb')

##store in reader variables using PyPDF to create reader objects
reader1 = PyPDF2.PdfFileReader(pdf1File)
reader2 = PyPDF2.PdfFileReader(pdf2File)

##iterate through both, stroring all pages in a new pdf file

##create new file - only in program, not on hard drive
writer = PyPDF2.PdfFileWriter()

##loop through reader objects to make populate new file
for pageNum in range (reader1.numPages):
    ## get page object, pass page number
    page = reader1.getPage(pageNum)
    ##take page object, pass it to writer object
    writer.addPage(page)

##exact code but with reader2
for pageNum in range (reader2.numPages):
    page = reader2.getPage(pageNum)
    writer.addPage(page)

##save file, using the writer object using write method to save to hardrive
outputFile = open('combinedminutes.pdf', 'wb')
writer.write(outputFile)
outputFile.close()
pdf1File.close()
pdf1File.close()
