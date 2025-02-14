# Learning How to Properly Scrape Websites

# This is just an example, meaning, this may not necessarily work
# on the aforementioned site

# Let's get the author link of a website
the_response = requests.get('https://www.mii.org') # Mineral Information Institute

mii_soup = bs4.BeautifulSoup(the_response.text) # 

elems = mii_soup.select('meta[name="author"]') # ['<meta name="author" content="http://bootstraptaste.com" />']

attrs = elems[0].attrs # {'name': 'author', 'content': 'http://bootstraptaste.com'}

author_link = attrs['content'] # 'http://bootstraptaste.com'





