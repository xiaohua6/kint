import asyncio
import time


now=lambda: time.time()

async def buy(item):
    await asyncio.sleep(2)
    return item

def callback(future):
    loop.stop()
start=now()
list1=['电脑','苹果','手机']
# 调用携程函数获取携程对象
# coroutine=buy('电脑')
loop=asyncio.get_event_loop()



def event_handler(future):
    if future:
        print("购买%s成功，开始玩游戏"%future.result())
        loop.stop()

    else:
        print('购买失败')


# 我发现我打字的苏苏好像变快乐一点啊

# 我要
# 获取默认的事件循环对象
for i in list1:

    # 根据携程对象创建task对象：注册事件event
    task=asyncio.Task(buy(i))

    task.add_done_callback(event_handler)

    loop.run_forever()

    # loop.run_until_complete(task)

    print(task)

print("耗时：",now()-start)