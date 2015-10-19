from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def getLinks(url):
	try:
		html = urlopen(url)
	except HTTPError as e:
		return None
	try:
		bsObj = BeautifulSoup(html)
		links = bsObj.findAll('a')
	except AttributeError as e:
		return None
	return links

url = input('Enter URL(press enter to redirect to default url): ')
if url == '':
	url = 'https://en.wikipedia.org/wiki/Kevin_Bacon'
links = getLinks(url)
if links == []:
	print ('Links not Found')
else:
	fhand = open('linksData.txt','w')
	for link in links:
		if 'href' in link.attrs:
			fhand.write(link.attrs['href']+'\n')
			print (link.attrs['href'])
	fhand.close()