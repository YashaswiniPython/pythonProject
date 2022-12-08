#conftest is a speacial file used to share fixtutres among the testcases.
# if there is multiple modules and need to shareed the same fixtures
# among them we make use of conftest.

import pytest
from selenium import webdriver

@pytest.fixture()
def common():
    driver = webdriver.Chrome(r"C:\Users\Yashaswini\PycharmProjects\pythonProject\driver\chromedriver.exe")
    driver.get("https://demowebshop.tricentis.com/login")
    driver.maximize_window()
    yield driver
    print(driver.title)
    driver.quit()