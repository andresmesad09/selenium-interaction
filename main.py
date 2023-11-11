# webdriver will be in charge of the browser
from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

URL = "https://www.python.org/"

driver = webdriver.Chrome()
driver.get(URL)
upcoming_events = driver.find_elements(By.XPATH, value="//*[@id='content']/div/section/div[3]/div[2]/div/ul/li")

event_time = [event.text.split("\n")[0] for event in upcoming_events]
event_name = [event.text.split("\n")[1] for event in upcoming_events]
events = zip(event_time, event_name)

for e in events:
    print(e)
# closes a single tab
# driver.close()
# quit the entire browser
driver.quit()
