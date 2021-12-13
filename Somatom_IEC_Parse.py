from pdfminer3.layout import LAParams, LTTextBox
from pdfminer3.pdfpage import PDFPage
from pdfminer3.pdfinterp import PDFResourceManager
from pdfminer3.pdfinterp import PDFPageInterpreter
from pdfminer3.converter import PDFPageAggregator
from pdfminer3.converter import TextConverter
import io

resource_manager = PDFResourceManager()
fake_file_handle = io.StringIO()
converter = TextConverter(resource_manager, fake_file_handle, laparams=LAParams())
page_interpreter = PDFPageInterpreter(resource_manager, converter)

# pageno=0
# with open('Docs//IEC.pdf', 'rb') as fh:
#     for page in PDFPage.get_pages(fh,caching=True,check_extractable=True):
#         page_interpreter.process_page(page)
#         text = fake_file_handle.getvalue()
# # close open handles
# converter.close()
# fake_file_handle.close()
# print(text)


from pdfminer3.pdfparser import PDFParser
from pdfminer3.pdfdocument import PDFDocument



fp = open('Docs//IEC.pdf', 'rb')
parser = PDFParser(fp)
doc = PDFDocument(parser)
print(doc.info[0]['ModDate'])


# rsrcmgr = PDFResourceManager()
# retstr = io.StringIO()
# print(type(retstr))
# codec = 'utf-8'
# laparams = LAParams()
# device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
# interpreter = PDFPageInterpreter(rsrcmgr, device)
#
# page_no = 0
# for pageNumber, page in enumerate(PDFPage.get_pages(fp)):
#     if pageNumber == page_no:
#         interpreter.process_page(page)
#         data = retstr.getvalue()
#         print(data)



