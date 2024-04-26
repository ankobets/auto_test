import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
    return str( math.log(abs(12* math.sin(x))))



# link = 'http://suninjuly.github.io/alert_accept.html'
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#     button = browser.find_element(By.TAG_NAME, 'button')
#     button.click()
#
#     browser.switch_to.alert.accept()
#
#     input_answer = browser.find_element(By.TAG_NAME, 'input')
#     input_answer.send_keys(calc(float(browser.find_element(By.ID, 'input_value').text)))
#
#     button = browser.find_element(By.TAG_NAME, 'button')
#     button.click()
#
# finally:
#     time.sleep(30)
#     browser.quit()


link = 'http://suninjuly.github.io/redirect_accept.html'
try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.CLASS_NAME, 'btn')
    time.sleep(1)
    button.click()

    new_window = browser.window_handles[2]
    browser.switch_to.window(new_window)


    ans = browser.find_element(By.ID, 'input_value').text
    print(ans)
    input_answer = browser.find_element(By.ID, 'answer')
    input_answer.send_keys(calc(int(ans)))

    button = browser.find_element(By.TAG_NAME, 'button')
    button.click()

finally:
    time.sleep(30)
    browser.quit()

