from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re, datetime, random

pages = set()
allExtLinks = set()
allIntLinks = set()
random.seed(datetime.datetime.now())

# Retrieval of a list of all internal links on a page
def getInternalLinks(bsObj, includeUrl):
	internalLinks = []
	# finds all links that begin with a '/'
	for link in bsObj.findAll('a', href=re.compile('^(/|.*'+includeUrl+')')):
		if link.attrs['href'] is not None:
			if link.attrs['href'] not in internalLinks:
				internalLinks.append(link.attrs['href'])
	return internalLinks

# Retrieval of a list of all external links on a page
def getExternalLinks(bsObj, excludeUrl):
	externalLinks = []
	# finds all links that begin with 'http' or 'www' that do not contain the current URL
	for link in bsObj.findAll('a', href=re.compile('^(http|www)((?!'+excludeUrl+').)*$')):
		if link.attrs['href'] is not None:
			if link.attrs['href'] not in externalLinks:
				externalLinks.append(link.attrs['href'])
	return externalLinks

def splitAddress(address):
	addressParts = address.replace('http://', '').split('/')
	return addressParts

def getRandomExternalLink(startingPage):
	try:
		html = urlopen(startingPage)
	except HTTPError as e:
		return None
	try:
		bsObj = BeautifulSoup(html)
		externalLinks = getExternalLinks(bsObj, splitAddress(startingPage)[0])
		if len(externalLinks) == 0:
			internalLinks = getInternalLinks(startingPage)
			return getNextExternalLink(internalLinks[random.randint(0, len(internalLinks)-1)])
		else:
			return externalLinks[random.randint(0, len(externalLinks)-1)]
	except AttributeError as e:
		return None

def getAllExternalLinks(siteUrl):
	try:
		html = urlopen(siteUrl)
	except HTTPError as e:
		return None
	try:
		bsObj = BeautifulSoup(html)
		internalLinks = getInternalLinks(bsObj, splitAddress(siteUrl)[0])
		externalLinks = getExternalLinks(bsObj, splitAddress(siteUrl)[0])
	except AttributeError as e:
		return None

	for link in externalLinks:
		if link not in allExtLinks:
			allExtLinks.add(link)
			print (link)
	for link in internalLinks:
		if link not in allIntLinks:
			print ('About to get link: '+link)
			allIntLinks.add(link)
			getAllExternalLinks(link)

def followExternalOnly(startingSite):
	externalLink = getRandomExternalLink('http://oreilly.com')
	print ('Random external link is: '+externalLink)
	followExternalOnly(externalLink)
	
inp = input('Enter 1 for random external links, 2 for all external links: ')
if inp == '1':
	followExternalOnly('http://oreilly.com')
elif inp == '2':
	getAllExternalLinks('http://oreilly.com')