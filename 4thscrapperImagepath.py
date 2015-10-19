from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re
def getImages(url):
	try:
		html = urlopen(url)
	except HTTPError as e:
		return None
	try:
		bsObj = BeautifulSoup(html)
		images = bsObj.findAll('img', {'src':re.compile('\.\.\/img\/gifts/img.*\.jpg')})
	except AttributeError as e:
		return None
	return images
url = input('Enter url(press Enter to redirect to default url): ')
if url == '':
	url = 'http://bit.ly/1KGe2Qk'
images = getImages(url)
if images == []:
	print ('Images Not found')
else:
	fhand = open('imagedata.txt','w')
	for image in images:
		fhand.write(image['src']+'\n')
		print (image['src']) 
	fhand.close()