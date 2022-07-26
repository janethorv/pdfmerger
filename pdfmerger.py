import PyPDF2
import os
import datetime as dt

#Formatting a string with current date

#Function for merging PDFs in a list of files, creating a file with filename on the format "yyyy_mm_dd_merged.pdf"
def merge_pdfs(files, writepath):
    merger = PyPDF2.PdfFileMerger()
    
    #Formatting a string with current date
    date = str(dt.date.today()).replace('-','_')
    
    for file in files:
        if file.endswith('.pdf'):
            merger.append(file)
    merger.write(writepath + date + '_merged.pdf')
    merger.close()
    
files = os.listdir(os.curdir)
writepath = './pdfmerger/'

merge_pdfs(files, writepath)

