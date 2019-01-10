# coding=utf-8
import threading


"""
    多线程导致全局变量乱套,共享变量出现问题
"""
n = 0
loop = 100000

def myadd():
    global n, loop
    for i in range(1, loop):
        n += 1

def myminu():
    global n, loop
    for i in range(1, loop):
        n -= 1

if __name__ == '__main__':
    # myadd()
    # print(n)
    # myminu()
    # print(n)
    print("starting.......{0}".format(n))
    t1 = threading.Thread(target=myadd, args=())
    t2 = threading.Thread(target=myminu, args=())

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("ending.......{0}".format(n))