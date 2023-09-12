from selenium import webdriver

web = "https://twitter.com/"
path=r"C:\Users\Admin\Desktop\web scrapping\chromedriver"

driver=webdriver.Chrome(path)
driver.get(web)
driver.maximize_window()

login=driver.find_element_by_xpath("//a[@href='/login']")
login.click()

time.sleep(2)
username=driver.find_element_by_xpath('//input[@name="text"]')
username.send_keys("email")

### click on next button
next_b=driver.find_element_by_xpath("//div[@role='button']//span[text()='Next']")
next_b.click()
### finding password area
password=driver.find_element_by_xpath('//input[@name="password"]')
username.send_keys("password")

## loging in
login=driver.find_element_by_xpath("//div[@role='button']//span[text()='Log in']")
login.click()


