import csv
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def getTableRows(url):
	try:
		html = urlopen(url)
	except HTTPError as e:
		return None
	try:
		bsObj = BeautifulSoup(html)
		table = bsObj.findAll('table', {'class':'wikitable'})[0]
		rows = table.findAll('tr')
	except AttributeError as e:
		return None
	return rows

url = 'http://en.wikipedia.org/wiki/Comparison_of_text_editors'
rows = getTableRows(url)

csvFile = open('editors.csv', 'wt')
writer = csv.writer(csvFile)

try:
	for row in rows:
		csvRow = []
		for cell in row.findAll(['td', 'th']):
			csvRow.append(cell.get_text())
			writer.writerow(csvRow)
finally:
	csvFile.close()