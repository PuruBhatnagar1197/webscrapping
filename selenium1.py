from selenium import webdriver
import pandas as pd
website='https://www.adamchoi.co.uk/overs/detailed'
path=r"C:\Users\Admin\Desktop\web scrapping\chromedriver"
driver=webdriver.Chrome(path)
driver.get(website)
all_matched_button=driver.find_element_by_xpath('//label[@analytics-event="All matches"]') ## this is to locate the button
all_matched_button.click() ### this is to click on the button
### now we will look into how to extract content of a table using selenium
table_row=driver.find_elements_by_tag_name('tr') # this will be a list  containing sleeium elements onces you write .text in front of that object you will get what exactly si there in that object
date=[]
home_team=[]
score=[]
away_team=[]
for table_row_cont in table_row:
    ## in python the indexes stat from 0 but in table elements it starts with 1
    date.append(table_row_cont.find_element_by_xpath('./td[1]').text) ## since table_row_cont contains rows context just wants to extract the lower value of tr i.e. td
    home=table_row_cont.find_element_by_xpath('./td[2]').text
    print(home)
    home_team.append(home)  ## since table_row_cont contains rows context just wants to extract the lower value of tr i.e. td
    score.append(table_row_cont.find_element_by_xpath('./td[3]').text)  ## since table_row_cont contains rows context just wants to extract the lower value of tr i.e. td
    away_team.append(table_row_cont.find_element_by_xpath('./td[4]').text)  ## since table_row_cont contains rows context just wants to extract the lower value of tr i.e. td

driver.quit()

df=pd.DataFrame({'date':date,'home_team':home_team,'score':score,'away_team':away_team})
df.to_csv('football_allscore.csv',index=False)










