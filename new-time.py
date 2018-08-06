import requests
from bs4 import BeautifulSoup

header = {
    'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Mobile Safari/537.36'
}
#（正常）
def open_url(url):
    page = requests.get(url, headers = header).content
    return page

page = open_url(input('Enter the url: '))

#保存到本地（正常）
def save_img(img_addr):
    response = requests.get(img_addr, headers = header).content
    name = img_addr[-12:-4]
    with open(name + '.png', 'wb') as file:
        file.write(response)
    return 'Save Sucessfully!'

#解析子页面
def find_img(address):
	soup_sec = BeautifulSoup(open_url(address), 'html.parser')
	img_links = soup_sec.find_all('div', class_='tpc_content do_not_catch')
	for img_link in img_links:
	    img = img_link.find('input').get('src')
	    print(img) #####

#解析主页面
soup = BeautifulSoup(page, 'html.parser')
linkPool = soup.find_all('td', class_='tal')
for links in linkPool:
    link = links.find('h3')
    title = link.get_text()
    address = 'http://aa.dety.men/' + link.a.get('href')
    print(title, '======', address)
    find_img(address)
