import time
# importing webdriver from selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
 
# Here Chrome  will be used
driver = webdriver.Chrome()
 
# URL of website
url = "https://www.hobowars.com/login/"
 
# Opening the website
driver.get(url)

time.sleep(1)
email = driver.find_element_by_id("username")
passwd = driver.find_element_by_id("password")
login = driver.find_element_by_id("login-btn")
email.send_keys('username')
passwd.send_keys('password')
login.click()

# Hospital
time.sleep(2)
hos = driver.find_element_by_link_text("Hospital")
hos.click()

if True:
    try:
        driver.find_element_by_class_name("healButton")
        heal = driver.find_element_by_class_name("healButton")
        heal.click()
    except:
        print("Skipping")

# Canbodia
time.sleep(1)
can = driver.find_element_by_link_text("Canbodia")
can.click()

# Sail
time.sleep(1)
sail = driver.find_element_by_link_text("Sail around on the river (5T)")
sail.click()
time.sleep(1)

for x in range(20):
    time.sleep(0.1)
    driver.refresh()
