# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import time
from scrapy import signals
from selenium import webdriver
from scrapy.http import HtmlResponse


class SeleniumMiddleware(object):

    def process_request(self, request, spider):
        if 'month=' in request.url:
            # _____________________基本设定___________________________
            CHROME_DRIVER_PATH = r'/usr/bin/chromedriver'
            PROXY = "http://127.0.0.1:8080"
            # _____________________启动参数___________________________
            options = webdriver.ChromeOptions()

            # options.add_argument("window-size=1024,768")
            # options.add_argument("--no-sandbox")
            # options.add_argument("--disable-gpu")
            # options.add_argument("--headless")

            # _____________________代理参数___________________________
            desired_capabilities = options.to_capabilities()
            desired_capabilities['acceptSslCerts'] = True
            desired_capabilities['acceptInsecureCerts'] = True
            desired_capabilities['proxy'] = {
                "httpProxy": PROXY,
                "ftpProxy": PROXY,
                "sslProxy": PROXY,
                "noProxy": None,
                "proxyType": "MANUAL",
                "class": "org.openqa.selenium.Proxy",
                "autodetect": False,
            }
            # _____________________启动浏览器___________________________
            driver = webdriver.Chrome(

                chrome_options=options,
                desired_capabilities=desired_capabilities,
            )


            url = request.url

            print(request.url)
            driver.get(url)

            time.sleep(3)
            data = driver.page_source
            driver.close()
            driver.quit()

            res = HtmlResponse(url=url, body=data, request=request, encoding='utf-8')

            return res

        # url = request.url


        # driver = webdriver.Chrome()
        # driver.get(url)
        # time.sleep(3)
        # data = driver.page_source
        #
        #
        # driver.close()
        #
        # res = HtmlResponse(url=url, body=data, request=request, encoding='utf-8')

        # return res


