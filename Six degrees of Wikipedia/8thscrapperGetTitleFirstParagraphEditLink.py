from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re

pages = set()
def getLinks(pageUrl):
	global pages

	try:
		html = urlopen('http://en.wikipedia.org'+pageUrl)
	except HTTPError as e:
		return None
	try:
		bsObj = BeautifulSoup(html)
		print (bsObj.h1.get_text())
		print (bsObj.find(id='mw-content-text').findAll('p')[0])
		print (bsObj.find(id='ca-edit').find('span').find('a').attrs['href'])
		
	except AttributeError as e:
		print ('This page is missing something')

	fhand = open('titleParagraphEditLinkdata.txt', 'w')
	
	for link in bsObj.findAll('a', href=re.compile('^(/wiki/)')):
		if 'href' in link.attrs:
			if link.attrs['href'] not in pages:
				# New Page encountered
				newPage = link.attrs['href']
				fhand.write(newPage+'\n')
				print ('----------------\n'+newPage)
				pages.add(newPage)
				getLinks(newPage)

pageUrl = input('Enter url(Press enter to redirect to default URL): ')
getLinks(pageUrl)