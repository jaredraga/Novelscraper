#Webnovel Chapter Automation

# Add pauses for more human-like nature and for the sake of the computer
# Record the saved
import pyautogui, time, random

slowTypingSpeedToLookMoreHuman = random.uniform(0.1, 0.3)
novelName = 'The Strongest System'
currentChapter = 635
finalChapter = 662

while currentChapter <= finalChapter:
	# EASY PART
	# Go to search bar, enter and open firefox
	pyautogui.hotkey('alt', 's')
	time.sleep(1)
	pyautogui.typewrite('firefox')
	pyautogui.press('enter')

	# Maximize firefox window
	time.sleep(3)
	pyautogui.hotkey('winleft', 'up')

	time.sleep(2)

	# Click anywhere along the search bar
	randomPositionAlongBrowserSearchBar = random.randint(85, 669)
	pyautogui.moveTo(randomPositionAlongBrowserSearchBar, 108, 3, pyautogui.easeOutQuad)
	pyautogui.click(randomPositionAlongBrowserSearchBar, 108)

	# Clear search bar contents
	pyautogui.hotkey('ctrl', 'a')
	pyautogui.press('backspace')

	pyautogui.typewrite('reddit ' + novelName + ' ' + str(currentChapter), interval=slowTypingSpeedToLookMoreHuman)
	pyautogui.press('enter')

	# Click the first search result
	time.sleep(15)
	randomPositionAlongFirstGoogleResult = random.randint(166, 600)
	pyautogui.moveTo(randomPositionAlongFirstGoogleResult, 350, 2, pyautogui.easeOutQuad)
	pyautogui.click(randomPositionAlongFirstGoogleResult, 350)

	# Click the link to Private Bin from reddit 
	time.sleep(20)
	randomPositionAlongFirstRedditResult = random.randint(250, 405)
	pyautogui.moveTo(randomPositionAlongFirstRedditResult, 433, 2, pyautogui.easeOutQuad)
	pyautogui.click(randomPositionAlongFirstRedditResult, 433)

	# Copy all the contents from Private Bin
	time.sleep(20)
	randomPositionAlongRawTextButton = random.randint(243, 319)
	pyautogui.moveTo(randomPositionAlongRawTextButton, 188, .3, pyautogui.easeOutQuad)
	pyautogui.click(randomPositionAlongRawTextButton, 188)
	time.sleep(0.2)
	pyautogui.hotkey('ctrl', 'a')
	time.sleep(1)
	pyautogui.hotkey('ctrl', 'c')
	time.sleep(3)

	# Open Text Editor and paste the Chapter 
	pyautogui.hotkey('alt', 'tab')
	time.sleep(1)
	pyautogui.hotkey('alt', 's')
	time.sleep(1)
	pyautogui.typewrite('text editor')
	pyautogui.press('enter')
	time.sleep(10)
	pyautogui.hotkey('ctrl', 'v')
	time.sleep(4)

	# Save Chapter; Title and Chapter Number as a .txt file
	pyautogui.hotkey('ctrl', 's')
	time.sleep(3)
	randomPositionAlongSaveFileDirectory = random.randint(150, 345)
	pyautogui.moveTo(520, randomPositionAlongSaveFileDirectory, .3, pyautogui.easeOutQuad)
	pyautogui.click(520, randomPositionAlongSaveFileDirectory)
	# Go to the Webnovels' Directory
	time.sleep(1)
	pyautogui.typewrite('W3BN0V3L')
	pyautogui.press('down')
	pyautogui.press('enter')
	time.sleep(2)
	# Go to the Novel's Directory
	pyautogui.press('down')
	pyautogui.press('enter')
	time.sleep(2)

	# Name the Chapter and close the Text Editor window
	randomPositionAlongFileNamingBar = random.randint(600, 810)
	pyautogui.moveTo(randomPositionAlongFileNamingBar, 50, .3, pyautogui.easeOutQuad)
	pyautogui.click(randomPositionAlongFileNamingBar, 50)
	pyautogui.hotkey('ctrl', 'a')
	pyautogui.press('backspace')
	pyautogui.typewrite(novelName + ' - Chapter ' + str(currentChapter) + '.txt')
	time.sleep(1)
	pyautogui.press('enter')
	time.sleep(2)
	pyautogui.hotkey('winleft', 'up')
	time.sleep(2)
	pyautogui.hotkey('alt', 'f4')

	currentChapter += 1


# Title Configuration
# Find the word 'Chapter' within the first 6 lines;
# If 'Chapter' is there:
#	* Type the title of the Novel first; then add the line afterwards
#	(The Strongest System - Chapter 629: To Think That It Would Be This Small!)
#If 'Chapter' is not there:
#	* Type the title of the Novel then the Chapter number
#	(The Strongest System - Chapter 630)
	
def placeholder():
		time.sleep(1)
		pyautogui.typewrite('https://www.google.com', interval=slowTypingSpeedToLookMoreHuman)
		pyautogui.press('enter')

		# HARD PART
		# Searching for chapter on reddit Qidian Underground
		time.sleep(2)
		randomPositionAlongGoogleSearchBar = random.randint(399, 981)
		pyautogui.moveTo(randomPositionAlongGoogleSearchBar, 500, 2, pyautogui.easeOutQuad)
		pyautogui.click(randomPositionAlongGoogleSearchBar, 500)

