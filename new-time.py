import requests
from bs4 import BeautifulSoup

header = {
    'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Mobile Safari/537.36'
}
url = input('Enter the url: ')
page = requests.get(url, headers = header).content

#保存到本地
def save_img(img_addr):
    response = requests.get(img_addr, headers = header).content
    name = img_addr[-12:-4]
    with open(name + '.png', 'wb') as file:
        file.write(response)

#解析主页面
soup = BeautifulSoup(page, 'html.parser')
linkPool = soup.find_all('td', class_='tal')
for links in linkPool:
    link = links.find('h3')
    title = link.get_text()
    address = 'http://aa.dety.men/' + link.a.get('href')
    print(title, '======', address)
