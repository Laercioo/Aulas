from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import keys

browser = Firefox()

link = 'https://google.com'

browser.get(link)

input_area = browser.find_element(By.NAME, "q")

input_area.send_keys("Instituto Joga Junto")
input_area.send_keys(keys.ENTER)
from time import sleep; sleep(3)
result_search= browser.find_element(By.TAG_NAME, 'h3')
print(result_search)


check = False 

while check == False:

    for result in result_search:
        if result.text == "Instituto Joga Junto" and result.text is not None:
            result.click()
            print("AEEE")
            check = True
            
            
