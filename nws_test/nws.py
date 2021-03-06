from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

path = "C:/Users/trent/Downloads/chromedriver_win32/chromedriver.exe"
# The web browser is Chrome; web driver for browser is located at path
# Webdriver is web automation framework

driver = webdriver.Chrome(path)

driver.get("https://weather.gov")
print(driver.title)

search = driver.find_element_by_name("inputstring")
search.click()  # Important so that you don't add to an already existing text
search.send_keys("Green Bay, WI")
search.send_keys(Keys.RETURN)

# Wait a maximum of 10 seconds until expected conditions are met
# Make sure element exists before clicking it

wait = WebDriverWait(driver, 10)

wait.until(EC.presence_of_element_located(
    (By.CLASS_NAME, 'autocomplete-suggestion')))


for elm in driver.find_elements_by_css_selector(".autocomplete-suggestion"):
    print(elm.text)

driver.quit()

# documentation: https://selenium-python.readthedocs.io/
# Tech with Tim's videos really helped me with this project.  Here's his channel:
# https://www.youtube.com/channel/UC4JX40jDee_tINbkjycV4Sg
