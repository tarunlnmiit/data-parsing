# The first step is to read XML from the file

from zipfile import ZipFile
from urllib.request import urlopen
from urllib.error import HTTPError
from io import BytesIO
from bs4 import BeautifulSoup

def getWordFileData(url):
	try:
		wordFile = urlopen(url).read()
	except HTTPError as e:
		return None
	wordFile = BytesIO(wordFile)
	document = ZipFile(wordFile)
	xml_content = document.read('word/document.xml')

	wordObj = BeautifulSoup(xml_content.decode('utf-8'))
	textStrings = wordObj.findAll('w:t')
	for textElem in textStrings:
		closeTag = ""
		try:
			style =	textElem.parent.previousSibling.find("w:pstyle")
			if style is	not	None and style["w:val"]	== "Title":
				print("<h1>")
				closeTag = "</h1>"
		except AttributeError:
		#No	tags	to	print
			pass
		print(textElem.text)
		print(closeTag)

url = input('Enter URL(Press Enter to redirect to default URL): ')
if url == '':
	url = 'http://pythonscraping.com/pages/AWordDocument.docx'

getWordFileData(url)