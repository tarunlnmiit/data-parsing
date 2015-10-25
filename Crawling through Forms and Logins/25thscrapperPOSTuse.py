import requests

params = {'firstname':'Tarun', 'lastname':'Gupta'}
r = requests.post('http://pythonscraping.com/files/processing.php', data=params)
print (r.text)