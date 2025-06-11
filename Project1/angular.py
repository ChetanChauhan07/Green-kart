import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element(By.XPATH,"//a[normalize-space()='Shop']").click()

# driver.find_element(By.CSS_SELECTOR,"body > app-root:nth-child(2) > app-navbar:nth-child(1) > div:nth-child(1) > nav:nth-child(1) > ul:nth-child(2) > li:nth-child(2) > a:nth-child(1)").click()
pro = driver.find_elements(By.XPATH,"//div[@class='card h-100']")
for r in pro:
    y=(r.find_element(By.XPATH,"div/h4/a").text)
    if y=="Blackberry":
        r.find_element(By.XPATH,"div/button").click()


#driver.find_element(By.CSS_SELECTOR,"body > app-root:nth-child(2) > app-shop:nth-child(3) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > app-card-list:nth-child(2) > app-card:nth-child(1) > div:nth-child(1) > div:nth-child(3) > button:nth-child(1)").click()
# driver.find_element(By.CSS_SELECTOR,".nav-link.btn.btn-primary").click()
# driver.find_element(By.CSS_SELECTOR,"button[class='btn btn-success']").click()
# driver.find_element(By.CSS_SELECTOR,"#country").send_keys("India")

# wait=WebDriverWait(driver,7)
# z=driver.find_element(By.XPATH,"//a[normalize-space()='India']")
# wait.until(EC.visibility_of_element_located(z))

# driver.find_element(By.CSS_SELECTOR,"label[for='checkbox2']").click()
# driver.find_element(By.CSS_SELECTOR,"input[value='Purchase']").click()
# print(driver.find_element(By.CSS_SELECTOR,".alert.alert-success.alert-dismissible").text)
# driver.get_screenshot_as_file("Order.png")

# driver.find_element(By.XPATH,"//a[normalize-space()='ProtoCommerce Home']").click()


"""driver.find_element(By.CSS_SELECTOR,"div[class='form-group'] input[name='name']").send_keys("Chauhan") 
driver.find_element(By.CSS_SELECTOR,"input[name='email']").send_keys("xyz@gmail.com")
driver.find_element(By.CSS_SELECTOR,"#exampleInputPassword1").send_keys("xyz1234")
driver.find_element(By.CSS_SELECTOR, "#exampleCheck1").click()
driver.find_element(By.CSS_SELECTOR,"#exampleFormControlSelect1").send_keys("Male")
driver.find_element(By.CSS_SELECTOR,'#inlineRadio1').click()
driver.find_element(By.CSS_SELECTOR,"input[name='bday']").send_keys("03/17/2003")
driver.find_element(By.CSS_SELECTOR,"input[value='Submit']").click()

print(driver.find_element(By.CSS_SELECTOR,".alert.alert-success.alert-dismissible").text)
"""

time.sleep(3)