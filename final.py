
# Selenium

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

# class mouse():
#     def actions():
#         driver = webdriver.Chrome("./driver/chromedriver.exe")
#         driver.get("https://courses.letskodeit.com/practice")
#         driver.maximize_window()
#
#         m = driver.find_element(By.ID,"mousehover")
#
#         try:
#             actions = ActionChains(driver)
#             actions.move_to_element(m)
#             time.sleep(5)
#
#             l = driver.find_element(By.XPATH, '//a[contains(text(),"Top")]')
#             actions.move_to_element(l).click()
#             time.sleep(5)
#
#         except:
#
#             print("error")
#
#
# t = mouse
# t.actions()

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver import ActionChains
#
# class actions():
#     def dsquare():
#         driver = webdriver.Chrome("./driver/chromedriver.exe")
#         driver.get("https://jqueryui.com/droppable/")
#         driver.maximize_window()
#
#         driver.switch_to.frame(0)
#
#         drag = driver.find_element("id","draggable")
#         drop1 = driver.find_element("id","droppable")
#
#         try:
#             actions = ActionChains(driver)
#             # actions.drag_and_drop(drag,drop1).perform()
#             actions.click_and_hold(drag).move_to_element(drop1).release().perform()
#             time.sleep(5)
#
#         except:
#             print("error")
#
# t = actions
# t.dsquare()


# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver import ActionChains
#
# class actions():
#     def slider():
#         driver = webdriver.Chrome("./driver/chromedriver.exe")
#         driver.get("https://jqueryui.com/slider/")
#         driver.maximize_window()
#
#         driver.switch_to.frame(0)
#         m = driver.find_element("id", "slider")
#
#         try:
#
#             actions = ActionChains(driver)
#             actions.drag_and_drop_by_offset(m,500,0).perform()
#             time.sleep(5)
#
#         except:
#             print("error")
#
# y = actions
# y.slider()



# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# class buttons():
#     def radb():
#         driver = webdriver.Chrome("./driver/chromedriver.exe")
#         driver.get("https://courses.letskodeit.com/practice")
#         driver.maximize_window()
#
#         try:
#             chk = driver.find_elements(By.XPATH,'//input[contains(@name,"cars") and contains (@type,"radio")]')
#             l = len(chk)
#             print("length is:" +str(l))
#
#             for radiobutton in chk:
#                 sel = radiobutton.is_selected()
#
#                 if not sel:
#                     radiobutton.is_selected()
#                     print("success")
#
#
#         except:
#             print("error")
#
#
#
# t = buttons
# t.radb()


# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
#
# class buttons():
#     def dropdown():
#         driver = webdriver.Chrome("./driver/chromedriver.exe")
#         driver.get("https://courses.letskodeit.com/practice")
#         driver.maximize_window()
#
#         h = driver.find_element("id","carselect")
#
#         i = Select(h)
#         i.select_by_value("bmw")
#         time.sleep(2)
#         m = i.select_by_index(1)
#         time.sleep(2)
#         n = i.select_by_visible_text("Honda")
#         time.sleep(2)
#
#
# r = dropdown
# r.chkbx()


# import time
# from selenium import webdriver
# # from selenium.webdriver.common.by import By
# # from selenium.webdriver.support.select import Select
#
# class buttons():
#     def chkbx():
#         driver = webdriver.Chrome("./driver/chromedriver.exe")
#         driver.get("https://courses.letskodeit.com/practice")
#         driver.maximize_window()
#
#         chk = driver.find_elements("xpath",'//input[contains(@name,"cars") and contains (@type,"checkbox")]')
#         i = len(chk)
#         print(i)
#
#         for checkbox in chk:
#             sel = checkbox.is_selected()
#             print(sel)
#
#             if not sel:
#                 checkbox.click()
#                 print("success")
#                 time.sleep(3)
#
#
# g = buttons
# g.chkbx()


# import time
# from selenium import webdriver

#
# class swicth():
#     def WH():
#         driver = webdriver.Chrome("./driver/chromedriver.exe")
#         driver.get("https://courses.letskodeit.com/practice")
#         driver.maximize_window()
#
#         PH = driver.current_window_handle
#
#         driver.find_element("id","openwindow").click()
#
#         handles = driver.window_handles
#
#         for handle in handles:
#             print("handles are",handle)
#
#             if handle not in PH:
#                 driver.switch_to.window(handle)
#                 time.sleep(3)
#
#                 driver.find_element("xpath", '//input[@placeholder="Search Course"]').send_keys("python")
#                 time.sleep(5)
#                 driver.find_element("xpath", '//button[@class="find-course search-course"]').click()
#                 time.sleep(5)
#             driver.switch_to.default_content()
#             print("success")
#
# r = swicth
# r.WH()

# import time
# from selenium import webdriver
#
#
# class swicth():
#     def SF():
#         driver = webdriver.Chrome("./driver/chromedriver.exe")
#         driver.get("https://courses.letskodeit.com/practice")
#         driver.maximize_window()
#
#         driver.execute_script("window.scrollBy(0,600);")
#
#         # driver.find_element("id","courses-iframe")
#         driver.switch_to.frame("courses-iframe")
#
#         driver.find_element("xpath",'//h4[@class="dynamic-heading" and contains (text(),"JavaScript for beginners")]').click()
#         time.sleep(3)
#
#
# m = swicth
# m.SF()


import time
from selenium import webdriver


class swicth:
    def RB(self):
        driver = webdriver.Chrome("./driver/chromedriver.exe")
        driver.get("https://jqueryui.com/checkboxradio/")
        driver.maximize_window()
        driver.execute_script("window.scrollBy(0,700);")

        driver.switch_to.frame(0)

        # m = driver.find_elements("xpath",'//input[@name="radio-1"]/..//span[1]')
        m = driver.find_elements("xpath",'//input[@name="checkbox-1"]/..//span[1]')
        f = len(m)
        print(f)

        # for radiobutton in m:
        for checkbox in m:
            # sel = radiobutton.is_selected()
            sel = checkbox.is_selected()
            print(sel)
            time.sleep(2)

            if not sel:
                checkbox.click()
                time.sleep(2)


i = swicth()
i.RB()
















