# encoding=utf-8


import threading
import time

lock1 = threading.Lock()
lock2 = threading.Lock()


def func1():
    print("func1 starting .........")
    lock1.acquire()
    print("func1 申请了 lock1")
    time.sleep(2)
    print("func1 等待 lock2")
    lock2.acquire()
    print("func1 申请了lock2")

    lock2.release()
    print("func1 释放了 lock2")
    lock1.release()
    print("func1 释放了 lock1")
    print("func1 ending.........")

def func2():
    print("func2 starting .........")
    lock2.acquire()
    print("func2 申请了 lock2")
    time.sleep(4)
    print("func2 等待 lock1")
    lock2.acquire()
    print("func2 申请了lock1")

    lock1.release()
    print("func2 释放了 lock1")
    lock2.release()
    print("func2 释放了 lock2")
    print("func2 ending.........")

if __name__ == '__main__':
    print("程序启动..........")

    t1 = threading.Thread(target=func1, args=())
    t2 = threading.Thread(target=func2, args=())

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("程序结束...........")