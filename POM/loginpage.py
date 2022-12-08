from selenium import webdriver
from selenium.webdriver.common.by import By
from excel import readobject

login_object = readobject.Excel()      #dictionary objects stored in L_o

driver = webdriver.Chrome(r"C:\Users\Yashaswini\PycharmProjects\pythonProject\driver\chromedriver.exe")
driver.get("https://demo.actitime.com/login.do")
driver.maximize_window()

class actitime():

    def enter_un(self):
          driver.find_element(*login_object["UN"]).send_keys("admin")

    def enter_pwd(self):
          driver.find_element(*login_object["PWD"]).send_keys("manager")

    def clogin(self):
          driver.find_element(*login_object["LIN"]).click()

l = actitime()
l.enter_un()
l.enter_pwd()
l.clogin()
















driver.quit()

