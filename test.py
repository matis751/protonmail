from selenium import webdriver
import time

url = 'https://protonmail.com/'

driver = webdriver.Chrome('/Users/matiselouali/Downloads/chromedriver')
driver.get(url)

time.sleep(1)

driver.find_element_by_xpath("//a[@href='signup']").click()

time.sleep(1)

driver.find_element_by_class_name('panel-heading').click()

time.sleep(1)

driver.find_element_by_id('freePlan').click()

usernameXpath = '//*[@id="username"]/html/body/div/div/div/div/input'

username = WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(usernameXpath))

actions = ActionChains(driver)

actions.move_to_element(username).send_keys("abcs").perform()

