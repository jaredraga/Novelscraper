# Author: Jared I. Raga ©2018
# Email: jir@gmail.com
# Beginning  Date: 7/24/18 2:12PM
# Completion Date:
# Program Name: Novelscraper: Requests
# Program Ver.:1.0.0

# Diary:
# 7/26/18 11:35PM
#	Fuck this is impossible, I don't think I will ever finish this project. Dealing with live javascript is a tedious task.

import bs4
import requests
from selenium import webdriver

browser = webdriver.PhantomJS()
browser.get('https://www.webnovel.com/book/7817013305001305/The-Strongest-System')

html_source = browser.page_source

novel_soup = bs4.BeautifulSoup(html_source.text)