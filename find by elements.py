# import os
#
# from selenium import webdriver
# import os
# # import time
#
# class elementbyid():
#     def test(self):
#         baseurl = "https://courses.letskodeit.com/practice"
#         driverlocation = "./driver/chromedriver.exe"
#         os.environ["webdriver.chrome.driver"] = driverlocation
#         driver = webdriver.Chrome(driverlocation)
#         driver.maximize_window()
#         driver.get(baseurl)
#
#         elementbyid = driver.find_element('id','name')
#         if elementbyid is not None:
#             print("success")
#
#         elementByname = driver.find_element('name','enter-name')
#         if elementByname is not None:
#             print("success by name")
#
#
# f = elementbyid()
# f.test()
#
# from selenium import webdriver
# import time
#
# class findbyxpath():
#     def test(self):
#         driver = webdriver.Chrome("./driver/chromedriver.exe")
#         driver.get("https://courses.letskodeit.com/practice")
#         driver.maximize_window()
#
#         byelement = driver.find_element('xpath',"//input[@id = 'name']")
#
#         if byelement is not None:
#             print("success")
#
#         byelements = driver.find_element('css selector','#displayed-text')
#
#         if byelements is not None:
#             print("super success")
#             time.sleep(5)
#
# s = findbyxpath()
# s.test()
# import time
#
# from selenium import webdriver
#
# class findelements():
#     def test(self):
#         driver = webdriver.Chrome("./driver/chromedriver.exe")
#         driver.get("https://courses.letskodeit.com/practice")
#         driver.maximize_window()
#
#         findelements1 = driver.find_element('link text','SIGN IN')
#         if findelements1 is not None:
#             print("founded")
#
#         findelements2 = driver.find_element('partial link text','HOM')
#         if findelements is not None:
#             print("success")
#             time.sleep(5)
#         exit()
#
# f = findelements()
# f.test()
# import time
#
# from selenium import webdriver
#
# class findelements():
#     def test(self):
#         driver = webdriver.Chrome("./driver/chromedriver.exe")
#         driver.get("https://courses.letskodeit.com/practice")
#         driver.maximize_window()
#
#         elements = driver.find_element('class name','displayed-class')
#         if elements is not None:
#             print("success")
#             time.sleep(5)
#
#         elements = driver.find_element('tag name', 'a')
#         if elements is not None:
#             print("success tag")
#             time.sleep(5)
#
#
#
# f = findelements()
# f.test()

# BY method
# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# class example():
#     def test(self):
#         driver = webdriver.Chrome("./driver/chromedriver.exe")
#         driver.get("https://flipkart.com/")
#         driver.maximize_window()
#
#         find = driver.find_element(By.CLASS_NAME,"_3704LK")
#         if find is not None:
#             print("Success")
#             time.sleep(5)
#         exit()
#
# f = example()
# f.test()

# list of elements
# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# class example():
#     def test(self):
#         driver = webdriver.Chrome("./driver/chromedriver.exe")
#         driver.get("https://www.flipkart.com/")
#         driver.maximize_window()
#
#         elements = driver.find_elements(By.TAG_NAME,'input')
#         length = len(elements)

        # if elements is not None:
        #     print("Length of the string is :" +str(len))
#
#             time.sleep(6)
#         exit()
# f = example()
# f.test()
import time

# from selenium.webdriver import ActionChains
# from selenium import webdriver
# from selenium.webdriver.common.by import By

# class action():
#     def test():
#         driver = webdriver.Chrome("./driver/chromedriver.exe")
#         driver.get("https://courses.letskodeit.com/practice")
#         # driver.get("https://jqueryui.com/droppable/")
#         driver.maximize_window()
#
#         action = ActionChains(driver)
#         driver.execute_script("window.scrollBy(0,600);")
#         time.sleep(5)
#         MH = driver.find_element(By.ID,"mousehover")
#         action.move_to_element(MH).perform()
#         l = driver.find_element("xpath",'//a[text()="Top"]')
#         action.move_to_element(l).click()
#         time.sleep(5)
#         print("Success")
#
#
# n = action
# n.test()

# class action():
#     def test():
#         driver = webdriver.Chrome("./driver/chromedriver.exe")
#         # driver.get("https://courses.letskodeit.com/practice")
#         driver.get("https://jqueryui.com/droppable/")
#         driver.maximize_window()
#
#         driver.switch_to.frame(0)
#
#         drag = driver.find_element("id","draggable")
#         drop = driver.find_element("id", "droppable")
#
#         action = ActionChains(driver)
#         # action.drag_and_drop(drag,drop).perform()
#         action.click_and_hold(drag).move_to_element(drop).release().perform()
#         print("Success")
#
# n = action
# n.test()

# class action():
#     def test():
#         driver = webdriver.Chrome("./driver/chromedriver.exe")
#         # driver.get("https://courses.letskodeit.com/practice")
#         driver.get("https://jqueryui.com/slider/")
#         driver.maximize_window()
#
#         driver.switch_to.frame(0)
#         time.sleep(5)
#
#         action = ActionChains(driver)
#         l = driver.find_element("id","slider")
#         time.sleep(5)
#         action.drag_and_drop_by_offset(l,100,0).perform()
#         time.sleep(5)
#         print("success")
#         driver.quit()
#
#
# n = action
# n.test()


# from selenium import webdriver
# # from selenium.webdriver.common.by import By
# class radio():
#     def test():
#         driver = webdriver.Chrome("./driver/chromedriver.exe")
#         driver.get("https://courses.letskodeit.com/practice")
#         driver.maximize_window()
#
#         # driver.switch_to.frame(0)
#         # time.sleep(5)
#
#         n = driver.find_elements("xpath",'//input[contains (@name,"cars") and contains(@type,"radio")]')
#         o = len(n)
#         print(o)
#
#         for radiobutton in n:
#             sel = radiobutton.is_selected()
#             # print(sel)
#
#             if not sel:
#                 radiobutton.click()
#                 time.sleep(10)
#
# j = radio
# j.test()


# from selenium import webdriver
#
# class checkbox():
#     def test():
#         driver = webdriver.Chrome("./driver/chromedriver.exe")
#         driver.get("https://courses.letskodeit.com/practice")
#         driver.maximize_window()
#
#         chk = driver.find_elements("xpath", '//input[contains(@type,"checkbox") and contains(@name,"cars")]')
#         l = len(chk)
#         print("length is:" +str(l))
#
#         for checkbox in chk:
#             sel = checkbox.is_selected()
#
#             if not sel:
#                 checkbox.click()
#                 time.sleep(5)
#
# j = checkbox
# j.test()


# from selenium import webdriver
# class hidden():
#     def test():
#         driver = webdriver.Chrome("./driver/chromedriver.exe")
#         driver.get("https://courses.letskodeit.com/practice")
#         driver.maximize_window()
#         driver.execute_script("window.scrollBy(0,400);")
#
#         m = driver.find_element("id","displayed-text")
#         m.send_keys("yashu")
#         h = driver.find_element("id","hide-textbox").click()
#         time.sleep(5)
#         ol = m.is_displayed()
#         print(ol)
#         h = driver.find_element("id", "show-textbox").click()
#         time.sleep(5)
#         on = m.is_displayed()
#         print(on)
# x = hidden
# x.test()

# from selenium import webdriver
#
# class frame():
#     def test():
#         driver = webdriver.Chrome("./driver/chromedriver.exe")
#         driver.get("https://courses.letskodeit.com/practice")
#         driver.maximize_window()
#         driver.execute_script("window.scrollBy(0,600);")
#
#         # driver.switch_to.frame("courses-iframe")
#         #
        # r = driver.find_element("xpath",'//img[@src="https://s3.amazonaws.com/contents.newzenler.com/3072/courses/11131/data/thumb/s-2.jpg"]')
        # r.click()

# l = frame
# l.test()

# from selenium import webdriver
# from selenium.webdriver.support.select import Select
# class window():
#     def test():
#         driver = webdriver.Chrome("./driver/chromedriver.exe")
#         driver.get("https://courses.letskodeit.com/practice")
#         driver.maximize_window()
#         driver.execute_script("window.scrollBy(0,400);")
#
#         PH = driver.current_window_handle
#
#         driver.find_element("id","openwindow").click()
#         time.sleep(5)
#
#         handles = driver.window_handles
#
#         for handle in handles:
#             print("the handle is",handles)
#
#             if handle not in handles:
#                 driver.switch_to.window(handle)
#                 driver.find_element("xpath",'//input[(@id="search") and contains(@name,"course")]').send_keys("python")
#                 time.sleep()
#         driver.switch_to.window(PH)
#         driver.quit()
# j = window
# j.test()

# from selenium import webdriver
# class radio():
#     def test():
#         driver = webdriver.Chrome("./driver/chromedriver.exe")
#         driver.get("https://jqueryui.com/checkboxradio/")
#         driver.maximize_window()
#         driver.execute_script("window.scrollBy(0,300);")
#
#         driver.switch_to.frame(0)
#         driver.execute_script("window.scrollBy(0,500);")
#
#         i = driver.find_elements("xpath",'//input[contains(@type,"radio") and contains(@name,"radio-1")')
#         p = len(i)
#         print(p)
#
#         for radiobutton in i:
#             sel = radiobutton.click()
#
#         # for val in i:
#         #     sel = val.is_selected()
#         #     print(sel)
#         #
#         #     if not val.is_selected():
#         #         val.click()
#         #         time.sleep(4)
#         #         driver.quit()
#
#
# j = radio
# j.test()

# from selenium import webdriver
# from selenium.webdriver.support.select import Select
#
# class dd():
#     def test():
#         driver = webdriver.Chrome("./driver/chromedriver.exe")
#         driver.get("https://courses.letskodeit.com/practice")
#         driver.maximize_window()
#
#         select = driver.find_element("id","carselect")
#
#         sel = Select(select)
#         sel.select_by_value('bmw')
#         time.sleep(5)
#         sel.select_by_index(1)
#         time.sleep(5)
#         sel.select_by_visible_text("Honda")
#         time.sleep(5)
#
# i = dd
# i.test()

# from selenium import webdriver
# class WH():
#     def test():
#         driver = webdriver.Chrome("./driver/chromedriver.exe")
#         driver.get("https://courses.letskodeit.com/practice")
#         driver.maximize_window()
#
#         PH = driver.current_window_handle
#
#         driver.find_element("id","openwindow").click()
#         time.sleep(10)
#
#         handle = driver.window_handles
#
#         for handles in handle:
#             print("the handles are",handles)
#
#             if handles not in handle:
#                 driver.switch_to.window(handles)
#                 # time.sleep(5)
#                 print("success")
#                 driver.find_element("xpath",'//input[@placeholder="Search Course"]').send_keys("python")
#                 time.sleep(5)
#         driver.switch_to.window(PH)
#         print("Succeess to PH")
#
# i = WH
# i.test()

from selenium import webdriver

# class Frame():
#     def test():
#         driver = webdriver.Chrome("./driver/chromedriver.exe")
#         driver.get("https://courses.letskodeit.com/practice")
#         driver.maximize_window()
#
#         driver.switch_to.frame("courses-iframe")
#         driver.find_element("xpath", '//input[@placeholder="Search Course"]').send_keys("JavaScript for beginners")
#         time.sleep(5)
#         driver.find_element("xpath",'//i[@class="fa fa-search"]').click()
#         time.sleep(2)
#         driver.switch_to.default_content()
#         print("success")
#
#
# r = Frame
# r.test()



























