import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_login(common):
    common.find_element(By.LINK_TEXT,"Log in").click()


def test_register(common):
    common.find_element(By.LINK_TEXT,"Register").click()










