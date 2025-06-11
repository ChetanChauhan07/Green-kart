#******* Importing essential components for automation from Selenium *******

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#*******Invoking the Chrome Browser*******
driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()


#******* Proceed to the site *******

driver.get("https://rahulshettyacademy.com/seleniumPractise/")
driver.find_element(By.CSS_SELECTOR,"input[placeholder='Search for Vegetables and Fruits']").send_keys("ber")
time.sleep(2)

expectedList =['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
   

results = driver.find_elements(By.XPATH,"//div[@class='products']/div")
count =len(results)
time.sleep(5) 
veg=[]
assert count>0
for result in results:
    veg.append(result.find_element(By.XPATH,"h4").text)
    result.find_element(By.XPATH,"div/button").click()
    
print(veg)
# time.sleep(5) 

assert expectedList==veg

driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()
# time.sleep(2)
driver.find_element(By.CSS_SELECTOR,"div[class='cart-preview active'] button[type='button']").click()
# time.sleep(2)

#*******SUM Validation

prices = driver.find_elements(By.XPATH, '//td[5]/p[@class="amount"]')
sum =0

for price in prices:
    sum=sum + int(price.text)

print(sum)

totalAmt = int(driver.find_element(By.CSS_SELECTOR,".totAmt").text)
assert sum==totalAmt

driver.find_element(By.CSS_SELECTOR,"input[placeholder='Enter promo code']").send_keys("rahulshettyacademy")


driver.find_element(By.CSS_SELECTOR,".promoBtn").click()
time.sleep(10)

discount = float(driver.find_element(By.CSS_SELECTOR,".discountAmt").text)
print(discount)
assert discount < totalAmt

driver.find_element(By.XPATH,"//button[normalize-space()='Place Order']").click()
#time.sleep(2)
driver.find_element(By.CSS_SELECTOR,"div[class='wrapperTwo'] div select").send_keys("In")
#time.sleep(5)
driver.find_element(By.CSS_SELECTOR,"input[type='checkbox']").click()
#time.sleep(2)
driver.find_element(By.CSS_SELECTOR,"div[class='wrapperTwo'] button").click()
#time.sleep(2)
driver.get_screenshot_as_file("paras.png")


