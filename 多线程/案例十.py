# encoding=utf-8
import threading
import time

import queue

queue = queue.Queue()

class Producer(threading.Thread):
    def run(self):
        global queue
        count = 0
        while True:
            # qsize返回queque内容长度
            if queue.qsize() < 1000:
                for i in range(100):
                    count += 1
                    msg = "生产产品" + str(count)
                    # put 是往queue中放入值
                    queue.put(msg)
                    print(msg)
            time.sleep(0.5)

class Consumer(threading.Thread):
    def run(self):
        global queue
        while True:
            # qsize返回queque内容长度
            if queue.qsize() > 100:
                for i in range(3):
                    # get是从queue中取出一个值
                    msg = self.name + "消费了" + queue.get()
                    print(msg)
            time.sleep(1)

if __name__ == '__main__':


    for i in range(100):
        queue.put("初始产品" + str(i))

    for i in range(2):
        p = Producer()
        p.start()

    for i in range(5):
        c = Consumer()
        c.start()