from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from PIL import Image
import time


def get_image(driver, n):
    # canvas = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/div[1]/div[1]/div/a/div[1]/div/canvas[2]')
    canvas = driver.find_element_by_xpath('//div[@class="geetest_window"]')
    print(canvas.location)
    print(canvas.size)
    left =round(1.25*canvas.location['x'])
    top = round(1.25*canvas.location['y'])
    elementWidth = left + round(1.25*canvas.size['width'])
    elementHeight = top + round(1.25*canvas.size['height'])
    image = driver.save_screenshot(n + '.png')

    picture = Image.open(n + '.png')
    print(picture.size)

    picture = picture.crop((left, top, elementWidth, elementHeight))
  
    print(picture.size)
    picture.save('photo' + n + '.png')
    return picture


def get_space(picture1, picture2):
    start = 80
    threhold=60

    for i in range(start, picture1.size[0]):
        for j in range(start,picture1.size[1]):
            rgb1 = picture1.load()[i, j]
            rgb2 = picture2.load()[i, j]
           
            res1 = abs(rgb1[0] - rgb2[0])
            res2 = abs(rgb1[1] - rgb2[1])
            res3 = abs(rgb1[2] - rgb2[2])
            if not (res1 < threhold and res2 < threhold and res3 < threhold):
                return round(i/1.25)-10
    return i


def get_tracks(space):
    # 模拟人工滑动，避免被识别为机器
    space +=20  # 先滑过一点，最后再反着滑动回来
    v = 0
    t = 0.3
    forward_tracks = []
    current = 0
    mid = space * 3 / 5
    while current < space:
        if current < mid:
            a = 2
        else:
            a = -3
        s = v * t +  a * (t ** 2)
        v = v + a * t
        #当速度小于0的时候给距离赋值1，不然会四循环的
        if round(s)<=0:
            s=1
        current += s
        forward_tracks.append(round(s))
    # 反着滑动到准确位置
    back_tracks = [-3,-3,-4,-4,-3,-3]
    return {'forward_tracks': forward_tracks, 'back_tracks': back_tracks}


def main():
    driver = webdriver.Chrome()
    driver.get('https://passport.bilibili.com/login')
    time.sleep(3)
    driver.find_element_by_id('login-username').send_keys('18206106822')

    driver.find_element_by_id('login-passwd').send_keys('110120xx')

    # 1、出现滑块验证，获取有缺口的图片
    # driver.find_element_by_xpath('//*[@id="captcha"]/div[2]/div[2]/div[1]/div[3]/span[1]').click()
    driver.find_element_by_xpath('//a[@class="btn btn-login"]').click()
    time.sleep(3)

    picture1 = get_image(driver, '1')

    # 2、执行js改变css样式，显示背景图！！！！！重点是这一步！
    # driver.execute_script('document.querySelectorAll("canvas")[1].style=""')  # 不是1
    driver.execute_script('document.querySelectorAll("canvas")[3].style=""')
    time.sleep(2)
    # 3、获取没有缺口的图片
    picture2 = get_image(driver, '2')
    # 4、对比两种图片的像素点，找出位移
    space = get_space(picture1, picture2)
    tracks = get_tracks(space)
    button = driver.find_element_by_class_name('geetest_slider_button')
    ActionChains(driver).click_and_hold(button).perform()
    ActionChains(driver).move_by_offset(xoffset=100, yoffset=0).perform()
    ActionChains(driver).move_by_offset(xoffset=-100, yoffset=0).perform()
    ActionChains(driver).move_by_offset(xoffset=120, yoffset=0).perform()
    ActionChains(driver).move_by_offset(xoffset=-120, yoffset=0).perform()
    for track in tracks['forward_tracks']:
        ActionChains(driver).move_by_offset(xoffset=track, yoffset=0).perform()

    for back_track in tracks['back_tracks']:
        ActionChains(driver).move_by_offset(xoffset=back_track, yoffset=0).perform()
    ActionChains(driver).move_by_offset(xoffset=-3, yoffset=0).perform()
    ActionChains(driver).move_by_offset(xoffset=3, yoffset=0).perform()
    time.sleep(0.5)
    ActionChains(driver).release().perform()
    time.sleep(3)
    driver.close()
    # driver.quit()


if __name__ == '__main__':
    main()