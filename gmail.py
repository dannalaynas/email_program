from selenium import webdriver
browser = webdriver.Firefox()

browser.get('http://gmail.com')

emailElem = browser.find_element_by_id('Email')
emailElem.send_keys('yuba.danna@gmail.com')

loginElem = browser.find_element_by_id('next')
loginElem.click()

passwordElem = browser.find_element_by_id('Passwd')
passwordElem.send_keys('pie1234567')

passwordElem.submit()

loginElem = browser.find_element_by_id('signIn')
loginElem.click()
