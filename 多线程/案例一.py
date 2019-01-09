# coding=utf-8
# 利用time函数，生成两个函数
# 顺序调用
# 计算总的运行使时间

import time
import _thread as thread


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
    print("我是参数:", arg, time.ctime())


# 带二个参数的线程调用
def loop4(arg1, arg2):
    print("我是参数1:", arg1, "和参数2：", arg2, "---------", time.ctime())




def main():
    print('程序start time :', time.ctime())
    thread.start_new_thread(loop1, ())
    thread.start_new_thread(loop2, ())
    thread.start_new_thread(loop3, ("haha",))
    thread.start_new_thread(loop4, ("123", "456"))
    print('程序end time :', time.ctime())


if __name__ == '__main__':
    main()
    while True:
        time.sleep(1)
        # 退出线程
        thread.exit()
