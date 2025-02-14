# -*- coding: utf-8 -*-
# Line above makes it backwards compatible for Python 2

# Author: Jared I. Raga ©2019
# Email: jir@gmail.com
# Beginning  Date: 3/26/19 4:25PM
# Completion Date: 3/27/19 9:35AM
# File saved to disk as: "novelscraper_wuxia 2.1.1.py"

from requests.packages.urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter
from logger import setup_custom_logger
from sys import stdout
import requests
import bs4
import sys
import os
import time

def requests_session(url):
	# Tries downloading the page 5 times before giving up
	requests_session = requests.Session()
	requests_retries = Retry(total=5, backoff_factor=1, status_forcelist=[ 502, 503, 504 ])
	requests_session.mount('http://', HTTPAdapter(max_retries=requests_retries))
	proxies = {
		'http': '178.128.151.27:80',
		'https': '34.201.122.197:80'
	} # Proxies from free-proxy.cz (Some proxies reset connection after several downloads...)

	response = requests_session.get(url, headers={'User-agent':bot_name}, proxies=proxies)
	return response

def find_title(chapter):
	# Printable characters except for spaces, tabs, and newlines
	all_chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~', '\x0b', '\x0c']
	
	for line in chapter:
		for char in line.text:
			if char in all_chars:
				return line.text

def remove_invalid_char(string):
	for char in string:	
		# Spare those who can be spared
		if char == '?':
			return string.replace('?','')
		elif char == '"':
			return string.replace('"',"'")
		elif char == ':':
			return string.replace(':','-')
		# If not, replace them with underscores. It can't be helped
		for invalid in '" * / : < > ? \\ |'.split():
			string = string.replace(invalid,'_')
		return string

def process_text(filename):
	open(filename,'a+') # Create file if it doesn't exist

	# Read content
	with open(filename,'r') as f:
		raw_data = f.readlines()

	# Remove newlines
	# To Python, a string with a newline and a string without is not the same.
	processed_data = []
	for i in range(len(raw_data)):
		processed_data.append(raw_data[i].replace('\n', ''))
	return processed_data



#** User variables **#
save_path = '/root/Desktop/Sovereign of the Three Realms' # !!!MUST create a folder with that novel name
novel_url = 'https://www.wuxiaworld.com/novel/sovereign-of-the-three-realms/sotr-chapter-' # !!!MUST copy the whole URL here. EXCEPT the chapter number
backup_url = 'https://www.wuxiaworld.com/novel/sovereign-of-the-three-realms/chapter-' # Sometimes the URL changes format so it's important to have the backup URL
start_at_chap = 1 # * Change this based on where you want to start
end_at_chap = 500 # * Change this based on where you want to END

to_downloads_amount = end_at_chap - start_at_chap
downloaded_chapters = 0
exit_message = 'Thank you for using Wuxia Novelscraper, Come again!'
app_version = '2.1.1'
logger = setup_custom_logger(app_version)
bot_name = ('I\'m sorry Web Admin!') # Wuxiaworld blocks our UserAgent

print(bot_name + '\n')

''' Starting the scraper '''
for current_chapter in range(start_at_chap, end_at_chap + 1):

	print('%s/%s chapters downloaded' % (downloaded_chapters, to_downloads_amount)) # Dynamic Notification

	chapter_url = novel_url + str(current_chapter) # Add chapter number to URL
	backup_chapter_url = backup_url + str(current_chapter)
	downloaded_log = process_text('downloaded_log.txt')

	# Get chapter
	if (chapter_url not in downloaded_log and backup_chapter_url not in downloaded_log):

		response = requests_session(chapter_url)
		main_url = True

		if response.status_code != 200: # Error downloading
			
			logger.error('Failed to download %s' % chapter_url)
			response = requests_session(backup_chapter_url) # Backup URL

			if response.status_code != 200: # Backup URL failed
				logger.error('Backup URL failed', exc_info=True)
				sys.exit() # Stop the program

			main_url = False

	# Don't download downloaded chapters
	elif chapter_url or backup_chapter_url in downloaded_log:
		downloaded_chapters += 1
		stdout.write('\033[F')

		continue # Start from beginning

	# Parsing/Processing the HTML File
	soup = bs4.BeautifulSoup(response.text, 'html.parser')
	chapter = soup.select('.fr-view p') # A list data type. stores each paragraph in separate sections.
	chapter_title = soup.select('.caption.clearfix h4')[0].text

	filename = chapter_title + '.txt'
	filename = remove_invalid_char(filename)
	absolute_path = os.path.join(save_path, filename)
	
	# Parsing paragraphs
	for para in chapter:
		try:
			with open(absolute_path,'a+') as f:
				f.writelines(para.text.encode('utf-8')) # The received html is utf8 encoded
				# Add spaces after each paragraph
				f.writelines('\n')
				f.writelines('')
				f.writelines('\n')
		except Exception as e:
			logger.error('Failed to save to %s' % filename, exc_info=True)
			sys.exit()

	with open('downloaded_log.txt','a+') as f:
		try:
			if main_url:
				f.writelines(chapter_url)
				f.writelines('\n')
			else:
				f.writelines(backup_chapter_url)
				f.writelines('\n')
			
		except:
			logger.error('Failed to write URL to downloaded_log.txt', exc_info=True)

	downloaded_chapters += 1

	# Dynamic Line
	stdout.write('\033[F') # \033[F is the ANSI escape sequence that clears the line. print('\033[F', end='') for Python 3.

print(exit_message)
sys.exit()
