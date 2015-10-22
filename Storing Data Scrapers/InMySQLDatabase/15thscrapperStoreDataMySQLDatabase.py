from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import random
import re
import datetime
import pymysql

conn = pymysql.connect(host='localhost', unix_socket='/tmp/mysqld.sock', user='root', passwd='pass', db='mysql', charset='utf8')
cur = conn.cursor()
cur.execute('USE scraping') # scraping is a local database on my local machine

random.seed(datetime.datetime.now())

def store(title, content):
	cur.execute('INSERT INTO pages (title, content) VALUES ("%s", "%s")', (title, content))
	cur.connection.commit()

def getLinks(articleUrl):
	try:
		html = urlopen('http://en.wikipedia.org'+articleUrl)
	except HTTPError as e:
		return None
	try:
		bsObj = BeautifulSoup(html)
		title = bsObj.find('h1').get_text()
		content = bsObj.find('div', {'id':'mw-content-text'}).find('p').get_text()
		store(title, content)
		links = bsObj.find('div', {'id':'bodyContent'}).findAll('a', href=re.compile('^(/wiki/)((?!:).)*$'))
		return links
	except AttributeError as e:
		return None

links = getLinks("/wiki/Kevin_Bacon")

try:
	while len(links) > 0:
		newArticle = links[random.randint(0, len(links)-1)].attrs['href']
		print (newArticle)
		links = getLinks(newArticle)
finally:
	cur.close()
	conn.close()