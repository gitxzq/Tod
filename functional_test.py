#coding=utf-8

from selenium import webdriver

driver=webdriver.Firefox()
driver.get('http://localhost:8000')
try:
	assert 'Django' in driver.title	
except AssertionError:
	print ('AssertionError')
	# pass
driver.close()