# coding=utf-8
import threading


"""
    多线程导致全局变量乱套,共享变量出现问题
"""
su = 0
loopsun = 100000


lock = threading.Lock()

def myadd():
    global su, loopsun
    for i in range(1, loopsun):
        lock.acquire()
        su += 1
        lock.release()

def myminu():
    global su, loopsun
    for i in range(1, loopsun):
        lock.acquire()
        su -= 1
        lock.release()

if __name__ == '__main__':
    # myadd()
    # print(su)
    # myminu()
    # print(su)
    print("starting.......{0}".format(su))
    t1 = threading.Thread(target=myadd, args=())
    t2 = threading.Thread(target=myminu, args=())

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("ending.......{0}".format(su))