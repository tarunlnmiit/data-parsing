import time
import subprocess
from urllib.request import urlretrieve
from selenium import webdriver

# Create new selenium driver
#driver = webdriver.PhantomJS(executable_path='../../phantomjs/bin/phantomjs')
driver = webdriver.Firefox()
driver.get('http://www.amazon.com/War-Peace-Leo-Nikolayevich-Tolstoy/dp/1427030200')
time.sleep(3)

# Click on the book preview button
driver.find_element_by_id('sitbLogoImg').click()
imageList = set()

# Wait for the page to load
time.sleep(10)

# While the right arrow is available for clicking, turn through pages
print (driver.find_element_by_id('sitbReaderRightPageTurner').get_attribute('style'))
while 'pointer' in driver.find_element_by_id('sitbReaderRightPageTurner').get_attribute('style'):
	driver.find_element_by_id('sitbReaderRightPageTurner').click()
	time.sleep(2)

	# Ger any new pages that have loaded (multiple pages can load at once, but duplicates will not be added to a set)
	pages = driver.find_element_by_xpath('//div[@class="pageImage"]/div/img')
	for page in pages:
		image = page.get_attribute('src')
		imageList.add(image)

driver.quit()

# Start processing the images with Tesseract
for image in sorted(imageList):
	urlretrieve(image, 'page.jpg')
	p = subprocess.Popen(['tesseract', 'page.jpg', 'page'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	p.wait()
	f = open('page.txt', 'r')
	print (f.read())