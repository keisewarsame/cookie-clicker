import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://orteil.dashnet.org/cookieclicker/")

driver.implicitly_wait(5)

try:
    language = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "langSelect-EN"))
    )
    language.click()
finally:
    pass
# driver.implicitly_wait(5)

cookie = driver.find_element(by=By.ID, value="bigCookie")
cookie_count = driver.find_element(by=By.ID, value="cookies")
items = [driver.find_element(by=By.ID, value='productPrice' + str(i)) for i in range(1, -1, -1)]

actions = ActionChains(driver)

while True:
    time.sleep(.00000001)
    actions.double_click(cookie)
    actions.perform()
    count= int(cookie_count.text.split(" ")[0])
    for item in items:
        value = int(item.text)
        if value <= count:
            upgrade_actions = ActionChains(driver)
            upgrade_actions.move_to_element(item)
            upgrade_actions.double_click()
            upgrade_actions.perform()











#NAVIGATING THROUGH THE SITE BY CLICKING

# link = driver.find_element(by=By.LINK_TEXT, value="Python Programming")
# link.click()

# try:
#     main = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.LINK_TEXT, "Beginner Python Tutorials"))
#     )
#     main.click()
#
#     main = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID, "sow-button-19310003"))
#     )
#     main.click()
#
#     #Goes back to the previous page
#     driver.back()
#     driver.back()
#     driver.back()
#     #Goes back to the next page
#     driver.forward()
#
#
# except:
#     driver.quit()






# NAVIGATE INTO THE SEARCH BAR AND CLICK ENTER; ALSO PRINTING OUT TEXT ON PAGE

# search = driver.find_element(value="s")
# search.send_keys("test")
# search.send_keys(Keys.RETURN)
#
# try:
#     main = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID, "main"))
#     )
#     articles = main.find_elements(by=By.TAG_NAME, value="article")
#     for article in articles:
#         header = article.find_element(by=By.CLASS_NAME, value="entry-summary")
#         print(header.text)
#
#
# finally:
#     driver.quit()






