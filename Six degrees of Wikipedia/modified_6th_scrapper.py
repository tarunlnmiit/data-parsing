from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re, datetime, random

random.seed(datetime.datetime.now())

def getLinks(articleurl):
	try:
		html = urlopen('http://en.wikipedia.org'+articleurl)
	except HTTPError as e:
		return None
	try:
		bsObj = BeautifulSoup(html)
		Links = bsObj.find('div', {'id':'bodyContent'}).findAll('a', href=re.compile('^(/wiki/)((?!:).)*$'))
	except AttributeError as e:
		return None
	return Links
url = input('Enter url(press Enter to redirect to default url): ')
if url == '':
	url = '/wiki/Kevin_Bacon'
Links = getLinks(url)
fhand = open('articleLinkData.txt','w')
while len(Links) > 0:
	newArticle = Links[random.randint(0, len(Links)-1)].attrs['href']
	fhand.write(newArticle+'\n')
	print (newArticle)
	Links = getLinks(newArticle)
fhand.close()