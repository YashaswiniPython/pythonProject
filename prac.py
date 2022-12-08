# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# class radchk():
#      def button():
#         driver = webdriver.Chrome("./driver/chromedriver.exe")
#         driver.get("https://courses.letskodeit.com/practice")
#         driver.maximize_window()
#         time.sleep(5)

        # xp = driver.find_elements(By.XPATH,'//input[@name="cars" and contains (@type,"radio")]')      #radiobutton
        # chk = driver.find_elements(By.XPATH,'//input[@name="cars" and contains (@type,"checkbox")]')
        # stru = len(xp)   #radiobutton
        # stru = len(chk)    #checkbox
        # print(stru)

        # for radiobutton in xp:
        #     sel = radiobutton.is_selected()
        #
        #     if not sel:
        #         radiobutton.click()

        # for checkbox in chk:
        #     sel = checkbox.is_selected()
        #
        #     if not sel:
        #         checkbox.click()
        #         print("success")
        #         time.sleep(5)

# f = radchk
# f.button()







# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# import time

# class lis():
#     def dropd():
#         driver = webdriver.Chrome("./driver/chromedriver.exe")
#         driver.get("https://courses.letskodeit.com/practice")
#         driver.maximize_window()
#         time.sleep(5)
#
#         d = driver.find_elements("id","carselect")
#
#         sel = Select(d)
#         h = sel.select_by_index(0)
#         print(h)
#         time.sleep(5)
#         i = sel.select_by_value(Benz)
#         print(i)
#         time.sleep(5)
#         i = sel.select_by_visible_text(Honda)
#         print(i)
#         time.sleep(5)
#
# r = lis
# r.dropd()



from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

class win():
    def han():
        driver = webdriver.Chrome("./driver/chromedriver.exe")
        driver.get("https://courses.letskodeit.com/practice")
        driver.maximize_window()
        time.sleep(5)

        PH = driver.current_window_handle

        driver.find_element(By.ID,"openwindow").click()
        handle = driver.window_handles

        try:
            for handle in handles:
                print("Handle is" + handle)

                if handle not in PH:
                    driver.switch_to.window(handle)

                k = driver.find_element(By.ID, '//input[@placeholder="Search Course"]')
                k.send_keys("Python")
                print("success")
        except:
            print("error")


m = win
m.han()






















