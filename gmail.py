from selenium import webdriver
browser = webdriver.Firefox()

browser.get('http://gmail.com')

emailElem = browser.find_element_by_id('Email')
emailElem.send_keys('yuba.danna@gmail.com')

loginElem = browser.find_element_by_id('next')
loginElem.click()

passwordElem = browser.find_element_by_name('Passwd')
passwordElem.send_keys('pie1234567')

passwordElem.submit()

loginElem = browser.find_element_by_id('signIn')
loginElem.click()

composeElem = browser.find_element_by_class('T-I J-J5-Ji T-I-Ke L3')
composeElem.click()

print('Recipiens\' Email?')
sendTo = input()

sendtoElem = browser.find_element_by_id(':9w')
sendtoElem.send_keys(sendTo)

print('Subject')
subjectline = input()

subjectElem = browser.find_element_by_id(':9h')
subjectElem.send_keys(subjectLine)

print('Input Your Messege')
bodyline = input()

sendtoElem = browser.find_element_by_id(':97')
sendtoElem.send_keys (bodyLine)
