import PyPDF2

#Line number 4 will convert the file object to binary mode
with open('dummy.pdf','rb') as file:
    print(file)
    reader = PyPDF2.PdfFileReader(file)
    print(reader.numPages)
    #since dummy file contains only one page
    page = reader.getPage(0)

    #Rotating the Pdf vertically
    page.rotateCounterClockwise(90)

    # print(page.rotateCounterClockwise(90) )
    writer = PyPDF2.PdfFileWriter()

    #giving the page that we rotated so that whatever we rotated is not going to go into trash.
    writer.addPage(page)
    with open('tilt.pdf','wb') as new_file:
        writer.write(new_file)
