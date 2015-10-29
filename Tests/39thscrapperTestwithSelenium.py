from selenium import webdriver

page = input('Enter Wikipedia Page Title (Press Enter to redirect to default URL): ')

if page == '':
	url = 'http://en.wikipedia.org/wiki/Monty_Python'
else:
	url = 'http://en.wikipedia.org/wiki/'+'_'.join(page.split())
driver = webdriver.PhantomJS(executable_path='../../phantomjs/bin/phantomjs')
driver.get(url)
assert page in driver.title
driver.close()