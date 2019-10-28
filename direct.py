from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common import action_chains, keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait

url = 'https://mail.protonmail.com/create/new?language=en'

driver = webdriver.Chrome('/Users/matiselouali/Downloads/chromedriver')

driver.get(url)

wait = WebDriverWait(driver, 30) 

#driver.implicitly_wait(5)
#Element = wait.until(expected_conditions.element_to_be_clickable((By.ID, 'username')))
#wait.until(expected_conditions.visibility_of_element_located((By.NAME, 'username'))).send_keys('user')
#element  = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, xpaths['your_xpath_path'])))
time.sleep(4)
ele = driver.find_element_by_xpath("//input[@name='username']")


driver.find_element_by_name('password').send_keys('abcde')

driver.find_element_by_name('passwordc').send_keys('abcde')

ele.send_keys('abcde')
