import multiprocessing
import os

import time


def dance():
    print("dance",os.getpid())
    for i in range(5):
        print("正在跳舞中")
        time.sleep(1)

def sing():
    print("sing", os.getpid())
    for i in range(5):
        print("正在唱歌中")
        time.sleep(1)

if __name__ == '__main__':


    dance_process=multiprocessing.Process(target=dance)
    sing_process=multiprocessing.Process(target=sing)

    dance_process.start()
    dance_process.join()
    sing_process.start()


