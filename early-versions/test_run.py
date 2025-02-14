import bs4

''' Kali Linux's default homepage stored in our computer. '''
html_doc = open('/usr/share/kali-defaults/web/homepage.html')
soup = bs4.BeautifulSoup(html_doc, 'html.parser')


''' Find and list all the links within the tag 'li' under the tag 'div' with the CSS class 'navbar-collapse collapse ' '''

# Beginning: 7/26/18 10:05AM
# Completion: 7/27/18 10:20AM

print('All links under tag <li> within tag <div> with the class="navbar-collapse"')
link_elems = soup.select('.navbar-collapse li')

# By default, return the first 5 links in the links passed by the list 'list_elems'
# , but, if the links returned by the list 'link_elems' is less than 5, we will pass that instead.
num_links = min(5, len(link_elems))

for i in range(num_links):
	print(link_elems[i].select('a')[0].get('href'))
print()

''' Find all the elements with the name 'img' that contains the attribute 'src' and list those 'src' values '''

# Beginning: 7/26/18 10:25AM
# Completion: 7/27/18  10:30AM

print('All the image files within the whole site')
image_elems = soup.select('img[src]')

for i in range(len(image_elems)):
	print(image_elems[i].get('src'))
print()

''' Find the introduction text of Kali Linux under the tag named 'p' that contains the attribute 'align' with the value 'justify' '''

# Beginning: 7/26/18 10:30AM
# Completion: 7/27/18 10:35AM

print('One of The Website\'s Information Text')
intro_title = soup.select('.box-gray h4')
intro_text = soup.select('.box-gray p')

print(intro_title[0].getText())
print(intro_text[0].getText())


''' Find all the Software Titles and their corresponding Logos under the element 'section' with the id attribute with the value 'projects' '''

# Beginning: 7/26/18 10:35AM
# Completion: 7/27/18 10:55AM

print('Kali Softwares and Groups')
# Find all the elements named 'a' within the element with the id "thumbs"
title_elems = soup.select('#thumbs a')
image_elems = soup.select('#thumbs img')

# We want to display every element, so even if the value returned
# by the one of the lists is lesser than the other, we would still display
# all of the strings of the list with the greater len()
num_links = max(len(title_elems), len(image_elems))

for i in range(num_links):
	print('Title: %s' % title_elems[i].get('title'))
	print('Image: %s' % image_elems[i].get('src'))
	print()


''' Find all the social network accounts within the Kali Linux default page '''

# Beginning: 7/26/18 10:55AM
# Completion: 7/27/18 11:10AM

print('Social Networks:')
# Find all the <a> tags under the element with the CSS class 'social-network'
sn_links = soup.select('.social-network a')

num_links = len(sn_links)
for i in range(num_links):
	print('%s: %s' % (sn_links[i].get('title').rjust(8), sn_links[i].get('href')))