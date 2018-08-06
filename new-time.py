import requests
from bs4 import BeautifulSoup

header = {
    'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Mobile Safari/537.36'
}
url = input('Enter the url: ')
page = requests.get(url, headers = header).content

soup = BeautifulSoup(page, 'html.parser')
linkPool = soup.find_all('td', class_='tal')
for links in linkPool:
    link = links.find('h3')
    line1 = link.get_text()
    line2 = 'http://aa.dety.men/' + link.a.get('href')
    print(line1, '======', line2)
