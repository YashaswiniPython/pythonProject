# import time
# from selenium import webdriver
# from selenium.webdriver import ActionChains

# class act():
#     def m():
        # driver = webdriver.Chrome("./driver/chromedriver.exe")
        # driver.get("https://courses.letskodeit.com/practice")
        # driver.get("https://jqueryui.com/droppable/")
        # driver.get("https://jqueryui.com/slider/")
        # driver.maximize_window()
        # driver.implicitly_wait(5)
        # driver.execute_script("window.scrollBy(0,600);")

        # actions = ActionChains(driver)
        # mouho = driver.find_element("id", "mousehover")
        # actions.move_to_element(mouho)
        # time.sleep(5)
        # i = driver.find_element("xpath", '//a[text()="Top"]')
        # actions.move_to_element(i).click()
        # time.sleep(5)

        # driver.switch_to.frame(0)
        #
        # from1 = driver.find_element("id","draggable")
        # to2 = driver.find_element("id","droppable")
        #
        # actions = ActionChains(driver)
        # # actions.drag_and_drop(from1, to2).perform()
        # actions.click_and_hold(from1).move_to_element(to2).release().perform()
        # time.sleep(10)

        # actions = ActionChains(driver)
        # r = driver.find_element("id","slider")
        # actions.drag_and_drop_by_offset(r,400,0).perform()
        # print("success")
        # time.sleep(5)

# t = act
# t.m()
#
# import time
# from selenium import webdriver
#
# class rad():
#     def m():
#         driver = webdriver.Chrome("./driver/chromedriver.exe")
#         driver.get("https://courses.letskodeit.com/practice")
#         # driver.get("https://jqueryui.com/checkboxradio/")
#         driver.maximize_window()
#         driver.execute_script("window.scrollBy(0,300);")
#
#         driver.switch_to.frame(0)
#
#         # rb = driver.find_elements("xpath",'//input[contains(@name,"radio-1") and contains (@type,"radio")]')
#         rb = driver.find_elements("xpath",'//input[contains(@class,"ui-checkboxradio ui-helper-hidden-accessible") and contains (@type,"checkbox")]')
#         h = len(rb)
#         print(h)
#
#         # for radiobutton in rb:
#         #     sel = radiobutton.is_selected()
#         #     print(sel)
#         #     time.sleep(10)
#         #
#         #     if not sel:
#         #         radiobutton.click()
#         #         time.sleep(8)
#         #         print("success")
#
#         for checkbox in rb:
#             sel = checkbox.is_selected()
#             print(sel)
#             time.sleep(10)
#
#             if not sel:
#                 checkbox.click()
#                 time.sleep(8)
#                 print("success")
#
# k = rad
# k.m()


# import time
# from selenium import webdriver
#
# class switches():
#     def m():
#         driver = webdriver.Chrome("./driver/chromedriver.exe")
#         driver.get("https://courses.letskodeit.com/practice")
#         # driver.get("https://jqueryui.com/checkboxradio/")
#         driver.maximize_window()
#         driver.execute_script("window.scrollBy(0,600);")
#
#         driver.find_element("id","courses-iframe")
#
#         driver.find_element("xpath", '//input[@placeholder="Search Course"]').send_keys("JavaScript for beginners")
#         time.sleep(5)
#         driver.find_element("xpath",'//i[@class="fa fa-search"]').click()
#         time.sleep(2)
#         driver.switch_to.default_content()
#         time.sleep(5)
#         print("success")
#
# d = switches
# d.m()

#
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# class selen():
#     def radio():
#         driver = webdriver.Chrome(r"C:\Users\Yashaswini\PycharmProjects\pythonProject")
#         driver.get("https://courses.letskodeit.com/practice")
#         time.sleep(5)
#         driver.maximize_window()
#
#         h = driver.find_element(By.XPATH,'//input[@name="cars" and contains (@type,"radio")]')
#         g = len(h)
#         print(g)
#
#         for radiobutton in h:
#             sel = radiobutton.is_selected()
#             print("success")
#
#             if not sel:
#                 radiobutton.click()
#                 time.sleep(5)
# f = selen
# f.radio()













