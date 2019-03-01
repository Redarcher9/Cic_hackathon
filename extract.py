from PyPDF2 import PdfFileReader
import docxpy
import base64
import sys
import os
class miner():
    def __init__(self,coded_string,extension):
        self.coded_string=coded_string
        self.extension=extension

    def text_extractor(self):
        print(self.extension,file=sys.stderr)
        text = ""
        if (self.extension == str(1)):
            with open("sample.pdf", "wb+") as f:
                f.write(base64.b64decode(self.coded_string))
            with open("sample.pdf", 'rb') as f:
                pdf = PdfFileReader(f)
                text = ""
                for page in range(pdf.getNumPages()):
                    page1 = pdf.getPage(page)
                    text += page1.extractText()
                os.remove("sample.pdf")


        if (self.extension == str(2)):
            with open("sample.docx", "wb+") as f:
                f.write(base64.b64decode(self.coded_string))
            file = 'sample.docx'
            text = docxpy.process(file)
            os.remove("sample.docx")


        if (self.extension == str(3)):
            with open("sample.txt", "wb+") as f:
                f.write(base64.b64decode(self.coded_string))
            file = open('sample.txt','r')
            lines = file.readlines()
            file.close()
            for line in lines:
                text += line
            os.remove("sample.txt")
        return text
