# coding=utf-8
# 利用time函数，生成两个函数
# 顺序调用
# 计算总的运行使时间

import time

import threading


def loop1():
    print('start loop1 at', time.ctime())
    time.sleep(2)
    print('end loop1 at:', time.ctime())


def loop2():
    print('start loop2 at:', time.ctime())
    time.sleep(2)
    print('end loop2 at:', time.ctime())


# 带一个参数的线程调用
def loop3(arg):
    print("我是参数1:", arg, time.ctime())


# 带二个参数的线程调用
def loop4(arg1, arg2):
    print("我是参数2:", arg1, "和参数3：", arg2, "---------", time.ctime())




def main():
    print('程序start time :', time.ctime())
    t1 = threading.Thread(target=loop1, args=())
    t1.start()
    t2 = threading.Thread(target=loop2, args=())
    t2.start()
    t3 = threading.Thread(target=loop3, args=("ten", ))
    t3.start()
    t4 = threading.Thread(target=loop4, args=("nine", "jiu"))
    t4.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    print('程序end time :', time.ctime())


if __name__ == '__main__':
    main()
    while True:
        time.sleep(1)


