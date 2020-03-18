# -*- coding: utf-8 -*-
# gevent中的锁
import gevent
from gevent.lock import Semaphore

sem = Semaphore(1)


def f1():
    for i in range(5):
        sem.acquire()
        print ('run f1, this is ', i)
        sem.release()
        gevent.sleep(1)




def f2():
    for i in range(10):
        sem.acquire()
        print ('run f2, that is ', i)
        sem.release()
        gevent.sleep(0.3)

t2 = gevent.spawn(f2)
t1 = gevent.spawn(f1)


gevent.joinall([t2,t1])