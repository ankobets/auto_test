import math

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from  selenium.webdriver.support import expected_conditions as EC
import  time

def calc(x):
    return str(math.log(abs(12* math.sin(x))))

browser = webdriver.Chrome()

browser.get('http://suninjuly.github.io/explicit_wait2.html')

# button = browser.find_element(By.ID, 'verify')
# button.click()
# message = browser.find_element(By.ID, 'verify_message')
#
#
# assert 'successful' in message.text
#
# time.sleep(2)

# button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable
#                                          ((By.ID, 'verify')))
# button.click()
# message = browser.find_element(By.ID, 'verify_message')
# assert 'successful' in message.text

check = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
if check:
    button = browser.find_element(By.ID, 'book')
    button.click()

ans = browser.find_element(By.ID, 'input_value').text
print(ans)
input_answer = browser.find_element(By.ID, 'answer')
input_answer.send_keys(calc(int(ans)))

button = browser.find_element(By.ID, 'solve')
button.click()

time.sleep(20)

