# This pytest plugin manages dependencies of tests. It allows to mark some tests as dependent from other tests.
# These tests will then be skipped if any of the dependencies did fail or has been skipped.
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time

driver = webdriver.Chrome(r"C:\Users\Yashaswini\PycharmProjects\pythonProject\driver\chromedriver.exe")
driver.get("https://demo.actitime.com/login.do")
driver.maximize_window()

@pytest.mark.dependency()
def test_login():
    driver.find_element("id","username").send_keys("admin")
    driver.find_element("name","pwd").send_keys("manager")
    driver.find_element(By.XPATH,'//div[text()= "Login "]').click()
    time.sleep(10)


@pytest.mark.dependency(depends=["test_login"])
def test_logout():
    driver.find_element("id","logoutLink").click()
    driver.quit()




