import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('https://passport.jd.com/new/login.aspx?ReturnUrl=https%3A%2F%2Fwww.jd.com%2F%3Fcu%3Dtrue%26utm_source%3Dbaidu-pinzhuan%26utm_medium%3Dcpc%26utm_campaign%3Dt_288551095_baidupinzhuan%26utm_term%3D0f3d30c8dba7459bb52f2eb5eba8ac7d_0_5bbdebeff1ce4f16859f89fd8a3dd46d')

agree=driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[1]/div/div[3]/a')
agree.click()
agree=driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[1]/div/div[3]/a')


agree=driver.find_element_by_xpath('//*[@id="loginname"]')
agree.clear()
agree.send_keys('18206106822')

agree=driver.find_element_by_xpath('//*[@id="nloginpwd"]')
agree.clear()
agree.send_keys('749684..')

agree=driver.find_element_by_xpath('//*[@id="loginsubmit"]')
agree.click()

# knob = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,
#                                                    '//*[@id="JDJRV-wrap-loginsubmit"]/div/div/div/div[2]/div[3]')))
c=driver.find_element_by_xpath('//*[@id="JDJRV-wrap-loginsubmit"]/div/div/div/div[2]/div[3]')
action=ActionChains(driver)

action.click_and_hold(c).perform()
action.move_by_offset(69,0).perform()
action.release()

driver.save_screenshot('2.png')

time.sleep(10)

driver.quit()
