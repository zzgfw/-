import requests
from bs4 import BeautifulSoup
import os
import re
homeDir = os.getcwd()    #获取脚本当前目录

header = {
    'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Mobile Safari/537.36'
}
#打开网页（正常）
def open_url(url):
    page = requests.get(url, headers = header).content
    return page

#保存到本地（正常）
def save_img(img_addr):
    response = requests.get(img_addr, headers = header).content
    name = img_addr[-12:]
    name = name.replace('/', '_')
    with open(name, 'wb') as file:
        file.write(response)

#解析子页面（正常）
def find_img(address):
    soup_sec = BeautifulSoup(open_url(address), 'html.parser')
    img_links = soup_sec.find_all('input', attrs={'type':'image'})
    for img_link in img_links:
        save_img(img_link.get('data-src'))
    print('Matched Successfully!\n')

#main（正常）
print('<Searching&Downloading...>\n\n ***Don`t Kill This Process***')
print()
for n in range(100, 0, -1):
    n = str(n)
    page = open_url('http://ab.cbcb.us/thread0806.php?fid=8&search=&page=' + n)
    
    soup = BeautifulSoup(page, 'html.parser')
    linkPool = soup.find_all('a', text=re.compile(r'^小鳥醬'))
    
    for links in linkPool:
        title = links.get_text()
        address = 'http://ab.cbcb.us/' + links.get('href')
        print('>>>'+title)
        os.mkdir(title)
        os.chdir(title)
        find_img(address)
        os.chdir(homeDir)    #自动归档

print()
print('-Mission Completed-')
input('Press Enter to exit...')
