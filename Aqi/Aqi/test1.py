import time
from selenium import webdriver

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# _____________________基本设定___________________________
CHROME_DRIVER_PATH = r'/usr/bin/chromedriver'
PROXY = "http://127.0.0.1:8080"
# _____________________启动参数___________________________
options = webdriver.ChromeOptions()

options.add_argument("window-size=1024,768")
options.add_argument("--no-sandbox")
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
driver = webdriver.Chrome(   chrome_options=options,

    desired_capabilities=desired_capabilities,
)
# driver = webdriver.Chrome( )
for i in range(1):




    driver.get('https://www.aqistudy.cn/historydata/daydata.php?city=%E4%BF%9D%E5%AE%9A&month=201406')

    time.sleep(500)

    driver.close()
    driver.quit()

