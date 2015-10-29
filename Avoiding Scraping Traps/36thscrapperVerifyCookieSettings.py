import requests
from bs4 import BeautifulSoup

session = requests.Session()
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:41.0) Gecko/20100101 Firefox/41.0', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
url = 'https://www.whatismybrowser.com/developers/what-http-headers-is-my-browser-sending'
req = session.get(url, headers=headers)

bsObj = BeautifulSoup(req.text)
print (bsObj.find('table', {'class': 'table-striped'}).get_text())