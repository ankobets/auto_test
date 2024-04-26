import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

# link = 'http://suninjuly.github.io/find_link_text'
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#     name = browser.find_element(By.NAME, 'first_name')
#     name.send_keys("Ivan")
#     surname = browser.find_element(By.NAME, 'last_name')
#     surname.send_keys('Ivanov')
#     city = browser.find_element(By.CLASS_NAME, 'city')
#     city.send_keys('Moscow')
#     country = browser.find_element(By.ID, 'country')
#     country.send_keys('Russia')
#     button = browser.find_element(By.ID, 'submit_button')
#     button.click()
#
# finally:
#     time.sleep(30)
#     browser.quit()


# source = 'http://suninjuly.github.io/find_link_text'
# find_link = str(math.ceil(math.pow(math.pi, math.e)*10000))
# print(find_link)
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(source)
#     link = browser.find_element(By.LINK_TEXT, find_link)
#     link.click()
#     name = browser.find_element(By.NAME, 'first_name')
#     name.send_keys("Ivan")
#     surname = browser.find_element(By.NAME, 'last_name')
#     surname.send_keys('Ivanov')
#     city = browser.find_element(By.CLASS_NAME, 'city')
#     city.send_keys('Moscow')
#     country = browser.find_element(By.ID, 'country')
#     country.send_keys('Russia')
#     button = browser.find_element(By.CLASS_NAME, 'btn')
#     button.click()
#
# finally:
#     time.sleep(30)
#     browser.quit()

# source = 'http://suninjuly.github.io/huge_form.html'
#
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(source)
#     form_elements = browser.find_elements(By.TAG_NAME, 'input')
#     for element in form_elements:
#         element.send_keys("Hey")
#     button = browser.find_element(By.CLASS_NAME, 'btn')
#     button.click()
#
# finally:
#     time.sleep(30)
#     browser.quit()


# link = 'http://suninjuly.github.io/find_xpath_form'

# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#     name = browser.find_element(By.NAME, 'first_name')
#     name.send_keys("Ivan")
#     surname = browser.find_element(By.NAME, 'last_name')
#     surname.send_keys('Ivanov')
#     city = browser.find_element(By.CLASS_NAME, 'city')
#     city.send_keys('Moscow')
#     country = browser.find_element(By.ID, 'country')
#     country.send_keys('Russia')
#     button = browser.find_element(By.XPATH, '//button[@type="submit"]')
#     button.click()
#
# finally:
#     time.sleep(30)
#     browser.quit()

# link = 'http://suninjuly.github.io/registration1.html'
#
# labels = []
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#     labels = browser.find_elements(By.CSS_SELECTOR, 'input[required]')
#     for label in labels:
#         print(label.text)
#         label.send_keys("aaaa")
#     button = browser.find_element(By.CLASS_NAME, 'btn')
#     button.click()
#
#     welcome_el = browser.find_element(By.TAG_NAME, 'h1')
#     welcome_text = welcome_el.text
#
#     assert "Congratulations! You have successfully registered!" == welcome_text
#
# finally:
#     time.sleep(15)
#     browser.quit()

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = 'http://suninjuly.github.io/get_attribute.html'
try:
    browser = webdriver.Chrome()
    browser.get(link)
    number = browser.find_element(By.TAG_NAME, 'img')

    input_answer = browser.find_element(By.ID, 'answer')
    print(input_answer)
    input_answer.send_keys(calc(number.get_attribute('valuex')))
    input_check = browser.find_element(By.CSS_SELECTOR, 'input[type="checkbox"]')
    input_check.click()
    input_radio = browser.find_element(By.CSS_SELECTOR, '[value="robots"]')
    input_radio.click()
    button = browser.find_element(By.XPATH, '//button[@type="submit"]')
    button.click()

finally:
    time.sleep(30)
    browser.quit()


