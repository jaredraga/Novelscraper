# -*- coding: utf-8 -*-
# Line above makes it backwards compatible for Python 2

# Author: Jared I. Raga ©2019
# Email: jir@gmail.com
# Beginning  Date: 4/19/19 4:25PM
# Completion Date: 
# File saved to disk as: "novelscraper_wuxia 2.1.1.py"

from requests.packages.urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter
from logger import setup_custom_logger
import tkinter as tk
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
	'''proxies = {
		'http': '157.230.57.151:80',
		'https': '178.128.234.188:80'
	} # Proxies from free-proxy.cz (Some proxies reset connection after several downloads...)'''

	response = requests_session.get(url, headers={'User-agent':user_agent})#, proxies=proxies)
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

def update_progress():
	current_progress = '%s/%s chapters downloaded' % (downloaded_chapters, to_downloads_amount)

	progress['text'] = current_progress



#** User variables **#
save_path = 'C:\\Users\\Roland\\Desktop\\test' # !!!MUST create a folder with that novel name
novel_url = 'https://www.wuxiaworld.com/novel/sovereign-of-the-three-realms/sotr-chapter-' # !!!MUST copy the whole URL here. EXCEPT the chapter number
backup_url = 'https://www.wuxiaworld.com/novel/sovereign-of-the-three-realms/chapter-' # Sometimes the URL changes format so it's important to have the backup URL
start_at_chap = 1 # * Change this based on where you want to start
end_at_chap = 10 # * Change this based on where you want to END

to_downloads_amount = end_at_chap - (start_at_chap-1)
downloaded_chapters = 0
current_chapter = start_at_chap
app_version = '2.1.1'
logger = setup_custom_logger(app_version)
user_agent = ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9') # Wuxiaworld blocks our UserAgent
# Get User Agents here: https://deviceatlas.com/blog/list-of-user-agent-strings

# print('UserAgent:'+ user_agent +'\n')

# GUI Notification
win = tk.Tk()
notification_text = tk.StringVar()
progress = tk.Label(win, textvariable=notification_text)
progress.grid(column=0, row=0)

response = 0

# Main
def run_scraper():

	global downloaded_chapters
	global current_chapter
	global response

	if current_chapter <= end_at_chap:
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
			notification_text.set("%s/%s chapters downloaded" % (downloaded_chapters, to_downloads_amount))
			win.after(1, run_scraper)
			

		# Parsing/Processing the HTML File
		soup = bs4.BeautifulSoup(response.str(), 'html.parser') # response.text
		chapter = soup.select('.fr-view p') # A list data type. stores each paragraph in separate sections.
		chapter_title = soup.select('.caption.clearfix h4')[0].text

		filename = chapter_title + '.txt'
		filename = remove_invalid_char(filename)
		absolute_path = os.path.join(save_path, filename)
		
		# Parsing paragraphs
		for para in chapter:
			try:
				with open(absolute_path,'a+') as f:
					f.writelines(para.decode('utf-8')) # The received html is utf8 encoded # para.text.encode('utf-8')
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
		current_chapter += 1

		notification_text.set("%s/%s chapters downloaded" % (downloaded_chapters, to_downloads_amount))
		win.after(1, run_scraper)

	else:
		notification_text.set("Thank you for using Wuxia Novelscraper, Come again!")


notification_text.set("0/%s chapters downloaded" % to_downloads_amount)
win.after(1, run_scraper)

win.mainloop()