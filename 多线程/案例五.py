# coding=utf-8

import time
import threading

def fun():
    print("start fun", time.ctime())
    time.sleep(2)
    print("end fun", time.ctime())


print("main thread", time.ctime())

t1 = threading.Thread(target=fun, args=())
# 设置守护线程，，必须在start之前设置，否则无效
t1.setDaemon(True)

t1.start()

time.sleep(1)
print("main thread end", time.ctime())