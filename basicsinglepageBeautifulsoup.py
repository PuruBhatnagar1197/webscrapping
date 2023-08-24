from bs4 import BeautifulSoup
import requests

url='https://subslikescript.com/movie/Titanic-120338'
response=requests.get(url)
content=response.text ### this will get the content from the website
soup=BeautifulSoup(content,'lxml')
# print(soup.prettify())### prettify to make HTML code look good
box=soup.find('article',class_='main-article')
title=box.find('h1').get_text()
trans=box.find('div',class_='full-script').get_text(strip=True,separator=' ') ### this get_text helps to clean the data and further used to get the data easily in dataframe
print(trans)
# with open(f'{title}.txt','w',encoding='utf-8') as file: ## add encoding to have same format
#     file.write(trans)





