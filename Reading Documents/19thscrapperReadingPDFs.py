from urllib.request import urlopen
from urllib.error import HTTPError
from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO
from io import open

def readPDF(pdfFile):
	rsrcmgr = PDFResourceManager()
	retstr = StringIO()
	laparams = LAParams()
	device = TextConverter(rsrcmgr, retstr, laparams=laparams)

	process_pdf(rsrcmgr, device, pdfFile)
	device.close()

	content = retstr.getvalue()
	retstr.close()
	return content

def getPDF(url):
	try:
		pdfFile = urlopen(url);
	except HTTPError as e:
		return None
	# To work with local PDFs.	
	# pdfFile = open('pdfName.pdf', 'rb')
	outputString = readPDF(pdfFile)
	print (outputString)
	pdfFile.close()

url = input('Enter URL(Press Enter to redirect to default URL): ')
if url == '':
	url = 'http://pythonscraping.com/pages/warandpeace/chapter1.pdf'

getPDF(url)