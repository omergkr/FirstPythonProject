# open browser
# go to webpage

# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://practicetestautomation.com/practice-test-login/")

driver.find_element(By.ID, "username").send_keys("student")
driver.find_element(By.XPATH, "//input[@id='password']").send_keys("Password123")
driver.find_element(By.CSS_SELECTOR, "button#submit").click()

current_url = driver.current_url
assert current_url == "https://practicetestautomation.com/logged-in-successfully/"

actual_test = driver.find_element(By.TAG_NAME, "h1").text
assert actual_test == "Logged In Successfully"

assert driver.find_element(By.LINK_TEXT, "Log out").is_displayed()

