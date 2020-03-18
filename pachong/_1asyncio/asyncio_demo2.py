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


list1=['手机','电脑','汽车']
tasks=[]
for i in list1:
    # 调用携程函数获取携程对象
    coroutine=buy(i)
    # 获取默认的事件循环对象
    loop=asyncio.get_event_loop()
    # 根据携程对象创建task对象：注册事件event,下面三种方法的作用相同
    # task=loop.create_task(coroutine)
    # task=asyncio.ensure_future(coroutine)

    task=asyncio.Task(coroutine)
    task.add_done_callback(event_handler)
    tasks.append(task)



# run_until_complete函数里面的参数只能传三种参数1个是携程对象2.是task对象3.是future对象,这里那就是把列表
# 通过asyncio.wait方法转化成future对象
loop.run_until_complete(asyncio.wait(tasks))
print(tasks)
print("耗时：",now()-start)