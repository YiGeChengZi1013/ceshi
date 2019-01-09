# 多线程文章：
#     1.https://www.cnblogs.com/jokerbj/p/7460260.html
#     2.http://www.dabeaz.com/python/UnderstandingGIL.pdf

'''
多线程 VS 多进程
    程序：一堆代码以文本形式存入一个文档
    进程：程序运行的一个状态
        包含地址空间，内存，数据栈等
        每个进程由自己完全独立的运行环境，多进程共享数据是一个问题。

    线程：
        一个进程的独立运行片段，一个进程可以由多个线程
        轻量化的进程
        一个进程的多个线程间共享数据和上下文的运行环境
        共享互斥问题。

    全局解释器锁（GIL）
        python 代码的执行是由python虚拟机进行控制
        在主循环中有一个控制线程在执行

    python包
        thread : 有问题，不好用，python3 改成_thread
        threading:通行的包
        不使用线程：顺序执行，耗时比较长
        改用线程，缩短总时间，使用_thread
        多线程，传参数（单个参数和多个参数）

    threading的使用
        直接利用threading.thread 生成thread 实例
        1.t = threading.Thread(target = xxx, args = (xxx, ))
        2.t.start(): 启动多线程。
        3.t.join():等待多线程执行完成
        4.例子：案例二


'''

