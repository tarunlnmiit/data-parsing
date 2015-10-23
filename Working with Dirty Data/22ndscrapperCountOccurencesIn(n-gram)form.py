from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re
import string
import operator

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
	output = {}
	for i in range(len(input)-n+1):
		ngramTemp = ' '.join(input[i:n+i])
		if ngramTemp not in output:
			output[ngramTemp] = 0
		output[ngramTemp] += 1
	return output

def getData(url):
	try:
		content = str(urlopen(url).read(), 'utf-8')
	except HTTPError as e:
		return None
	try:
		ngrams = getNgrams(content, 2)
		sortedNgrams = sorted(ngrams.items(), key=operator.itemgetter(1), reverse=True)
		print (sortedNgrams)
	except AttributeError as e:
		return None

url = input('Enter url(Press Enter to redirect to default URL): ')

if url == '':
	url = 'http://pythonscraping.com/files/inaugurationSpeech.txt'
getData(url)