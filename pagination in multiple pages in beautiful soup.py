### codes works fine in jupyter notebook

from bs4 import BeautifulSoup
import requests

root_url='https://subslikescript.com'
website_hp=f'{root_url}/movies_letter-A'
response=requests.get(website_hp)
content=response.text
soup=BeautifulSoup(content,'lxml')
### locate the box where page number is written
box_page=soup.find('ul', class_='pagination')
pages=box_page.find_all('li', class_='page-item')
last_page=pages[-2].text ## this is the last page number on the website

for page in range(1,int(last_page)+1):
    result = requests.get(f'{website_hp}?page={page}') ## structuring according to page name
    content=result.text
    soup=BeautifulSoup(content, 'lxml')
    box=soup.find('article',class_='main-article')
    links=[]
    for link in box.find_all('a',href=True):
        links.append(link['href'])

    for link_all in links:
        try:
            website_single_page=f'{root_url}/{link_all}'
            response1=requests.get(website_single_page)
            content_all=response1.text
            soup_all=BeautifulSoup(content_all,'lxml')
            box_title=soup_all.find('h1').get_text()
            trans=soup_all.find('div',class_='full-script').get_text(strip=True,separator='')
            with open(f'{box_title}.txt','w',encoding="utf-8") as file:
                print(box_title)
                file.write(trans)
        except:
            print("this link doesn't work  ",link_all)


