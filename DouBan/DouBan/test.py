import time


class ProxyMiddleware(object):
    _instance = None


    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls,_time1=time.time()
        return cls._instance



    def cc(self):
        now_2=time.time()
        return now_2

c=ProxyMiddleware()
b=ProxyMiddleware()

print(c.now_1)
print(c.cc())
time.sleep(2)
print(b.now_1)
print(b.cc())

print(id(c))
print(id(b))