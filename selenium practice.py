# import os
#
from selenium import webdriver
import os
import time

# class RunChromeTestsWindows():
#     def test(self):
#         driverlocation = "./driver/chromedriver.exe"
#         os.environ["webdriver.chrome.driver"] = driverlocation
#         driver = webdriver.Chrome(driverlocation)
#         driver.get("https://www.gmail.com")
# chromeTest = RunChromeTestsWindows()
# chromeTest.test()
# import time
# from selenium import webdriver
# class findelements():
#     def test(self):
#         driver = webdriver.Chrome("./driver/chromedriver.exe")
#         driver.get("https://www.flipkart.com/")
#         driver.maximize_window()
#
#         findbyid = driver.find_element('id','identifierId')
#         # findbyid.send_keys("yashaswinicr@gmail.com")
#         if findbyid is not None:
#             print("Success")
#             time.sleep(7)
#         exit()
# a = findelements()
# a.test()
        # findbyclass = driver.find_element('class name','TquXA')
        # findbyclass.click()
        # if findbyclass is not None:
        #     print("class Success")
        #     time.sleep(7)
        # exit()

        # findbyname = driver.find_element('name','q')
        # findbyname.send_keys("mobiles")
        #
        # if findbyname is not None:
        #     print("success")
        #     time.sleep(5)
        # exit()

        # findbyxpath = driver.find_element('xpath',"//input[@class = '_3704LK']")
        # findbyxpath.send_keys("kitchen items")
        # if findbyxpath is not None:
        #         print("success")
        #         time.sleep(7)
        # exit()

        # findbylinktext = driver.find_element('link text','Login')
        # if findbylinktext is not None:
        #     print("success")
        #     time.sleep(7)
        # exit()

        # findbypartial = driver.find_element('partial link text','Become a')
        # # findbypartial.click()
        # if findbypartial is not None:
        #     print("Super")
        #     time.sleep(7)
        # exit()

        # findbytag = driver.find_element('tag name','a')
        # if findbytag is not None:
        #     print("success")
        #     time.sleep(5)
        # exit()



# f = findelements()
# f.test()

# By Method
import time

# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# class Byelements():
#     def test(self):
#         driver = webdriver.Chrome("./driver/chromedriver.exe")
#         driver.get("https://www.flipkart.com/")
#         driver.maximize_window()
#
#         findByid = driver.find_element(By.CLASS_NAME,'_3704LK')
#
#         if findByid is not None:
#             print("Success")
#             time.sleep(5)
#         exit()
# f = Byelements()
# f.test()

# findby elements

# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# class listelements():
#     def test(self):
#         driver = webdriver.Chrome("./driver/chromedriver.exe")
#         driver.get("https://www.flipkart.com/")
#         driver.maximize_window()
#
#
#         listofele = driver.find_elements(By.TAG_NAME,'a')
#         length = len(listofele)
#         if listofele is not None:
#             print("length is :" +str(length))
#             time.sleep(5)
#         exit()
# f = listelements()
# f.test()

# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# class cssexample():
#     def test(self):
#         driver = webdriver.Chrome("./driver/chromedriver.exe")
#         driver.get("https://www.flipkart.com/")
#         driver.maximize_window()
#
#         # bycss = driver.find_element('css selector','._3704LK')
#         bycss = driver.find_elements(By.CSS_SELECTOR,'._3704LK')
#         if bycss is not None:
#             print("hello")
#             time.sleep(5)
#         exit()

# f = cssexample()
# f.test()

# CSS Selector - HTML uses css for layouting the webpages i.e. to beautify the webpages

# syntax - tagname[attribute = 'value']

# id=#
# example: #value or input#value
# class="."
# example: .value or input.value

# multiple classes = .class1.class2.class3
# using wildcards

# "^" = to find the value from first word
# "$" = to find the value from last word
# "*" = to find the value from anywhere of the word

# Syntax = tagname[attribute<spl character>=value]

# to find children nodes
# syntax[headername>tagnameattributevalue]
# example: fieldset>input#name


# xpath

# 1. absolute xpath
# 2.relative xpath

# syntax: //tag[@attribute = value]


