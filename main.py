from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service('/Users/stuartrapoport/prgming/python/automate/chromedriver')

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time


def get_chrome_driver():
	options = webdriver.ChromeOptions()
	options.add_argument('disable-infobars')
	options.add_argument('start-maximized')
	options.add_argument('disable-dev-shm-usage')
	options.add_argument('no-sandbox')
	options.add_experimental_option("excludeSwitches", ["enable-automation"])
	options.add_argument('--disable-blink-features=AutomationControlled')

	driver = webdriver.Chrome(service= service, options=options)
	driver.get("https://automated.pythonanywhere.com/login/")
	return driver

def clean_text(text):
	"""Extract only the temperature from the text"""
	output = float(text.split(": ")[1])
	return output

def main():
	driver = get_chrome_driver()
	# WebDriverWait(driver, 60).until(
    # EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/h1[1]'))
	# )
	driver.find_element(By.ID,'id_username').send_keys('automated')
	time.sleep(1)
	driver.find_element(By.ID,'id_password').send_keys('automatedautomated' + Keys.RETURN)
	time.sleep(3)
	print(driver.current_url)

	driver.find_element(By.XPATH,'/html/body/nav/div/a').click()

	time.sleep(3)
	element = driver.find_element(By.XPATH,'/html/body/div[1]/div/h1[2]')
	return clean_text(element.text)
	print(driver.current_url)



print(main())



