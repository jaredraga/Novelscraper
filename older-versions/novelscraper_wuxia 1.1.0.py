# Author: Jared I. Raga ©2018
# Email: jir@gmail.com
# Beginning  Date: 7/31/18 1:15PM
# Completion Date: 7/31/18 1:50PM
# Program Name: Wuxia Novelscraper
# Program Ver.: 1.1.0

from requests.packages.urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter
from logger import setup_custom_logger
import requests
import bs4
import sys
import os

signature ='''Wuxia Novelscraper

Please follow the instructions to get the best out of this software.

The non-permitted use of this software in any means possible is prohibited.
Please contact the author for more information.
You can contact me at: jir@gmail.com

Author: Jared I. Raga ©2018
Email: jir@gmail.com
Beginning  Date: 7/31/18 1:15PM
Completion Date: 7/31/18 1:50PM
Program Name: Wuxia Novelscraper
Program Ver.: 1.1.0
'''

exit_message = 'Thank you for using Wuxia Novelscraper!'


def requests_session(url):
	''' Try downloading the page 5 times before giving up '''
	requests_session = requests.Session()
	requests_retries = Retry(total=5, backoff_factor=1, status_forcelist=[ 502, 503, 504 ])
	requests_session.mount('http://', HTTPAdapter(max_retries=requests_retries))
	response = requests_session.get(url, headers={'User-agent':bot_name})

	return response

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


''' Start of the program '''
app_version = '1.1.0'
logger = setup_custom_logger(app_version)
bot_name = ('Wuwuro Bot %s' %app_version)

print('%s:' % bot_name)

''' These are the changeable variables '''
save_path = '/media/root/KINGSTON1/Mine/Computer/webnovels/Against the Gods/' # * MUST create a folder with the novel name
novel_url = 'https://www.wuxiaworld.com/novel/against-the-gods/atg-chapter-' # * MUST copy the whole URL here. EXCEPT the chapter number
start_at_chap = 1097 # * MUST change this based on where you want to start
end_at_chap = 1146 # * MUST change this based on where you want to END
''' These are the changeable variables '''

for current_chapter in range(start_at_chap, end_at_chap + 1):
	''' Starting the scraper '''
	chapter_url = novel_url + str(current_chapter)
	

	''' Download the page source, Get the chapter, Log errors '''
	print('Downloading Chapter-%s (%s)' % (current_chapter, chapter_url))
	try:
		response = requests_session(chapter_url)
	except Exception as e:
		logger.info('Failed to download %s' % chapter_url, exc_info=True)
		continue

	''' Parsing the HTML File '''
	soup = bs4.BeautifulSoup(response.text, 'html.parser')
	chapter = soup.select('.fr-view p')
	chapter_title = chapter[0].text
	print('Downloaded %s' % chapter_title)


	''' Saving it to a text file '''
	filename = chapter_title + '.txt'
	filename = remove_invalid_char(filename)
	absolute_path = os.path.join(save_path, filename)
	
	try:
		# For paragraph in chapter
		for para in chapter:
			with open(absolute_path,'a+') as f:
				f.writelines(para.text)
				# Retain the previous format. Empty line after each para.
				f.writelines('\n')
				f.writelines('')
				f.writelines('\n')
	except Exception as e:
		logger.error('Failed to save to %s' % filename, exc_info=True)

	print("Saved to '%s' " % filename)
	print()

print(exit_message)
