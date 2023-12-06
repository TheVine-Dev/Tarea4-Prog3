from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_components():
    driver = webdriver.Chrome()

    driver.get("http://www.automationpractice.pl/index.php")

    caja = driver.find_element(by=By.ID, value="search_query_top")
    caja.send_keys("ShoEs")

    driver.implicitly_wait(0.5)

    submitb = driver.find_element(by=By.NAME, value="submit_search")

    submitb.click()


    time.sleep(5)

    driver.quit()

#Saul Vizcaino Soto 2019-8168