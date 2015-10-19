from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re

pages = set()
def getLinks(pageUrl):
	try:
		html = urlopen('http://en.wikipedia.org'+pageUrl)
	except HTTPError as e:
		return None
	try:
		bsObj = BeautifulSoup(html)
		Links = bsObj.findAll('a', href=re.compile('^(/wiki/)'))
	except AttributeError as e:
		return None
	return Links

pageUrl = input('Enter url(Press enter to redirect to default URL): ')

Links = getLinks(pageUrl)

if Links == []:
	print ('Links not Found')
else:
	fhand = open('entiresitedata.txt', 'w')
	for link in Links:
		if 'href' in link.attrs:
			if link.attrs['href'] not in pages:
				newPage = link.attrs['href']
				fhand.write(newPage+'\n')
				print (newPage)
				pages.add(newPage)
				getLinks(newPage)