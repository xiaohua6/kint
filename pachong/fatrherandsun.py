import multiprocessing

import time


def task():

    for i in range(5):
        print("任务正在执行中")

        time.sleep(2)




if __name__ == '__main__':
    task1=multiprocessing.Process(target=task)
    task1.daemon=True
    task1.start()


    time.sleep(3)
    print("over")
    exit()