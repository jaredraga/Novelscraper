#!/usr/bin/python3

import requests, bs4, sys, os, re, time, optparse
from requests.packages.urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter
from sys import stdout

# Take argv switches, beautify cli with colors, stop logging downloaded, stop logging, remove process_text() and find_title() functions, no longer supporting python2

def requests_session(url):
	# Try downloading the page 7 times before giving up
	requests_session = requests.Session()
	requests_retries = Retry(total=7, backoff_factor=1, status_forcelist=[ 502, 503, 504 ])
	requests_session.mount('http://', HTTPAdapter(max_retries=requests_retries))

	response = requests_session.get(url, headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.27 Safari/537.36'})
	return response

def dynamic_notif(dled, total):
	print('%s/%s chapters downloaded' % (dled, total))
	
	if dled != total:
		# Clear line
		print('\033[F', end='')

def fix_invalid_title(title):
		# Interpret quotes and colons
		title = title.replace('"',"'")
		title = title.replace(':','-')

		# Replace everything else with underscores
		for invalid in '" * / : < > ? \\ |'.split():
			title = title.replace(invalid,'_')
		
		return title

def main():
	# Creates CLI switches and stores in variables
	parser = optparse.OptionParser(sys.argv[0]+' '+
	'''-o <output folder> -u <first chapter url> -r <download range>
	Example: novelscraper -o ~/Downloads -u https://www.wuxiaworld.com/novel/a-will-eternal/awe-chapter-1 -r 1-100''')
	parser.add_option('-o', dest='output_folder', type='string', help='set the folder to save files')
	parser.add_option('-u', dest='chapter_url', type='string', help='specify the URL of the first chapter')
	parser.add_option('-r', dest='download_range', type='string', help='specify the range to download [eg:1-100]')
	(options, args) = parser.parse_args()
	output_folder = options.output_folder
	chapter_url = options.chapter_url
	download_range = options.download_range

	# Remove chapter number from link
	chapter_url = re.sub(r'[0-9]+', '', chapter_url) 
	# Find the last occurance of "/" and replace it
	backup_chapter_url = chapter_url[:chapter_url.rfind('/')] + '/chapter-'
	
	split_download_range = download_range.split('-')
	start_chap, end_chap = int(split_download_range[0]), int(split_download_range[1])+1

	total_to_download = end_chap - start_chap
	already_downloaded = 0

	print('0/%s chapters downloaded' % total_to_download)
	print('\033[F', end='')
	for current_chapter in range(start_chap, end_chap):

		# Add chapter numbers to the end of URLs
		current_chapter_url = chapter_url + str(current_chapter) 
		backup_current_chapter_url = backup_chapter_url + str(current_chapter)

		# Download chapter
		response = requests_session(current_chapter_url)
		if response.status_code != 200: # Error downloading
			echo('Failed downloading Main URL')

			# Try Backup URL
			response = requests_session(backup_current_chapter_url)

			if response.status_code != 200:
				echo('Failed downloading Backup URL')
				sys.exit()

		# Parsing the Download
		soup = bs4.BeautifulSoup(response.text, 'html.parser')
		# Select all paragraph elements with the class="fr-view" attribute
		chapter = soup.select('.p-15 > .fr-view > p')
		chapter_title = soup.select('.caption.clearfix h4')[0].text

		filename = chapter_title + '.txt'
		filename = fix_invalid_title(filename)
		absolute_path = os.path.join(output_folder, filename)
		
		# Parsing paragraphs
		for para in chapter:
			try:
				with open(absolute_path,'w+') as f:
					f.writelines(para.text)
					# Manually add newlines for each paragraph
					f.writelines('\n')
					f.writelines('')
					f.writelines('\n')
			except Exception as e:
				echo('Failed to save to %s' % filename)
				sys.exit()

		already_downloaded += 1
		dynamic_notif(already_downloaded, total_to_download)
		
	sys.exit(0)

if __name__ == "__main__":
	main()