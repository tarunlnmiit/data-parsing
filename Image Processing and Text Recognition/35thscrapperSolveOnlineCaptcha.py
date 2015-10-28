from urllib.request import urlopen, urlretrieve
from urllib.error import HTTPError
from bs4 import BeautifulSoup
from PIL import Image, ImageOps
import subprocess
import requests

def cleanImage(imagePath):
	image = Image.open(imagePath)
	image = image.point(lambda x: 0 if x<143 else 255)
	borderImage = ImageOps.expand(image, border=20, fill='white')
	borderImage.save(imagePath)

def getCaptcha(url):
	try:
		html = urlopen(url)
	except HTTPError as e:
		return None
	try:
		bsObj = BeautifulSoup(html)
		# Gather pre populated form values
		imageLocation = bsObj.find('img', {'title': 'Image CAPTCHA'})['src']
		formBuildId = bsObj.find('input', {'name': 'form_build_id'})['value']
		captchaSid = bsObj.find('input', {'name': 'captcha_sid'})['value']
		captchaToken = bsObj.find('input', {'name': 'captcha_token'})['value']
		captchaUrl = 'http://pythonscraping.com' + imageLocation

		urlretrieve(captchaUrl, 'captcha.jpg')
		cleanImage('captcha.jpg')

		p = subprocess.Popen(['tesseract', 'captcha.jpg', 'captcha'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		p.wait()
		f = open('captcha.txt', 'r')

		# Clena any whitespace characters
		captchaResponse = f.read().replace(' ', '').replace('\n', '')
		print ('Captcha solution attempt: '+captchaResponse)

		if len(captchaResponse) == 5:
			params = {'captcha_token': captchaToken, 'captcha_sid': captchaSid, 'form_id': 'comment_node_page_form', 'form_build_id': formBuildId, 'captcha_response': captchaResponse, 'name': 'Tarun Gupta', 'subject': 'Random Subject',           'comment_body[und][0][value]': '...and I am definitely not a bot'}
			r = requests.post('http://www.pythonscraping.com/comment/reply/10',	data=params)
			responseObj = BeautifulSoup(r.text)
			if responseObj.find('div', {'class': 'messages'}) is not None:
				print (responseObj.find('div', {'class': 'messages'}).get_text())
		else:
			print ('There was a problem reading the CAPTCHA properly')

	except AttributeError as e:
		return None

getCaptcha('http://www.pythonscraping.com/humans-only')