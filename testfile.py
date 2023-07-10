# Importing required libraries

# pip install selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Setting up the webdriver
driver = webdriver.Chrome()

# Navigating to the Amazon.ca homepage
driver.get("https://www.amazon.ca")
time.sleep(3)


language_button= driver.find_element("xpath","/html/body/div[1]/header/div/div[1]/div[3]/div/a[1]")
language_button.click()
time.sleep(2)

french_button= driver.find_element("xpath","/html/body/div[1]/div[2]/div/form/div[1]/div[1]/div[3]/div/label/i")
french_button.click()
time.sleep(2)

save_changes= driver.find_element("xpath","/html/body/div[1]/div[2]/div/span[2]/span/input")
save_changes.click()
time.sleep(2)

# Finding the search bar and entering text
search_bar = driver.find_element("id","twotabsearchtextbox")
search_bar.send_keys("ipad")

# Submitting the search query
search_bar.send_keys(Keys.RETURN)

# Waiting for the search results page to load
time.sleep(5)

# Verifying that the search results page has loaded
assert "ipad" in driver.title

# Selecting a ipad from the search results
ipad_link = driver.find_element("xpath","/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[10]/div/div/div/div/div[1]/span/a/div/img")
ipad_link.click()

# Waiting for the laptop details page to load
time.sleep(5)

# Adding the laptop to the cart
buy_now_button = driver.find_element("id","buy-now-button")
buy_now_button.click()

# Waiting for the cart to update
time.sleep(5)

# Closing the webdriver
driver.close()