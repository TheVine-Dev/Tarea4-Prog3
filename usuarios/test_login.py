from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_sign_in():
    driver = webdriver.Chrome()

    driver.get("http://www.automationpractice.pl/index.php")

    login = driver.find_element(by=By.CLASS_NAME, value="login")
    login.click()

    driver.implicitly_wait(0.5)

    time.sleep(5)
    driver.quit()

#Saul Vizcaino Soto 2019-8168