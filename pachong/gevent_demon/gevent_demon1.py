from gevent import greenlet
import gevent
from greenlet import greenlet

# gevent的猴子补丁来替换python的自带库，来识别其中的io操作
import gevent.monkey
gevent.monkey.patch_all()