from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome()
URL = "https://secure-retreat-92358.herokuapp.com/"
try:
    driver.get(URL)
    first_name = driver.find_element(By.NAME, value="fName")
    first_name.send_keys("Andres")
    last_name = driver.find_element(By.NAME, value="lName")
    last_name.send_keys("Mesa")
    email_address = driver.find_element(By.NAME, value="email")
    email_address.send_keys("andresf.mesad@gmail.com")
    button = driver.find_element(By.XPATH, value="/html/body/form/button")
    button.click()
except Exception as e:
    print(f"Error: {e}")
finally:
    driver.close()
