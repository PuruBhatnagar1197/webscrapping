from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd
import time

option=Options()
option.headless=False
# option.add_argument('window-size=1920x1080')

website="https://www.audible.com/search"
path=r"C:\Users\Admin\Desktop\web scrapping\chromedriver"
driver=webdriver.Chrome(path,options=option)
driver.get(website)
driver.maximize_window()

### pagination
pagination=driver.find_element_by_xpath('//ul[contains(@class,"pagingElements")]')
pages=pagination.find_elements_by_tag_name('li')

last_page=int(pages[-2].text)
current_page=1
book_title=[]
book_author=[]
book_runtime=[]
while current_page<=last_page:
    time.sleep(3)
    container = driver.find_element_by_class_name("adbl-impression-container ")
    products = container.find_elements_by_xpath('.//li[contains(@class, "productListItem")]')
    for product in products:
        book_title.append(product.find_element_by_xpath('.//h3[contains(@class,"bc-heading")]').text)
        book_author.append(product.find_element_by_xpath('.//li[contains(@class,"authorLabel")]').text)
        book_runtime.append(product.find_element_by_xpath('.//li[contains(@class,"runtimeLabel")]').text)

    current_page+=1
    try:
        next_page = driver.find_element_by_xpath('//span[contains(@class,"nextButton")]') ## this is for moving to next page
        next_page.click()
    except:
        pass
driver.quit()

book_dataframe=pd.DataFrame({"book_title":book_title,"book_author":book_author,"book_runtime":book_runtime})
book_dataframe.to_csv("book_data.csv",index=False)