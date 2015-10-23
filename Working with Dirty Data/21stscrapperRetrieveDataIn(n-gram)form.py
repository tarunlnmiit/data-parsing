from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re
import string

def cleanInput(input):
	input = re.sub('\n+', ' ', input)
	input = re.sub('\[[0-9]*\]', '', input)
	input = re.sub(' +', ' ', input)
	input = bytes(input, 'UTF-8')
	input = input.decode('ascii', 'ignore')
	cleanInput = []
	input = input.split(' ')
	for item in input:
		item = item.strip(string.punctuation)
		if len(item) > 1 or (item.lower() == 'a' or item.lower() == 'i'):
			cleanInput.append(item)
	return cleanInput

def getNgrams(input, n):
	input = cleanInput(input)
	output = []
	for i in range(len(input)-n+1):
		output.append(input[i:n+i])
	return output

def getData(url):
	try:
		html = urlopen(url)
	except HTTPError as e:
		return None
	try:
		bsObj = BeautifulSoup(html)
		content = bsObj.find('div', {'id':'mw-content-text'}).get_text()
		ngrams = getNgrams(content, 2)
		print (ngrams)
		print ('2-grams count is: '+str(len(ngrams)))
	except AttributeError as e:
		return None

url = input('Enter url(Press Enter to redirect to default URL): ')

if url == '':
	url = 'http://en.wikipedia.org/wiki/Python_(programming_language)'
getData(url)