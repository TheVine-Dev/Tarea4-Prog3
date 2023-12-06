from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

def test_sign_in():
    driver = webdriver.Chrome()

    driver.get("http://www.automationpractice.pl/index.php")

    femail = driver.find_element(by=By.ID, value="email_create")
    femail.send_keys("prueba@klk.do")

    createac = driver.find_element(by=By.CLASS_NAME, value="SubmitCreate")
    createac.click()

    driver.implicitly_wait(0.5)

    time.sleep(5)
    driver.quit()

#Saul Vizcaino Soto 2019-8168