from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd

option=Options()
option.headless=True
option.add_argument('window-size=1920x1080')

website="https://www.audible.com/search"
path=r"C:\Users\Admin\Desktop\web scrapping\chromedriver"
driver=webdriver.Chrome(path,options=option)
driver.get(website)
driver.maximize_window()

container=driver.find_element_by_class_name("abdl-impression-container")
products=container.find_elements_by_xpath('.//li[contains(@class, "productListItem")]')

book_title=[]
book_author=[]
book_runtime=[]
for product in products:
    book_title.append(product.find_elements_by_xpath('.//h3[contains(@class,"bc-heading")]').text)
    book_author.append(product.find_elements_by_xpath('.//li[contains(@class,"authorlabel")]').text)
    book_runtime.append(product.find_elements_by_xpath('.//li[contains(@class,"runtimeLabel")]').text)

driver.quit()

book_dataframe=pd.DataFrame({"book_title":book_title,"book_author":book_author,"book_runtime":book_runtime})
book_dataframe.head()