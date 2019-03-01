from PyPDF2 import PdfFileReader
import docxpy
import base64
import sys
import os
import sys
import io
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import XMLConverter, HTMLConverter, TextConverter
from pdfminer.layout import LAParams
class miner():
    def __init__(self,coded_string,extension):
        self.coded_string=coded_string
        self.extension=extension
    def pdfparser(self,data):

        fp = open(data, 'rb')
        rsrcmgr = PDFResourceManager()
        retstr = io.StringIO()
        codec = 'utf-8'
        laparams = LAParams()
        device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
        # Create a PDF interpreter object.
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        # Process each page contained in the document.

        for page in PDFPage.get_pages(fp):
            interpreter.process_page(page)
            data =  retstr.getvalue()

        return data

    def text_extractor(self):
        print(self.extension,file=sys.stderr)
        text = ""
        if (self.extension == str(1)):
            with open("sample.pdf", "wb+") as f:
                f.write(base64.b64decode(self.coded_string))
            text=self.pdfparser("sample.pdf")
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
