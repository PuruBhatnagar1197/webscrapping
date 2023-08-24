### codes works fine in jupyter notebook

from bs4 import BeautifulSoup
import requests

root_url='https://subslikescript.com'
website_hp=f'{root_url}/movies'
response=requests.get(website_hp)
content=response.text
soup=BeautifulSoup(content,'lxml')
box=soup.find('article',class_='main-article')
links=[]
for link in box.find_all('a',href=True):
    links.append(link['href'])
print(links)

for link_all in links:
    website_single_page=f'{root_url}/{link_all}'
    response1=requests.get(website_single_page)
    content_all=response1.text
    soup_all=BeautifulSoup(content_all,'lxml')
    box_title=soup_all.find('h1').get_text()
    trans=soup_all.find('div',class_='full-script').get_text(strip=True,separator='')
    with open(f'{box_title}.txt','w',encoding="utf-8") as file:
        print(box_title)
        file.write(trans)


