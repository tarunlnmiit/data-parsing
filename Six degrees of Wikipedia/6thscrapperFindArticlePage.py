from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re
def getArticle(url):
	try:
		html = urlopen(url)
	except HTTPError as e:
		return None
	try:
		bsObj = BeautifulSoup(html)
		articles = bsObj.find('div', {'id':'bodyContent'}).findAll('a', href=re.compile('^(/wiki/)((?!:).)*$'))
	except AttributeError as e:
		return None
	return articles
url = input('Enter url(press Enter to redirect to default url): ')
if url == '':
	url = 'http://en.wikipedia.org/wiki/Kevin_Bacon'
articles = getArticle(url)
if articles == []:
	print ('Articles Not found')
else:
	fhand = open('articledata.txt','w')
	for link in articles:
		if 'href' in link.attrs:
			fhand.write(link.attrs['href']+'\n')
			print (link.attrs['href']) 
	fhand.close()