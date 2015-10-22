from urllib.request import urlopen
from urllib.error import HTTPError
from io import StringIO
import csv

def getData(url):
	try:
		data = urlopen(url).read().decode('ascii', 'ignore')
	except HTTPError as e:
		return None
	dataFile = StringIO(data)
	# DictReader will return values as dictionary objects 
	# reader will return values as list objects 
	# reader is fast as compared to dictReader
	csvReader = csv.DictReader(dataFile)
	for row in csvReader:
		print (row)

url = input('Enter URL(Press Enter to redirect to default URL): ')
if url == '':
	url = 'http://pythonscraping.com/files/MontyPythonAlbums.csv'
getData(url)		