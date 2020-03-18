

# import requests
#
#
# headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"}
#
# urls=['https://www.jianshu.com/p/bb6c7f9aa1ae','www.baidu.com','https://www.douban.com/']


# 实现了异步


# 通过补丁来替换python原有的库来让gevent来识别对应的io延迟操作
from gevent import monkey; monkey.patch_all()
import gevent
import requests
from datetime import datetime


def f(url,bb):
    print ('time: %s, GET: %s' % (datetime.now(), url),bb)
    resp = requests.get(url)
    print ('time: %s, %d bytes received from %s.' % (
        datetime.now(), len(resp.text), url))


gevent.joinall([
        gevent.spawn(f, 'https://www.python.org/','aa'),
        gevent.spawn(f, 'https://www.yahoo.com/','aa'),
        gevent.spawn(f, 'https://github.com','aa')])