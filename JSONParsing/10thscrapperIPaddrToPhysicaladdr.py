# This scrapper will use pyhton's JSON pasrsing functions
import json
from urllib.request import urlopen
from urllib.error import HTTPError

def getCountry(ipAddress):
	try:
		response = urlopen('http://freegeoip.net/json/'+ipAddress).read().decode('utf-8')
	except HTTPError as e:
		return None
	responseJson = json.loads(response)
	return responseJson.get('country_code'), responseJson.get('country_name')

print (getCountry(input('Enter Global IP Address: ')))