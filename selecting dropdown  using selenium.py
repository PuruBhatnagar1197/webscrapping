# to select the dropdown using selenium lets do it in this manner
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import pandas as pd

website='https://www.adamchoi.co.uk/overs/detailed'
path=r"C:\Users\Admin\Desktop\web scrapping\chromedriver"
driver=webdriver.Chrome(path)
driver.get(website)
all_matches=driver.find_element_by_xpath('//label[@analytics-event="All matches"]')

all_matches.click()

dropdown=Select(driver.find_element_by_id('country'))
dropdown.select_by_visible_text('Spain')

time.sleep(3)

tabel_cont=driver.find_elements_by_tag_name('tr')
date=[]
home_team=[]
score=[]
away_team=[]
for table_row_cont in tabel_cont:
    ## in python the indexes stat from 0 but in table elements it starts with 1
    date.append(table_row_cont.find_element_by_xpath('./td[1]').text) ## since table_row_cont contains rows context just wants to extract the lower value of tr i.e. td
    home=table_row_cont.find_element_by_xpath('./td[2]').text
    print(home)
    home_team.append(home)  ## since table_row_cont contains rows context just wants to extract the lower value of tr i.e. td
    score.append(table_row_cont.find_element_by_xpath('./td[3]').text)  ## since table_row_cont contains rows context just wants to extract the lower value of tr i.e. td
    away_team.append(table_row_cont.find_element_by_xpath('./td[4]').text)  ## since table_row_cont contains rows context just wants to extract the lower value of tr i.e. td

driver.quit()

df=pd.DataFrame({'date':date,'home_team':home_team,'score':score,'away_team':away_team})
df.to_csv('football_allscore_spain.csv',index=False)

