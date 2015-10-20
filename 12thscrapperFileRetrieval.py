from urllib.request import urlretrieve
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def getSingleFile(url):
	try:
		html = urlopen(url)
	except HTTPError as e:
		return None
	try:
		bsObj = BeautifulSoup(html)
		imageLocation = bsObj.find('a', {'id':'logo'}).find('img')['src']
		urlretrieve(imageLocation, 'logo.jpg')
	except AttributeError as e:
		return None

url = input('Enter url(Press Enter to redirect to default URL): ')

if url == '':
	url = 'http://www.pythonscraping.com'

getSingleFile(url)