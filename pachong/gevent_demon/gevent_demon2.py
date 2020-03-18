# -*- coding: utf-8 -*-

import gevent


def f1():
    for i in range(5):
        print ('run func: f1, index: %s ' % i)
        gevent.sleep(1)


def f2():
    for i in range(5):
        print ('run func: f2, index: %s ' % i)
        gevent.sleep(1)


t1 = gevent.spawn(f1)
t2 = gevent.spawn(f2)
gevent.joinall([t1, t2])