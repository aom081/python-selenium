from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time


# Initialize the Chrome WebDriver
s = Service('D:\chromedriver.exe')
driver = webdriver.Chrome(service=s)

driver.get("https://www.google.com/")
driver.set_window_size(1072,816)
driver.find_element(By.ID, "APjFqb").send_keys("5+5")
driver.find_element(By.CSS_SELECTOR, "center:nth-child(1) > .gNO89b").click()
assert driver.find_element(By.ID, "cwos").text == "10"
assert driver.title == "5+5 - ค้นหาด้วย Google"
# Wait for the search results to load
time.sleep(5)

# Print the title of the current page
print(driver.title)

# Close the browser
driver.quit()