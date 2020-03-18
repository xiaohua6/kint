import asyncio
import time


now=lambda: time.time()


def event_handler(future):
    if future:
        print("购买%s成功，开始玩游戏"%future.result())

    else:
        print('购买失败')


async def buy(item):
    await asyncio.sleep(2)
    return item


start=now()

# 调用携程函数获取携程对象
coroutine=buy('电脑')
# 获取默认的事件循环对象
loop=asyncio.get_event_loop()
# 根据携程对象创建task对象：注册事件event，下面三种方法的效果是相同的
# task=loop.create_task(coroutine)
# task=asyncio.ensure_future(coroutine)


task = asyncio.Task(coroutine)

task.add_done_callback(event_handler)
print(task)

loop.run_until_complete(task)
print(task)
print("耗时：",now()-start)