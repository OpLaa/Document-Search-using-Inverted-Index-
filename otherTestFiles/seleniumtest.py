#!/usr/bin/env python

from selenium import webdriver

import os

browser = webdriver.Chrome()
browser.get("file:///home/venkatram/PycharmProjects/invertedIndex/projecthtml/index.html")
browser.maximize_window()
query=browser.find_element_by_class_name('button')
check=browser.find_element_by_id('check')


def getquery():
    print("query goes here"+str(qrystring))
    check.clear()
    check.send_keys('false')


while True:
    if(check.get_attribute('value')=='true'):
        qrystring=query.get_attribute('value')
        getquery()
#file:///home/venkatram/Desktop/animated-search-box-pure-css/
#file:///home/venkatram/PycharmProjects/invertedIndex/projecthtml/index.html
#/home/PycharmProjects/invertedIndex/projecthtml/index.html
#https://www.facebook.com/
#browser.find_element_by_id("email").send_keys("venkatram624@gmail.com")
#browser.find_element_by_id("pass").send_keys("venkat1997164")
#browser.find_element_by_id("loginbutton").click()
#browser.find_element_by_id("findFriendsNav").click()
