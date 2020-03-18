from selenium import webdriver

import time

from selenium.webdriver import ActionChains

driver=webdriver.Chrome()

driver.get('https://reg.gome.com.cn/register/index/person')
# # user=driver.find_element_by_class_name('login-title')
# # user.click()
# alerta=driver.switch_to.alert
# print(alerta.text)
driver.implicitly_wait(10)
time.sleep(2)


agree=driver.find_element_by_class_name('inpBtn')
agree.click()
# driver.switch_to.default_content()
#
# mobile=driver.find_element_by_xpath('//*[@id="mobile"]')
# mobile.send_keys("18206106822")
# agree1=driver.find_element_by_xpath('//*[@id="js-dingxiang"]/a')
# agree1.click()
# move=driver.find_element_by_xpath('//*[@id="dx_captcha_basic_slider-img-active_1"]')
# action=ActionChains(driver)
# action.click_and_hold(move).perform()
#
# action.move_by_offset(50,0).perform()
# time.sleep(5)
#
#
# action.release(move)
driver.quit()


