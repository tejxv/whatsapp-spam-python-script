from selenium import webdriver

# get chromedriver: https://chromedriver.chromium.org/downloads
# replace path with the location of chromedriver.exe 

driver = webdriver.Chrome("path\to\chromedriver.exe") 

driver.implicitly_wait(10) 
driver.get('https://web.whatsapp.com')

driver.find_element_by_css_selector("span[title='" + input("name of the victim (case sensitive): ") + "']").click()
inputString = input("your message: ")

while(True):
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(inputString)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button').click()
