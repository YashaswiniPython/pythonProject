# import time
#
# from selenium import webdriver
#
# class runscript():
#     def test(self):
#         driver = webdriver.Chrome(executable_path="./driver/chromedriver.exe")
#         driver.get("https://login.yahoo.com/")
#         # driver.get("https://www.amazon.com/")
#         driver.maximize_window()
#         time.sleep(5)
#
# c = runscript()
# c.test()




#
#         # byid = driver.find_element('id','login-username')
#         # byclassname = driver.find_element('class name','nav-input nav-progressive-attribute')
#         byname = driver.find_element('name','')
#         byclassname.click()
#         if byclassname is not None:
#             print("success")
#             time.sleep(5)
#             driver.close()
#


# By method
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# class bymethod():
#     def test(self):
#         driver = webdriver.Chrome("./driver/chromedriver.exe")
#         driver.get("https://www.amazon.com/")
#         driver.maximize_window()
#         time.sleep(5)
#
#         Byid = driver.find_element(By.ID,'twotabsearchtextbox')
#         Byid.send_keys("Mobiles")
#         if Byid is not None:
#             print("Success")
#             time.sleep(5)
#
# c = bymethod()
# c.test()

# id, name, classname, tagname, link text, Partial link text,xpath,css selectors
# By.Id,name, classname, tagname, link text, Partial link text,xpath,css selectors

# effective xpath by text
# ex: //div[@class='nav-progressive-content']//a[text()='Sell']


# actions

# from selenium import webdriver
# import time
#
# class action():
#     def test1(self):
#         driver = webdriver.Chrome("./driver/chromedriver.exe")
#         driver.get("https://www.amazon.in/")
#         driver.maximize_window()
#         time.sleep(10)
#
#         s = driver.find_element('id','twotabsearchtextbox')
#         s.send_keys("mobiles")
#         c = driver.find_element('id','nav-search-submit-button')
#         c.click()
#         if c is not None:
#             print("success")
#             time.sleep(10)
#             driver.close()
# a = action()
# a.test1()
#
# is_enabled
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# class enable():
#     def test(self):
#         driver = webdriver.Chrome("./driver/chromedriver.exe")
#         driver.get("https://www.google.co.in/")
#         driver.maximize_window()
#         driver.implicitly_wait(5)
#
#         enable = driver.find_element(By.XPATH,"//input[@class = 'gLFyf gsfi']")
#         time.sleep(5)
#         enable.send_keys("capgemini")
#         if enable is not None:
#             print("success")
#
#
# c = enable()
# c.test()


# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
#
# class radiocheck():
#     def test(self):
#         driver = webdriver.Chrome("./driver/chromedriver.exe")
#         driver.get("https://courses.letskodeit.com/practice")
#         driver.maximize_window()
#         time.sleep(10)
#
#         radio = driver.find_element(By.ID,'hondaradio')
#         radio.click()
#         time.sleep(1)
#         radio1 = driver.find_element(By.ID,'bmwradio')
#         radio1.click()
#         check = driver.find_element(By.ID,'bmwcheck')
#         check.click()
#         time.sleep(3)
#         check1 = driver.find_element(By.ID, 'hondacheck')
#         check1.click()
#         # driver.close()
#
#         print("is radio is selected" +str(radio.is_selected()))
#         print("is radio1 is selected" + str(radio1.is_selected()))
#         print("is check is selected" + str(check.is_selected()))
#         print("is check1 is selected" + str(check1.is_selected()))
#
#
# r = radiocheck()
# r.test()



# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
# class list():
#     def test(self):
#         driver = webdriver.Chrome("./driver/chromedriver.exe")
#         driver.get("https://courses.letskodeit.com/practice")
#         driver.maximize_window()
#         time.sleep(10)
#
#         rb = driver.find_elements(By.XPATH,"//input[contains(@name,'cars') and contains(@type,'radio')]")
#         h = len(rb)
#         print("size of the list is" +str(h))
#
#         for radiobutton in rb:
#             issel = radiobutton.is_selected()
#
#             if not issel:
#                 radiobutton.click()
#                 time.sleep(3)
#
# m = list()
# m.test()


# Dropdown



# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# class drop():
#     def test(self):
#         driver = webdriver.Chrome("./driver/chromedriver.exe")
#         driver.get("https://courses.letskodeit.com/practice")
#         driver.maximize_window()
#         time.sleep(5)
#
#         dd = driver.find_element(By.ID,'carselect')
#         select = Select(dd)
#         select.select_by_index("2")
#         print("Selected index is benz")
#         select.select_by_value("honda")
#         print("Selected value is honda")
#         select.select_by_visible_text("BMW")
#         print("Selected value is BMW")
#         select.select_by_index(0)
#         print("Selected value is Honda")
#
#
# s = drop()
# s.test()

# hidden elements

# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# class hiddenel():
#     def test(self):
#         driver = webdriver.Chrome("./driver/chromedriver.exe")
#         driver.get("https://courses.letskodeit.com/practice")
#         driver.maximize_window()
#         time.sleep(5)
#
#         he = driver.find_element(By.ID,'displayed-text')
#         r = he.is_displayed()
#         print("sucess"+str(r))
#         hide = driver.find_element(By.ID,'hide-textbox')
#         hide.click()
#         n = hide.is_displayed()
#         print("display success" + str(n))
#         time.sleep(2)
#         show = driver.find_element(By.ID, 'show-textbox')
#         show.click()
#         i = show.is_displayed()
#         print("display success" +str(i))
#         time.sleep(2)
#
# c = hiddenel()
# c.test()

# Methods
# get text
# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By

# class gettext():
#     def text(self):
#         driver = webdriver.Chrome("./driver/chromedriver.exe")
#         driver.get("https://www.amazon.in/")
#         driver.maximize_window()
#
#         fe = driver.find_element(By.ID,"glow-ingress-line2")
#         m = fe.text
#         print("Text on the link is:" +m)
#
# c = gettext()
# c.text()

# get attribute
# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
#
# class getat():
#     def test(self):
#         driver = webdriver.Chrome("./driver/chromedriver.exe")
#         driver.get("https://www.amazon.in/")
#         driver.maximize_window()
#
#         val = driver.find_element(By.XPATH,"// span[ @ id = 'glow-ingress-line2']")
#         find = val.get_attribute("id")
#         print("The value of the attribute is:" +find)
#         driver.implicitly_wait(5)
# d = getat()
# d.test()

# switch to window

# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
# imp: current.windowhandles, swtichto.window.handles
#
# class Findele():
#     def test(self):
#         driver = webdriver.Chrome("./driver/chromedriver.exe")
#         driver.get("https://www.amazon.in/")
#         driver.maximize_window()
#         time.sleep(3)
#
#         ph = driver.current_window_handle
#         print("current window is" +ph)
#
#         m = driver.find_element(By.ID,"nav-global-location-popover-link")
#         m.click()
#
#         handles = driver.window_handles
#
#         for handle in handles:
#             print("handle is" +handle)
#
#             if handle not in ph:
#                 driver.switch_to.window(handle)
#                 l = driver.find_element(By.XPATH,"//input[@class='GLUX_Full_Width a-declarative']")
#                 l.send_keys(560026)
#                 time.sleep(20)
#                 driver.close()
#                 break
#
#         driver.switch_to.window(ph)
#         driver.find_element(By.ID,"twotabsearchtextbox").send_keys("mobiles")
#         time.sleep(20)
#
# n = Findele()
# n.test()

#
# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
#
# class frame():
#     def test(self):
#         driver = webdriver.Chrome("./driver/chromedriver.exe")
#         driver.get("https://courses.letskodeit.com/practice")
#         driver.maximize_window()
#         driver.execute_script("window.scrollBy(0,1000);")
#         time.sleep(3)
#
#         # switch by name
#         # driver.switch_to.frame("iframe-name")
#
#         # switch by id
#         # driver.switch_to.frame("courses-iframe")
#
#         # switch by id
#         driver.switch_to.frame(0)
#
#
#         driver.switch_to.default_content()
#         driver.execute_script("window.scrollBy(0,-1000);")
#         w = driver.find_element(By.ID,"name")
#         w.send_keys("Yashu")
#         time.sleep(10)
#         driver.close()
#
# k = frame()
# k.test()


# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By

# it works only for javascript pop ups, not required for window or html popup
# class popup():
#     def test(self):
#         driver = webdriver.Chrome("./driver/chromedriver.exe")
#         driver.get("https://courses.letskodeit.com/practice")
#         driver.maximize_window()
#         # time.sleep(5)
#
#         h = driver.find_element(By.ID,"name")
#         h.send_keys("Yashu")
#
#         a1 = driver.find_element(By.ID,"alertbtn")
#         a1.click()
#
#         alert1 = driver.switch_to.alert
#         alert1.accept()
#
#         time.sleep(10)
#
#         a2 = driver.find_element(By.ID, "confirmbtn")
#         a2.click()
#
#         alert2 = driver.switch_to.alert
#         alert2.dismiss()
#
#         time.sleep(10)
#
# n = popup()
# n.test()

# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
# class iselement():
#     def test(self):
#         driver = webdriver.Chrome("./driver/chromedriver.exe")
#         driver.get("https://courses.letskodeit.com/practice")
#         driver.maximize_window()
#         time.sleep(5)
        # getting text
        # n = driver.find_element(By.ID,"opentab")
        # result = n.text
        # print("The result is:" +result)
        # getting value of the attribute
        # n1 = driver.find_element(By.ID, "opentab")
        # result1 = n.get_attribute("ID")
        # print("The result is:" + result1)

#
# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
#
# class login():
#     def test(self):
#         driver = webdriver.Chrome("./driver/chromedriver.exe")
#         driver.get("https://letskodeit.teachable.com/")
#         driver.maximize_window()
#         time.sleep(5)
#
#         h = driver.find_element(By.LINK_TEXT,"Login")
#         h.click()
#
#         h1 = driver.find_element(By.NAME,"email")
#         h1.send_keys("test@email.com")
#         time.sleep(5)
#
#         h2 = driver.find_element(By.ID, "password")
#         h2.send_keys("abcabc")
#         time.sleep(5)
#
#         i = driver.find_element(By.NAME,"commit")
#         i.click()
#         time.sleep(5)
#
#         driver.close()
#
# hi = login()
# hi.test()
















































































