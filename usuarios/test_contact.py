from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

def test_sign_in():
    driver = webdriver.Chrome()
    driver.get("http://www.automationpractice.pl/index.php")

    time.sleep(2)

    contact = driver.find_element(by=By.ID, value="contact-link")
    contact.click()

    select_customer = Select(driver.find_element(By.NAME, value="id_contact"))
    select_customer.select_by_value('2')

    email = driver.find_element(by=By.ID, value="email")
    email.send_keys("prueba@klk.do" + Keys.ENTER)

    order = driver.find_element(by=By.ID, value="id_order")
    order.send_keys("Blue package" + Keys.ENTER)

    messageb = driver.find_element(by=By.ID, value="message")
    messageb.send_keys("Tarea 4, prog 3, fecha 12/6/2023, 2019-8168")

    time.sleep(1.5)

    enviar = driver.find_element(by=By.ID, value="submitMessage")
    enviar.click()


    time.sleep(5)
    driver.quit()

#Saul Vizcaino Soto 2019-8168
