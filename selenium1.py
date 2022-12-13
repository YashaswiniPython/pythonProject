# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# from selenium.webdriver import ActionChains

# driver = webdriver.Chrome("./driver/chromedriver.exe")
# driver.get("https://www.amazon.com/")
# driver.maximize_window()
# driver.implicitly_wait(5)
# driver.quit()

# class findele():
#     def test():
        # driver.find_element("id","twotabsearchtextbox").send_keys("mobiles")
        # driver.find_element(By.CLASS_NAME,"nav-input nav-progressive-attribute")
        # driver.find_element("link_text","Sell").click()
        # driver.find_element(By.PARTIAL_LINK_TEXT,"Customer").click()
        # driver.find_element("Xpath",'//input[@id="nav-search-submit-button"]').click()
        # driver.find_element("CSS", 'input[id="nav-search-submit-button"]').click()
        # driver.find_element(By.NAME,"field-keywords").send_keys("mobiles")
        # driver.find_element(By.TAG_NAME,"a").click()
#         time.sleep(20)
#     if test is not None:
#         print("success")
# findele()

# actionchains
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# from selenium.webdriver import ActionChains

# class AA():
#     def mouseover():
#
#         driver = webdriver.Chrome("./driver/chromedriver.exe")
#         driver.get("https://courses.letskodeit.com/practice")
#         driver.maximize_window()
#         driver.implicitly_wait(5)
#
#         try:
#             driver.execute_script("window.scrollBy(0,600);")
#             time.sleep(5)
#             actions = ActionChains(driver)
#             MH = driver.find_element(By.ID, "mousehover")
#             actions.move_to_element(MH).perform()
#             ck = driver.find_element(By.XPATH,'//div[@class="mouse-hover-content"] //a[text()="Top"]')
#             actions.move_to_element(ck).click()
#             print("success")
#
#         except:
#
#             print("error")
# g = AA
# g.mouseover()


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# from selenium.webdriver import ActionChains

# class AA():
#     def dragdrop():
#         driver = webdriver.Chrome("./driver/chromedriver.exe")
#         driver.get("https://jqueryui.com/droppable/")
#         driver.maximize_window()
#         driver.implicitly_wait(5)
#
#         driver.switch_to.frame(0)
#
#         fromelement = driver.find_element("id","draggable")
#         toelement = driver.find_element("id", "droppable")
#
#         try:
#             actions = ActionChains(driver)
#             # actions.drag_and_drop(fromelement, toelement).perform()
#             actions.click_and_hold(fromelement).move_to_element(toelement).release().perform()
#             print("success")
#             time.sleep(5)
#
#         except:
#             print("unsuccess")
#
#
# d = AA
# d.dragdrop()

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# from selenium.webdriver import ActionChains

# class AA():
#     def slider():
#         driver = webdriver.Chrome("./driver/chromedriver.exe")
#         driver.get("https://jqueryui.com/slider/")
#         driver.maximize_window()
#         driver.implicitly_wait(5)
#
#         driver.switch_to.frame(0)
#
#         element = driver.find_element("id","slider")
#
#         try:
#             actions = ActionChains(driver)
#             actions.drag_and_drop_by_offset(element,100,0)
#             print("success")
#             time.sleep(5)
#
#         except:
#             print("unsuccess")
#
#
# d = AA
# d.slider()

# import time
# from selenium import webdriver
# from selenium.webdriver import ActionChains
#
# class AA():
#     def slider():
#         driver = webdriver.Chrome("./driver/chromedriver.exe")
#         driver.get("https://jqueryui.com/slider/")
#         driver.maximize_window()
#
#         # driver.execute_script("window.scrollBy(0,500);")
#         driver.switch_to.frame(0)
#         slider = driver.find_element("xpath",'//span[@class="ui-slider-handle ui-corner-all ui-state-default"]')
#         # droper= driver.find_element("id","droppable")
#
#         try:
#             actions = ActionChains(driver)
#             # actions.drag_and_drop(drager,droper).perform()
#             actions.drag_and_drop_by_offset(slider,0,100).perform()
#             time.sleep(10)
#             print("success")
#             driver.quit()
#
#         except:
#             print("unsuccess")
#
#
# g = AA
# g.slider()
# import time
#
# from selenium import webdriver
# class radio():
#     def test(self):
#         driver = webdriver.Chrome("./driver/chromedriver.exe")
#         driver.get("https://courses.letskodeit.com/practice")
#         driver.maximize_window()
#
#         ire = driver.find_elements("xpath",'//input[contains (@name,"cars") and contains(@type,"radio")]')
#         M = len(ire)
#         print("length of RB is"+str(M))
#
#         for radiobutton in ire:
#             sel = radiobutton.is_selected()
#
#             if not sel:
#                 radiobutton.click()
#                 time.sleep(5)
#
# i = radio()
# i.test()

# from selenium import webdriver
#
# class checkbox():
#     def test(self):
#         driver = webdriver.Chrome("./driver/chromedriver.exe")
#         driver.get("https://courses.letskodeit.com/practice")
#         driver.maximize_window()
#
#         chk = driver.find_elements("xpath",'//input[contains(@type,"checkbox") and contains(@name,"cars")]')
#         l = len(chk)
#         print("length is:" +str(l))
#
#         for checkbox in chk:
#             sel = checkbox.is_selected()
#             print("success")
#
#             if not sel:
#                 checkbox.click()
# o = checkbox()
# o.test()

# from selenium import webdriver
# import time
#
# class findingelements():
#     def test():
#         baseurl="https://www.goibibo.com/bus/online-go-bus-booking/"
#         driver=webdriver.Chrome("./driver/chromedriver.exe")
#         driver.maximize_window()
#         driver.get(baseurl)
#         driver.implicitly_wait(10)
#
#
#         driver.find_element("id","searchWidgetDeparture").click()
#         driver.implicitly_wait(5)
#
#         driver.find_element("xpath",'//input[@placeholder="Pick a date"]').click()
#         driver.implicitly_wait(10)
#         driver.find_element("xpath",'//span[text()="10"]').click()
#         driver.implicitly_wait(5)
#         driver.close()
#
#
# ff = findingelements
# ff.test()


# from selenium import webdriver
# import time
#
# class hiddenele():
#     def test():
#         driver = webdriver.Chrome("./driver/chromedriver.exe")
#         driver.get("https://courses.letskodeit.com/practice")
#         driver.maximize_window()
#         driver.implicitly_wait(5)
#
#         driver.execute_script("window.scrollBy(0,300);")
#
#         eletxt = driver.find_element("xpath", '//input[@class="inputs displayed-class"]')
#         eletxt.send_keys("yashu")
#         time.sleep(5)
#         hide = driver.find_element("id","hide-textbox").click
#         time.sleep(10)
#         o = eletxt.is_displayed()
#         print("text is hidden" +str(o))
#         # if eletxt.is_displayed():
#         #     print("if it is false" +str(hide))
#         show = driver.find_element("id","hide-textbox").click
#         time.sleep(10)
#         n = eletxt.is_displayed()
#         time.sleep(5)
#         print("text is visble" +str(n))
#         # if eletxt.is_displayed():
#         #     print("if it is True" +str(hide))
#
# i = hiddenele
# i.test()


from selenium import webdriver
import time

class frame():
    def test():
        driver = webdriver.Chrome("./driver/chromedriver.exe")
        driver.get("https://courses.letskodeit.com/practice")
        driver.maximize_window()
        driver.implicitly_wait(5)

        driver.execute_script("window.scrollBy(0,1000);")

        driver.switch_to.frame("courses-iframe")

        driver.find_element("xpath",'//input[@name="course"]').send_keys("JavaScript for beginners")
        driver.find_element("xpath",'//i[@class="fa fa-search"]').click()
        driver.find_element("xpath",'//img[@class = "img-responsive"]').click()
        time.sleep(5)

        driver.switch_to.default_content()
        time.sleep(5)
        print("success")

        # parenthandle = driver.current_window_handle
        # print("Parent window is:"+parenthandle)
        #
        # driver.find_element("id","openwindow").click()
        #
        # handles = driver.window_handles
        #
        # for handle in handles:
        #     print("The handle is:" +handle)
        # if handles not in parenthandle:
        #     driver.switch_to.window(handles)
        #     time.sleep(10)
        # driver.switch_to.default_content()
        # print("success")

i = frame
i.test()






























