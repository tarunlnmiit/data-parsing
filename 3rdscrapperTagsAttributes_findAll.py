from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
def getTitle(url):
	try:
		html = urlopen(url)
	except HTTPError as e:
		return None
	try:
		bsObj = BeautifulSoup(html)
		# findAll(tag,	attributes,	recursive,	text,	limit,	keywords)
		# find(tag,	attributes,	recursive,	text,	keywords)
		nameList = bsObj.findAll('span',{'class':'green'})
		headerList = bsObj.findAll({'h1','h2','h3','h4','h5','h6'})
		allText	= bsObj.findAll(id="text")
	except AttributeError as e:
		return None
	return [nameList, headerList, allText]
url = input('Enter url(press Enter to redirect to default url): ')
if url == '':
	url = 'http://www.pythonscraping.com/pages/warandpeace.html'
nameList, headerList, allText = getTitle(url)
if nameList == []:
	print ('Names Not found')
else:
	fhand = open('data.txt','w')
	for name in nameList:
		fhand.write(name.get_text()+'\n')
		print (name.get_text()) # get_text() strips all	tags from the document you are working with	and	returns	a string containing	the	text only.
if headerList == []:
	print ('Headers Not found')
else:
	for header in headerList:
		fhand.write(header.get_text())
		print (header.get_text())
fhand.write('\n')
fhand.write(allText[0].get_text()+'\n')
print (allText[0].get_text())
fhand.close()