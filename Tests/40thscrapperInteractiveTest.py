from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

driver = webdriver.PhantomJS(executable_path='../../phantomjs/bin/phantomjs')
driver.get('http://pythonscraping.com/pages/files/form.html')

firstNameField = driver.find_element_by_name('firstname')
lastNameField = driver.find_element_by_name('lastname')
submitButton = driver.find_element_by_id('submit')

#####   METHOD 1  #####
firstNameField.send_keys('Tarun')
lastNameField.send_keys('Gupta')
submitButton.click()
######################

#####   METHOD 2  #####
actions = ActionChains(driver).click(firstNameField).send_keys('Tarun').click(lastNameField).send_keys('Gupta').send_keys(Keys.RETURN)
actions.perform()
######################

print (driver.find_element_by_tag_name('body').text)
driver.close()