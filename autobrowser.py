from splinter import Browser


browser = Browser('chrome')

browser.visit('http://google.com')
input_element = browser.find_by_name('q')
input_element.fill('splinter - python acceptance testing for web applications')