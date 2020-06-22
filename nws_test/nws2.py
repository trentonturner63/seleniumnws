from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

path = "C:/Users/trent/Downloads/chromedriver_win32/chromedriver.exe"
# The web browser is Chrome; web driver for browser is located at path

driver = webdriver.Chrome(path)

driver.get("https://weather.gov")

# Inputs value into text box
search = driver.find_element_by_name("inputstring")
search.click()
search.send_keys("Green Bay, WI")

# Waits 10 seconds for the autocomplete suggestions to appear.  Once they appear, I press Enter.
wait = WebDriverWait(driver, 10)

wait.until(EC.presence_of_element_located(
    (By.CLASS_NAME, 'autocomplete-suggestion')))

search.send_keys(Keys.ENTER)

wait.until(EC.presence_of_element_located(
    (By.LINK_TEXT, '3 Day History')))

link = driver.find_element_by_partial_link_text("Day History")
link.click()

for i in range(2):
    driver.back()
