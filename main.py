import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import username, password

# Enter the message you want to send here
message_template = "Hi {name}, I hope this message finds you well."

# Set up the webdriver
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

# Log in to LinkedIn
driver.get("https://www.linkedin.com/login")
username_field = driver.find_element_by_name("session_key")
username_field.send_keys(username)
password_field = driver.find_element_by_name("session_password")
password_field.send_keys(password)
password_field.submit()

# Search for the user you want to send a message to
search_field = driver.find_element_by_xpath('//input[@aria-label="Search"]')
search_field.send_keys("John Doe")
search_field.send_keys(Keys.RETURN)

# Navigate to the user's profile
user_link = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//a[@data-control-name="search_srp_result"]')))
user_link.click()

# Send a message to the user
message_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//span[text()="Message"]')))
message_button.click()
message_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//textarea[@aria-label="Write a message…"]')))
message = message_template.format(name="John")
message_box.send_keys(message)
message_box.send_keys(Keys.RETURN)

# Close the webdriver
driver.quit()
