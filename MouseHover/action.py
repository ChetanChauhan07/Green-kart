from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

chrome_options= webdriver.ChromeOptions()
chrome_options.add_argument("headless")

driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(5)
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.find_element(By.XPATH,"//a[contains(text(),'Free Access to')]").click()

win = driver.window_handles
driver.switch_to.window(win[1])
time.sleep(2)

mail = (driver.find_element(By.CSS_SELECTOR,"a[href='mailto:mentor@rahulshettyacademy.com']").text)
driver.switch_to.window(win[0])
driver.find_element(By.XPATH,"//input[@id='username']").send_keys(mail)
driver.find_element(By.CSS_SELECTOR,"#password").send_keys("learning")
driver.find_element(By.CSS_SELECTOR,"#terms").click()
driver.find_element(By.CSS_SELECTOR,"#signInBtn").click()
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger")))
print(driver.find_element(By.CSS_SELECTOR, ".alert-danger").text)

time.sleep(2)
