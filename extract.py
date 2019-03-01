from PyPDF2 import PdfFileReader
import docxpy
import base64
class miner():
    def __init__(self,coded_string,extension):
        self.coded_string=coded_string
        self.extension=extension

    def text_extractor(coded_string,extension):
        text = ""
        if (self.extension == 1):
            with open("sample.pdf", "wb") as f:
                f.write(base64.b64decode(coded_string))
            with open("sample.pdf", 'rb') as f:
                pdf = PdfFileReader(f)
                text = ""
                for page in range(pdf.getNumPages()):
                    page = pdf.getPage(page)
                    text += page.extractText()

        if (self.extension == 2):
            with open("sample.docx", "wb") as f:
                f.write(base64.b64decode(coded_string))
            file = 'sample.docx'
            text = docxpy.process(file)


        if (self.extension == 3):
            with open("sample.txt", "wb") as f:
                f.write(base64.b64decode(coded_string))
            file = open('sample.txt','r')
            lines = file.readlines()
            file.close()
            for line in lines:
                text += line
        return text

"""coded_string = '''c2FtZSAyIGRvY3VtZW50cyAoZDEgYW5kIGQyKQ0KDQpkMSA9ICJNYXJpanVhbmEgaXMgbGVnYWwgaW4gc29tZSBjb3VudHJpZXMuIEl0IGlzIGlsbGVnYWwgaW4gb3RoZXJzLiBGb3IgZXhhbXBsZSwgaXQgaXMgaWxsZWdhbCBpbiBzb3V0aCBlYXN0IEFzaWFuIGNvdW50cmllcy5Ib3dldmVyLCBUaGFpbGFuZCBjaGFuZ2VzIHRoaXMuSXQgYmVjb21lcyB0aGUgZmlyc3Qgc291dGggZWFzdCBBc2lhbiBjb3VudHJ5IHRvIG1ha2UgbWFyaWp1YW5hIGxlZ2FsLlBlb3BsZSBjYW4gc2VsbCBpdCBhbmQgYnV5IGl0LlRoZXkgY2FuIHVzZSBpdCBhcyBtZWRpY2luZS5UaGUgVGhhaSBnb3Zlcm5tZW50IGNvbnRyb2xzLCB3aG8gc2VsbHMgbWFyaWp1YW5hLiBZb3UgY2FuIHVzZSBpdC4gSG93ZXZlciwgeW91IG11c3QgaGF2ZSBhIGNlcnRpZmljYXRlLiINCg0KZDIgPSAiTWFyaWp1YW5hIGlzIGdhaW5pbmcgcG9wdWxhcml0eSBhcm91bmQgdGhlIHdvcmxkLCBhbmQgVGhhaWxhbmQgYmVjYW1lIHRoZSBmaXJzdCBzb3V0aCBlYXN0IEFzaWFuIGNvdW50cnkgdG8gbGVnYWxpc2UgaXQuQmVnaW5uaW5nIHdpdGggdGhlIG5ldyB5ZWFyLCBwZW9wbGUgd2lsbCBiZSBhYmxlIHRvIHVzZSBpdCBhcyBhIG1lZGljaW5lIG9yIHN0dWR5IGl0LiBIb3dldmVyLCBsaWNlbnNlcyB0byBwcm9kdWNlIGFuZCBzZWxsIG1hcmlqdWFuYSBwcm9kdWN0cyB3aWxsIGJlIHN0cmljdGx5IGNvbnRyb2xsZWQuIFBlb3BsZSB3aWxsIGJlIGFibGUgdG8gY2FycnkgY2VydGFpbiBhbW91bnRzIG9mIHRoZSBkcnVncyBpZiB0aGV5IGhhdmUgYSBwcmVzY3JpcHRpb24gb3IgY2VydGlmaWNhdGUuIFRoZSBuZXcgbGF3IGFsc28gYWxsb3dzIGtyYXRvbSwgd2hpY2ggaXMgYSBwbGFudCBuYXRpdmUgdG8gdGhlIHJlZ2lvbi4gUGVvcGxlIHVzZSBpdCB0byB0cmVhdCBwYWluLCBhbnhpZXR5IGFuZCBvdGhlciBwcm9ibGVtcy4iDQoNCg0Kc2ltaWxhcml0eSBzY29yZSBmb3IgYWxnb3MgaXMgOg0KDQoxLmNvc2luZSB3aXRoIHRmaWRmIHdlaWdodHMgPSAwLjMzNzAxMDkNCjIud29yZG5ldF9jb3NpbmUgd2l0aCBiYWdvZndvcmRzKEJPVykgPSAwLjM5DQozLndvcmRuZXQgd2l0aCBwb3MgdGFnZ2luZyA9IDAuNjE3Mw0KDQotLSBjb252ZXJ0IG5vdCAtLQ0KDQp0ZW1wID0gIlN5bnNldCgnbm90LnIuMDEnKSINCg0KICBub3RfcG9zMSA9IFtdDQogIG5vdF9wb3MyID0gW10NCg0KICBmb3IgaSBpbiByYW5nZSAoMCxsZW4oc3luc2V0czEpKToNCg0KICAgICAgaWYgdGVtcCA9PSBzdHIoc3luc2V0czFbaV0pOg0KICAgICAgICAgIHBvc2l0aXZlID0gc3luc2V0czFbaSsxXQ0KICAgICAgICAgIG5lZ2F0aXZlID0gcG9zaXRpdmUubGVtbWFzKClbMF0uYW50b255bXMoKVswXQ0KICAgICAgICAgIHN5bnNldHMxW2krMV09bmVnYXRpdmUuc3luc2V0KCkNCiAgICAgICAgICBub3RfcG9zMS5hcHBlbmQoaSkNCg0KICBmb3IgaSBpbiByYW5nZSAoMCxsZW4oc3luc2V0czIpKToNCg0KICAgICAgaWYgdGVtcCA9PSBzdHIoc3luc2V0czJbaV0pOg0KICAgICAgICAgIGlmKGkrMSA9PSBsZW4oc3luc2V0czIpKToNCiAgICAgICAgICAgICAgYnJlYWs7DQogICAgICAgICAgcG9zaXRpdmUgPSBzeW5zZXRzMltpKzFdDQogICAgICAgICAgbmVnYXRpdmUgPSBwb3NpdGl2ZS5sZW1tYXMoKVswXS5hbnRvbnltcygpWzBdDQogICAgICAgICAgc3luc2V0czJbaSsxXT1uZWdhdGl2ZS5zeW5zZXQoKQ0KICAgICAgICAgIG5vdF9wb3MyLmFwcGVuZChpKQ0KDQogIGlmIChsZW4obm90X3BvczEpIT0wIG9yIGxlbihub3RfcG9zMikhPTApOg0KICAgICAgZm9yIGogaW4gbm90X3BvczE6DQogICAgICAgICAgZGVsIHN5bnNldHMxW2pdDQogICAgICBmb3IgaiBpbiBub3RfcG9zMjoNCiAgICAgICAgICBkZWwgc3luc2V0czJbal0NCg0KDQpqYWNjYXJkOg0KDQpyZXN1bHQgPSAwLjANCg0KaW50ZXJzZWN0aW9uICA9IGxlbihsaXN0KHNldChzMSkgJiBzZXQoczIpKSkNCnVuaW9uID0gbGVuKGxpc3Qoc2V0KHMxKS51bmlvbihzZXQoczIpKSkpDQpyZXN1bHQgPSBpbnRlcnNlY3Rpb24vdW5pb24NCnJldHVybiByZXN1bHQNCg=='''
