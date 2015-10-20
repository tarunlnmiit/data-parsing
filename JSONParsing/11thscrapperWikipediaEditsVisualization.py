''' a basic script that crawls Wikipedia, looks for revision history pages, and then looks for IP addresses on those revision history pages'''

from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re
import random
import datetime
import json

random.seed(datetime.datetime.now())

def getLinks(articleUrl):
	try:
		html = urlopen('http://en.wikipedia.org'+articleUrl)
	except HTTPError as e:
		return None
	try:
		bsObj = BeautifulSoup(html)
	except AttributeError as e:
		return None
	return bsObj.find('div', {'id':'bodyContent'}).findAll('a', href=re.compile('^(/wiki/)((?!:).)*$'))

def getHistoryIPs(pageUrl):
	# Format of revision history page is :
	# http://en.wikipedia.org/w/index.php?title=Title_in_URL&action=history
	pageUrl = pageUrl.replace('/wiki/', '')
	historyUrl = 'http://en.wikipedia.org/w/index.php?title='+pageUrl+'&action=history'
	print ('history url is: '+historyUrl)
	try:
		html = urlopen(historyUrl)
	except HTTPError as e:
		return None
	try:
		bsObj = BeautifulSoup(html)
	except AttributeError as e:
		return None
	# finds only the links with class 'mw-anonuserlink' which has IP addresses instead of usernames
	ipAddresses = bsObj.findAll('a', {'class':'mw-anonuserlink'})
	addressList = set()
	for ipAddress in ipAddresses:
		addressList.add(ipAddress.get_text())
	return addressList

def getCountry(ipAddress):
	try:
		response = urlopen('http://freegeoip.net/json/'+ipAddress).read().decode('utf-8')
	except HTTPError as e:
		return None
	responseJson = json.loads(response)
	return responseJson.get('country_name') 

links = getLinks('/wiki/'+input('Enter name of Wikipedia Page: '))

while len(links) > 0:
	fhand = open('wikipediaEditVisualizationdata.txt','a')
	for link in links:
		print ('-----------------')
		historyIPs = getHistoryIPs(link.attrs['href'])
		for historyIP in historyIPs:
			country = getCountry(historyIP)
			if country is not None:
				fhand.write(historyIP+' is from '+country+'\n')
				print (historyIP+' is from '+country)
	fhand.close()
	newLink = links[random.randint(0, len(links)-1)].attrs['href']
	links = getLinks(newLink)