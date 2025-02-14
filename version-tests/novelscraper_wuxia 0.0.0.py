# Beginning: 7/31/18 1:15PM

import requests
import bs4
import os

num_chapters = 439
save_path = '/media/root/KINGSTON1/Mine/Computer/webnovels/Rebirth of the Thief Who Roamed the World/'

for i in range(num_chapters):
	# Save the chapter to a text file
	current_chapter = i + 1

	response = requests.get('https://www.wuxiaworld.com/novel/rebirth-of-the-thief-who-roamed-the-world/rotwrtw-chapter-%s' % current_chapter )
	soup = bs4.BeautifulSoup(response.text)
	chapter = soup.select('.fr-view p')
	chapter_title = chapter[0].text

	filename = chapter_title + '.txt'
	absolute_path = os.path.join(save_path, filename)

	for para in chapter:
		with open(absolute_path,'a+') as f:
			f.writelines(para.text)
			f.writelines('\n')
			f.writelines('')
			f.writelines('\n')

	break
