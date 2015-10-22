from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re
import pymysql

conn = pymysql.connect(host='localhost', unix_socket='/tmp/mysqld.sock', user='root', passwd='pass', db='mysql', charset='utf8')
cur = conn.cursor()
cur.execute('USE wikipedia')

def insertPageIfNotExists(url):
	cur.execute('SELECT * FROM pages WHERE url = %s', (url))
	if cur.rowcount == 0:
		cur.execute('INSERT INTO pages (url) VALUES (%s)', (url))
		conn.commit()
		return cur.lastrowid
	else:
		return cur.fetchone()[0]

def insertLink(fromPageId, toPageId):
	cur.execute('SELECT * FROM links WHERE fromPageId = %s AND toPageId = %s', (int(fromPageId), int(toPageId)))
	if cur.rowcount == 0:
		cur.execute('INSERT INTO links (fromPageId, toPageId) VALUES (%s, %s)', (int(fromPageId), int(toPageId)))
		conn.commit()

pages = set()

def getLinks(pageUrl, recursionLevel):
	global pages
	if recursionLevel > 4:
		return;
	pageId = insertPageIfNotExists(pageUrl)
	try:
		html = urlopen('http://en.wikipedia.org'+pageUrl)
	except HTTPError as e:
		return None
	try:
		bsObj = BeautifulSoup(html)
		for link in bsObj.findAll('a', href=re.compile('^(/wiki/)((?!:).)*$')):
			insertLink(pageId, insertPageIfNotExists(link.attrs['href']))
			if link.attrs['href'] not in pages:
				# We have encountered a new Page, add it and search it for links
				newPage = link.attrs['href']
				pages.add(newPage)
				getLinks(newPage, recursionLevel+1)
	except AttributeError as e:
		return None

url = input('Enter wiki URL in form /wiki/Kevin_Bacon (Press Enter to redirect to default URL): ')		
if url == '':
	url = '/wiki/Kevin_Bacon'
getLinks(url, 0)
cur.close()
conn.close()