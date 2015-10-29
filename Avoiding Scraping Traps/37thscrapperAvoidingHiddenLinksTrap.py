from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement

url = input('Enter URL(Press Enter to redirect to default URL): ')
if url == '':
	url = 'http://pythonscraping.com/pages/itsatrap.html'

driver = webdriver.PhantomJS(executable_path='../../phantomjs/bin/phantomjs')
driver.get(url)
links = driver.find_elements_by_tag_name('a')
for link in links:
	if not link.is_displayed():
		print ('The link ' + link.get_attribute('href') + ' is a trap.')

fields = driver.find_elements_by_tag_name('input')
for field in fields:
	if not field.is_displayed():
		print ('Do not change value of ' + field.get_attribute('name'))