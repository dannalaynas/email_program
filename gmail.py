from selenium import webdriver
browser = webdriver.Firefox()

browser.get('http://gmail.com')
emailElem = browser.find_element_by_id('Email')
emailElem.send_keys('')

passwordElem = browser.find_element_by_id('Passwd')
passwordElem.send_keys('')
passwordElem.submit()
