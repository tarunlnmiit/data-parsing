import requests

files = {'uploadFile': open('../../img3.png', 'rb')}
r = requests.post("http://pythonscraping.com/pages/processing2.php", files=files)
print(r.text)