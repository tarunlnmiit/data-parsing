import os
from urllib.request import urlretrieve
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

downloadDirectory = 'downloaded'
baseUrl = 'http://pythonscraping.com'

def getAbsoluteURL(baseUrl, source):
	if source.startswith('http://www.'):
		url = 'http://'+source[11:]
	elif source.startswith('http://'):
		url = source
	elif source.startswith('www.'):
		url = source[4:]
		url = 'http://'+source
	else:
		url = baseUrl+'/'+source
	if baseUrl not in url:
		return None
	return url

def getDownloadPath(baseUrl, absoluteUrl, downloadDirectory):
	path = absoluteUrl.replace('www.', '')
	path = path.replace(baseUrl, '')
	path = downloadDirectory+path
	directory = os.path.dirname(path)

	if not os.path.exists(directory):
		os.makedirs(directory)

	return path

def getMultipleFiles(url):
	html = urlopen(url)
	bsObj = BeautifulSoup(html)
	downloadList = bsObj.findAll(src=True)
	for download in downloadList:
		fileUrl = getAbsoluteURL(baseUrl, download["src"])
		if fileUrl is not None:
			print (fileUrl)

	urlretrieve(fileUrl, getDownloadPath(baseUrl, fileUrl, downloadDirectory))

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
option = int(input('Enter 1 to get single file and 2 to get multiple files: '))

if url == '':
	url = 'http://www.pythonscraping.com'

if option == 1:
	getSingleFile(url)
elif option == 2:
	getMultipleFiles(url)