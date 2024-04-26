import time
import math
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# link = 'http://suninjuly.github.io/selects1.html'
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#     num1 = browser.find_element(By.ID, 'num1').text
#     num2 = browser.find_element(By.ID, 'num2').text
#     sum_nums = browser.find_elements(By.TAG_NAME, 'option')
#     del sum_nums[0]
#
#     for num in sum_nums:
#         if int(num.text) == (int(num1) + int(num2)):
#             num.click()
#
#     browser.find_element(By.TAG_NAME, 'button').click()
#
# finally:
#     time.sleep(15)
#     browser.quit()

# link = 'http://suninjuly.github.io/selects2.html'
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#     num1 = int(browser.find_element(By.ID, 'num1').text)
#     num2 = int(browser.find_element(By.ID, 'num2').text)
#     sum_nums = Select(browser.find_element(By.TAG_NAME, 'select'))
#     sum_nums.select_by_visible_text(str(num1+num2))
#
#     browser.find_element(By.TAG_NAME, 'button').click()
#
# finally:
#     time.sleep(15)
#     browser.quit()

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

# link = 'http://suninjuly.github.io/file_input.html'
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#     number = browser.find_element(By.ID, 'input_value').text
#
#     input_answer = browser.find_element(By.ID, 'answer')
#     browser.execute_script('return arguments[0].scrollIntoView(true);', input_answer)
#     input_answer.send_keys(calc(number))
#     input_check = browser.find_element(By.CSS_SELECTOR, 'input[type="checkbox"]')
#     input_check.click()
#     input_radio = browser.find_element(By.CSS_SELECTOR, '[value="robots"]')
#     input_radio.click()
#     button = browser.find_element(By.XPATH, '//button[@type="submit"]')
#     button.click()
#
# finally:
#     time.sleep(30)
#     browser.quit()


link = 'http://suninjuly.github.io/file_input.html'

try:
    with open('file.txt', 'w+') as file:
        file.write('hey')

    browser = webdriver.Chrome()
    browser.get(link)
    labels = browser.find_elements(By.CSS_SELECTOR, 'input[type="text"]')
    for label in labels:
        label.send_keys("aaaa")

    cur_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(cur_dir, 'file.txt')
    file_but = browser.find_element(By.CSS_SELECTOR, '[type="file"]')
    file_but.send_keys(file_path)
    button = browser.find_element(By.XPATH, '//button[@type="submit"]')
    button.click()

finally:
    file.close()
    time.sleep(30)
    browser.quit()