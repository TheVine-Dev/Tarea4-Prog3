from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_section():
    driver = webdriver.Chrome()
    driver.get("http://www.automationpractice.pl/index.php")

    botond = driver.find_element(by=By.CLASS_NAME, value="sf-with-ul")
    botond[2].click()

    time.sleep(5)

    driver.quit()

#Saul Vizcaino Soto 2019-8168