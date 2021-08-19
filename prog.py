import requests
import time
from bs4 import BeautifulSoup

url = 'https://www.miniclip.com/games/page/en/downloadable-games/#privacy-settings'
download_url = 'https://www.miniclip.com/downloadable-games/download.php?n=3-foot-ninja'
time.sleep(5)
print('Sending Request to URL')
html = requests.get(url)
print(html.status_code)
print("Request Complete")

soup = BeautifulSoup(html.text, 'html.parser')

links = soup.ul

i = 0
gameLinks = []
imgLinks = []
games = {}

for link in links.find_all('a', "button positive small greedy"):
	gameLink = link.get('href')
	name = gameLink.split('=')[1]
	games[name] = {'link': "https://miniclip.com" + gameLink}

i = 0
keys = list(games)

for link in links.find_all('img'):
	games[keys[i]]['Img'] = link.get('src')
	i+=1

for game in games:
	print('Requesting Game: ' + game, end='')
	r = requests.get(games[game]['link'], 'wb')
	open(f'{game}.exe', 'wb').write(r.content)
	print(' - Done')
	


# print(games)

# r = requests.get(download_url, allow_redirects=True)

# print(r.headers.get('content-type'))

# game = download_url.split('=')[1]