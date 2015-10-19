from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
def getTitle(url):
	try:
		html = urlopen(url)
	except HTTPError as e:
		return None
	try:
		bsObj = BeautifulSoup(html.read())
		title = bsObj.h1
	except AttributeError as e:
		return None
	return title

title = getTitle('http://www.pythonscraping.com/exercises/exercise1.html')
if title == None:
	print ('Title Not found')
else:
	print (title)