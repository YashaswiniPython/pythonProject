from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time

@pytest.fixture()
def fixtur():
    driver = webdriver.Chrome(r"C:\Users\Yashaswini\PycharmProjects\pythonProject\driver\chromedriver.exe")
    driver.get("https://demo.actitime.com/login.do")
    driver.maximize_window()
    yield driver
    driver.quit()

def test_login(fixtur):
        fixtur.find_element("id", "usernam").send_keys("admin")
        fixtur.find_element("name", "pwd").send_keys("manager")
        fixtur.find_element(By.XPATH, '//div[text()= "Login "]').click()
        time.sleep(10)


def test_out(fixtur):
    print("Good bye")
