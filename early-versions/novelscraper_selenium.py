#!/usr/bin/env python


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, UnexpectedAlertPresentException, WebDriverException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pyautogui
import tkinter
import time

# Author: Jared I. Raga ©2018
# Email: jir@gmail.com
# Beginning  Date: 7/9/18
# Completion Date: 7/12/18
# Program Name: Novel Webscraper

#Created on:
#7/9/18
#Author: Jared I. Raga

# Problem:
# I'm already at the PrivateBin site but 
# I don't know what method to use 
# to save the Chapther to a text file

# Add:
# Configure ctrl + a and ctrl + c to be done with selenium not pyautogui

# Make code clean - Done 7/12/18


# Flowchart:
# > Open webdriver or browser - open_firefox_for_webnovel():
# > Get Information - Title, Chapter Number, etc. - get_novel_info():
# > Open Google and do a Search - open_google(*search term*):
# > Wait for Google to Load and Click the First Result
# > The Reddit-Side Execution - Go to Old Reddit and Click the Paste Bin Link
# > Wait for Paste Bin to Load
# > Copy the Contents of the Website
# > Read the Text from Clipboard and Store it in a Variable
# > Write the Text into a File and Name the File 

# 7/12/18
# Search how to send hotkeys using selenium
# Search the purpose of if __name__ == '__main__':

def main():

	print('''Novel Webscraper

Please follow the instructions to get the best out of this software.

The non-permitted use of this software in any means possible is prohibited.
Please contact the author for more information.
You can contact me at: jir@gmail.com

Author: Jared I. Raga ©2018
Email: jir@gmail.com
Beginning  Date: 7/9/18
Completion Date: 7/12/18
Program Name: Novel Webscraper
''')
	time.sleep(3)

	novelTitle, currentChapterNumber, stopAtChapterNumber = get_novel_info()

	browser = open_firefox_with_webnovel_profile()
	
	#novelTitle = 'Alchemy Emperor of the Divine Dao'
	#startAtChapterNumber = 251
	#currentChapterNumber = startAtChapterNumber
	#stopAtChapterNumber = 260

	while currentChapterNumber <= stopAtChapterNumber:
		print_novel_info(novelTitle, startAtChapterNumber, currentChapterNumber, stopAtChapterNumber)

		searchForWebnovelReddit = 'reddit ' + novelTitle + ' ' + str(currentChapterNumber)
		open_google(browser, searchForWebnovelReddit)

		wait_for_google_to_load_and_click_first_result(browser)

		# Go to Reddit then to Old Reddit and Click the Paste Bin Link
		reddit_side_webnovel(browser, novelTitle)

		# Wait for Paste Bin to Load then click the Raw Text Button
		paste_bin_side_webnovel(browser)
		
		ctrl_c_website_content(browser)

		chapterContents = read_text_from_clipboard()
		
		chapterFilename = novelTitle + ' ' + str(currentChapterNumber) + '.txt'	
		write_text_to_file(chapterFilename, chapterContents)

		currentChapterNumber += 1

		browser.delete_all_cookies()
		
	print('Finished Copying %s Chapter %s-%s' % [novelTitle, startAtChapterNumber, stopAtChapterNumber])
	     


def get_novel_info():

	print('''
--------------------
 Provide Novel Info 	
--------------------
(Provide the Exact Title of the Novel because that is what the program will use in naming the text files!)
''')
	print('Novel Name (Verbatim):')
	novel = input()

	print('Chapter Start:(The chapter that you want to start with)')
	chapterStart = int(input())

	print('Chapter End:(The chapter you want the program to end copying)')
	chapterEnd = int(input())

	return [novel, chapterStart, chapterEnd]

def print_novel_info(novel, startingChapter, currentChapter, endingChapter):
	print()
	print('Novel: %s' %novel)
	print('Starting Chapter: %s' %startingChapter)
	print('Current Chapter : %s' %currentChapter)
	print('Ending Chapther : %s' %endingChapter)
	print()

def open_firefox_with_webnovel_profile():

	firefoxProfile = webdriver.FirefoxProfile()
	# Set the network.http.spdy... to False; it doesn't allow for any website to open
	firefoxProfile.DEFAULT_PREFERENCES['frozen']["network.http.spdy.enforce-tls-profile"] = False
	
	# This disables the driver from opening a new window for every link
	firefoxProfile.DEFAULT_PREFERENCES["browser.link.open_newwindow.restriction"] = 1

	browser = webdriver.Firefox(firefoxProfile)

	return browser

def open_google(browser, searchTerm):
	print('Waiting for Google...')
	browser.get("https://www.google.com")
	
	delay = 600
	try:
		myElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.ID, 'lst-ib')))
		print("Google is ready!")
	except TimeoutException:
		print("Google took too much time!")

	googleSearchBar = browser.find_element_by_id('lst-ib')
	googleSearchBar.send_keys(searchTerm)
	googleSearchBar.send_keys(Keys.RETURN) # hit enter after you enter search text

def wait_for_google_to_load_and_click_first_result(browser):
	print('Waiting for Google Results...')
	# Wait up to 10 Minutes for Google to Load
	delay = 600
	try:
		myElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH, "//div[@class='rc']")))
		print("Google Result is ready!")
	except TimeoutException:
		print("Google Result took too much time!")

	# Click the First Google Result
	googleSearchResult = browser.find_elements(By.XPATH, "//div[@class='rc']")[0] #Make a List of Results and Get the First One
	googleSearchResult.find_element(By.XPATH, "//h3[@class='r']").click() #Click its Href

def reddit_side_webnovel(browser, novelTitle):
	print('Waiting for Reddit...')

	# Wait for Reddit to Load
	delay = 600
	try:
		myElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located(((By.PARTIAL_LINK_TEXT, "Old Reddit"))))
		print("Reddit is ready!")
		time.sleep(1)
		myElem.click()
	except TimeoutException:
		print("Reddit took too much time!")


	print('Waiting for Old Reddit...')
	# Go to Old Reddit because New Reddit Opens New Windows when Clicking Links
	
	time.sleep(3)

	# Wait for Old Reddit to Load
	delay = 600
	try:
		WebDriverWait(browser, delay).until(EC.url_contains('old.reddit.com'))
		print("Old Reddit is ready!")
	except TimeoutException:
		print("Old Reddit took too much time!")


	# Click the Paste Bin Link
	delay = 600
	try:
		myElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located(((By.PARTIAL_LINK_TEXT, 'Alchemy Emperor'))))
		time.sleep(1)
		myElem.click()
	except TimeoutException:
		print("Cannot find Paste Bin link!")

def paste_bin_side_webnovel(browser):
	print('Waiting for Paste Bin...')

	delay = 600
	try:
		WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH, "//div[@class = 'row']")))
		print("Paste Bin is ready!")
	except TimeoutException:
		print("Paste Bin took too much time!")

	# Click Paste Bin 'Raw Text' button
	#browser.find_element(By.XPATH, "//button[@id = 'rawtextbutton']").click()
	time.sleep(1)

def ctrl_c_website_content(browser):
	print('Copying Website...')

	pyautogui.hotkey('ctrl','a')
	pyautogui.hotkey('ctrl','c')

	print('Copied Website')

def read_text_from_clipboard():
	print('Reading Clipboard...')

	# Using tkinter to read text from clipboard
	root = tkinter.Tk()
	root.withdraw() # Hide the main window (optional)
	clipboardText = root.clipboard_get()

	print('Read Clipboard!')

	return clipboardText

def write_text_to_file(filename, fileContents):
	print('Writing to Text File...')

	with open(filename,'w+') as f:
		f.writelines(fileContents)

	print('Written to Text File succesfully!')

if __name__ == '__main__':
	main()
