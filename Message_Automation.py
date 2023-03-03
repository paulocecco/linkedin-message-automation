from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Open LinkedIn in a new Chrome window
driver = webdriver.Chrome()
driver.get("https://www.linkedin.com/")

# Log in to LinkedIn
email = driver.find_element_by_id("session_key")
password = driver.find_element_by_id("session_password")
email.send_keys("your_email_address")
password.send_keys("your_password")
driver.find_element_by_class_name("sign-in-form__submit-button").click()

# Wait for the page to load and navigate to the Messages page
time.sleep(5)
driver.find_element_by_class_name("msg-overlay-list-bubble--conversation").click()

# Search for the user you want to message and open their profile
search_box = driver.find_element_by_xpath("//input[@placeholder='Search']")
search_box.send_keys("User's Name")
search_box.send_keys(Keys.RETURN)
time.sleep(5)
driver.find_element_by_class_name("search-result__result-link").click()

# Click the Message button and send your message
time.sleep(5)
driver.find_element_by_class_name("pv-s-profile-actions__message").click()
time.sleep(2)
message_box = driver.find_element_by_class_name("msg-form__contenteditable")
message_box.send_keys("Your Message Here")
message_box.send_keys(Keys.RETURN)

# Close the browser
time.sleep(5)
driver.quit()
