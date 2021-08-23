import requests
import os
from bs4 import BeautifulSoup

url = 'https://www.miniclip.com/games/page/en/downloadable-games/#privacy-settings'
# download_url = 'https://www.miniclip.com/downloadable-games/download.php?n=3-foot-ninja'
print('Sending Request to URL')
html = requests.get(url)

print("Request Complete, Starting Download...")

soup = BeautifulSoup(html.text, 'html.parser')

links = soup.ul

i = 0
gameLinks = []
#imgLinks = []
games = {}

for link in links.find_all('a', "button positive small greedy"):
	gameLink = link.get('href')
	name = gameLink.split('=')[1]
	games[name] = "https://miniclip.com" + gameLink

# i = 0
# keys = list(games)
# for link in links.find_all('img'):
# 	games[keys[i]]['Img'] = link.get('src')
# 	i+=1

folderName = "MiniClip Games"
curDir = os.getcwd()

try:
	os.mkdir(folderName)
	print("Created games folder in current directory")
except:
    print("Found Games Folder")

os.chdir(curDir + "\\" + folderName)
count = 1
for game in games:
	print('Requesting Game (' + str(count) + '/' + '77): ' + game, end='')
	r = requests.get(games[game], 'wb')
	open(f'{game}.exe', 'wb').write(r.content)
	print(' - Done')
	count+=1
print("Downloaded Games can be found at " + os.getcwd())
