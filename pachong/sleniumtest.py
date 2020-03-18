from selenium import webdriver
from selenium.webdriver import ActionChains
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as cc
driver=webdriver.Chrome()
url='file:///home/python/Desktop/source/A.html'
driver.get(url)
driver.set_window_size(500,600)
driver.implicitly_wait(5)
sleep(3)
# user=driver.find_element_by_id("fwA")
# user.click()
# # user1=driver.find_element_by_name("userA")v
# # user1.send_keys("小花猫")
# pwd=driver.find_element_by_id("passwordA")
# pwd.send_keys("123456")
#
# telphone=driver.find_element_by_class_name("haha")
# telphone.send_keys("18206106822")
#
#
# # driver.find_element_by_tag_name("input")[0].send_keys("小猫爱吃鱼")
# driver.find_elements_by_tag_name("input")[1].send_keys("123456")
#
# apple=driver.find_element_by_xpath('//*[@id="pga"]')
# apple.click()
#
#
# orage=driver.find_element_by_xpath('//*[@value="jza"]')
# orage.click()
# sleep(3)
# element = WebDriverWait(driver, 10).until(cc.presence_of_element_located((By.ID, 'userA')))
# element.send_keys("admin")

# user=driver.find_element_by_xpath('//*[@id="fwA"]')
# user.click()
# handels=driver.window_handles
# driver.switch_to_window(handels[1])
# Action=ActionChains(driver)
# c=driver.find_element_by_id("kw")
# c.send_keys("小花")
# c.send_keys(Keys.ENTER)
# # d=driver.find_element_by_id("su")
# element=Action.double_click(d)
# element.perform()
# map=driver.find_element_by_xpath('//*[@id="u1"]/a[3]')
# element=Action.move_to_element(map)
# element.perform()

#
# select1=driver.find_element_by_xpath('//*[@id="selectA"]')
# at=Select(select1)
# at.select_by_index(0)
#
# driver.find_element_by_id("alerta").click()
# alert=driver.switch_to.alert
# print(alert.text)
# sleep(3)
# # alert.accept()
# # sleep(2)
# alert.dismiss()
js="window.scrollTo(1000,1000)"
driver.execute_script(js)
sleep(5)
driver.quit()