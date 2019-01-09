# Log
# logging
# longging模块提供模块级别的函数记录日志
# 包括四大组件

# 1：日志相关概念
#     日志
#     日志级别（level）
#     DEBUG
#     INFO
#     NOTICE
#     WARNING
#     ERROR
#     CRITICAL
#     ALERT
#     EMERGENCY

# IO操作---》不要频繁操作
# LOG的作用
#     调试
#     了解软件的运行情况
#     分析定位问题
#     日志信息
#         time：时间
#         地点：定位
#         level
#         内容
#     成熟的第三方日志
#         log4j
#         log4php
#         logging
#
# 2：logging 模块
# 日志级别
#     级别可自定义
#     DEBUG
#     INFO
#     WARNING
#     ERROR
#     CRITICAL
# 初始化写日志实例需要指定级别，只有级别等于或高于指定级别才被记录
# 使用方式
#   直接使用longging
#     logging四大组件直接定制

# 2.1：logging 模块级别的日志
#     使用以下几个函数
#         logging.debug(msg, *args, **kwargs)	创建一条严重级别为DEBUG的日志记录
#         logging.info(msg, *args, **kwargs)	创建一条严重级别为INFO的日志记录
#         logging.warning(msg, *args, **kwargs)	创建一条严重级别为WARNING的日志记录
#         logging.error(msg, *args, **kwargs)	创建一条严重级别为ERROR的日志记录
#         logging.critical(msg, *args, **kwargs)	创建一条严重级别为CRITICAL的日志记录
#         logging.log(level, *args, **kwargs)	创建一条严重级别为level的日志记录
#         logging.basicConfig(**kwargs)	对root logger进行一次性配置
#         logging.basicConfig(**kwargs)
#         只在第一次调用的时候起作用
#         不配置logger则使用默认值
#             输出：sys.stderr(标准错误输出)
#             级别：Warning
#             格式：lever：log_name:content

import logging


# 日志输出到一个文件中
# logging.basicConfig(filename="xingxing.log", level=logging.DEBUG)

# 日志格式化输出；
LOG_FORMAT = "%(asctime)s-----------%(levelname)s-----------%(message)s"
logging.basicConfig(filename="xingxing.log", level=logging.DEBUG, format=LOG_FORMAT)

'''
format参数：
    asctime	%(asctime)s	日志事件发生的时间--人类可读时间，如：2003-07-08 16:49:45,896
    created	%(created)f	日志事件发生的时间--时间戳，就是当时调用time.time()函数返回的值
    relativeCreated	%(relativeCreated)d	日志事件发生的时间相对于logging模块加载时间的相对毫秒数（目前还不知道干嘛用的）
    msecs	%(msecs)d	日志事件发生事件的毫秒部分
    levelname	%(levelname)s	该日志记录的文字形式的日志级别（'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'）
    levelno	%(levelno)s	该日志记录的数字形式的日志级别（10, 20, 30, 40, 50）
    name	%(name)s	所使用的日志器名称，默认是'root'，因为默认使用的是 rootLogger
    message	%(message)s	日志记录的文本内容，通过 msg % args计算得到的
    pathname	%(pathname)s	调用日志记录函数的源码文件的全路径
    filename	%(filename)s	pathname的文件名部分，包含文件后缀
    module	%(module)s	filename的名称部分，不包含后缀
    lineno	%(lineno)d	调用日志记录函数的源代码所在的行号
    funcName	%(funcName)s	调用日志记录函数的函数名
    process	%(process)d	进程ID
    processName	%(processName)s	进程名称，Python 3.1新增
    thread	%(thread)d	线程ID
    threadName	%(thread)s	线程名称
'''



logging.debug("This is a debug log.")
logging.info("This is a info log.")
logging.warning("This is a warning log.")
logging.error("This is a error log.")
logging.critical("This is a critical log.")
# 另一种写法


logging.log(logging.DEBUG, "This is a debug log.")
logging.log(logging.INFO, "This is a info log.")
logging.log(logging.WARNING, "This is a warning log.")
logging.log(logging.ERROR, "This is a error log.")
logging.log(logging.CRITICAL, "This is a critical log.")


'''
2.2 logging模块的处理流程
    四大组件
        日志器（logger）：产生日志的一个接口
        处理器（handler）：把产生的日志发送到相应的目的地
        过滤器（filter）：要更精细的控制哪些日志输出
        格式器（formatter）：对输出信息进行格式化
    
    logger
        产生一个日志
        操作
        Logger.setLevel()	设置日志器将会处理的日志消息的最低严重级别
        Logger.addHandler() 和 Logger.removeHandler()	为该logger对象添加 和 移除一个handler对象
        Logger.addFilter() 和 Logger.removeFilter()	为该logger对象添加 和 移除一个filter对象

后面还有。。。。。。。。。。。。。。。。。。。。。。。


'''




