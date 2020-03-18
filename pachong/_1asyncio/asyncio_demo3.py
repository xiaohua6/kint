# 把事件放在线程池中取执行

import asyncio
import time
import threading
import random

now=lambda: time.time()


def event_handler(future):
    print("event_handler:",threading.current_thread().name)
    if future:
        print("购买%s成功，开始玩游戏"%future.result())

    else:
        print('购买失败')


def buy(item):
    print("buy:",threading.current_thread().name)

    asyncio.sleep(random.randint(1,10))
    return item


start=now()


list1=['手机','电脑','汽车']
tasks=[]
for i in list1:

    # 获取默认的事件循环对象
    loop=asyncio.get_event_loop()

    future=loop.run_in_executor(None,buy,i)

    future.add_done_callback(event_handler)
    tasks.append(future)

# run_until_complete函数里面的参数只能传三种参数1个是携程对象2.是task对象3.是future对象,这里那就是把列表
# 通过asyncio.wait方法转化成future对象
loop.run_until_complete(asyncio.wait(tasks))
print(tasks)
print("耗时：",now()-start)