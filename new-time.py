import requests
from bs4 import BeautifulSoup
import os
homeDir = os.getcwd()    #获取脚本当前目录

header = {
    'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Mobile Safari/537.36'
}
#打开网页（正常）
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

#解析子页面（正常）
def find_img(address):
    soup_sec = BeautifulSoup(open_url(address), 'html.parser')
    img_links = soup_sec.find_all('input', attrs={'type':'image'})
    for img_link in img_links:
        save_img(img_link.get('data-src'))
    print('Matched Successfully!')

#main（正常）
soup = BeautifulSoup(page, 'html.parser')
linkPool = soup.find_all('td', class_='tal')
i = 1    #控制跳过前几项
for links in linkPool:
    if i <= 13:
        i = i +1
        continue
    else:
        link = links.find('h3')
        title = link.get_text()
        address = 'http://cc.etet.men/' + link.a.get('href')
        print(title)
        os.mkdir(title)
        os.chdir(title)
        find_img(address)
        os.chdir(homeDir)    #自动归档
