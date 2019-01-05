# -*- coding: UTF-8 -*-
# 日历
import calendar


cal = calendar.calendar(2019, l=0, c=5)
# print(cal)

# isleap : 判断某一年是否是闰年
print(calendar.isleap(2018))

# leapdays : 获取指定年份之间的闰年的个数
help(calendar.leapdays)
print(calendar.leapdays(1998, 2018))

# month() 获取某个月的日历字符串
print(calendar.month(2019, 2))

# monthrange() 获取一个月从周几开始和这个月的天数
# 格式: calendar.monthrange(年,月)
# 注意: 周默认0-6 表示周一到周天

print(calendar.monthrange(2019, 2))

w, t = calendar.monthrange(2019, 2)
print(w)
print(t)

# mothcalendar() 返回一个月的矩阵列表
# 格式:calendar.monthcalendar(年, 月)
# 返回值:耳机列表
# 注意: 矩阵中没有天数用0表示
m = calendar.monthcalendar(2019, 2)
print(m)

#  prcal : print calendar 直接打印日历
calendar.prcal(2018)


# prmonth(年,月) 打印月
calendar.prmonth(2018, 3)

# weekday() 获取周几

# 格式:calendar.weekday(年,月,日)
calendar.weekday(2018, 3, 26)


# ###########################################################################################################

# time 模块
#     时间戳
#         一个时间表示,根据不同语言,可以是整数或者浮点数
#         是从1970年1月1日0时0分0秒到现在经历的秒数
#         如果表示的时间是1970年以前或者太遥远的未来,可能出现异常
#         32位系统能够支持到2038年
#     UTC时间
#         UTC又称世界协调时间,以英国的格林泥治天文所在的地区作为参考时间,也叫世界标准时间
#         中国时间是 utc-8  东八区
#     夏令时
#         夏令时就是夏天的时候将时间调快一小时,本意是督促大家找谁早起节省蜡烛!每天变成25个小时,本质没变还是24个小时
#
#     时间元组
#         一个包含时间的普通元组
#
# 时间模块需要单独导入
import time
# 时间模块的属性
# timezone :当前时区和UTC时间相差的秒数,在没有夏令时的情况下的间隔,东八区的是-28800
# altzone  前时区和UTC时间相差的秒数,在有夏令时的情况下的间隔
# daylight 测当前是否是夏令时时间 状态,

print(time.timezone)
print(time.altzone)
print(time.daylight)


# 获取时间戳
print(time.time())
# 结果是浮点数 1546658064.5517719


# 获取当前时间
print(time.localtime())
# 结果:time.struct_time(tm_year=2019, tm_mon=1, tm_mday=4, tm_hour=17, tm_min=43, tm_sec=42, tm_wday=4, tm_yday=4, tm_isdst=0)

print(time.localtime().tm_hour)

# asctime() 返回元组的正常字符串化之后的时间格式
# 用法: time.asctime(时间元组)
# 返回值: 字符串

print(time.asctime(time.localtime()))

t = time.localtime()
tt = time.asctime(t)
print(tt)

# ctime : 获取字符串化的当前时间
print(time.ctime())

# mktime() 使用时间元组获取对应的时间戳
# 用法:time.mktime(时间元组)
# 返回值:浮点数时间戳

print(time.mktime(time.localtime()))

# clock : 获取cpu时间,3.0-3.3版本直接使用,3.6调用有问题
time.clock()
print(time.clock())

# sleep : 使程序进入睡眠状态  n秒后继续
time.sleep(1)

# strftime : 将时间元组转化成自定义的格式
'''
    %y 两位数的年份表示（00-99）
    %Y 四位数的年份表示（000-9999）
    %m 月份（01-12）
    %d 月内中的一天（0-31）
    %H 24小时制小时数（0-23）
    %I 12小时制小时数（01-12）
    %M 分钟数（00=59）
    %S 秒（00-59）
    %a 本地简化星期名称
    %A 本地完整星期名称
    %b 本地简化的月份名称
    %B 本地完整的月份名称
    %c 本地相应的日期表示和时间表示
    %j 年内的一天（001-366）
    %p 本地A.M.或P.M.的等价符
    %U 一年中的星期数（00-53）星期天为星期的开始
    %w 星期（0-6），星期天为星期的开始
    %W 一年中的星期数（00-53）星期一为星期的开始
    %x 本地相应的日期表示
    %X 本地相应的时间表示
    %Z 当前时区的名称
    %% %号本身
'''

# 把时间表示成,2019年1月4日 18:22
t = time.localtime(time.time())
ft = time.strftime('%Y-%m-%d %H:%M', t)
ftt = time.strftime('%Y{0}%m{1}%d{2}%H:%M').format('年', '月', '日')
print(ft)
print(ftt)

# datetime模块
#     datetime 提供日期和时间的运算和表示
#     datetime常见属性
#     datetime.date : 一个理想化的日期,提供
import datetime
print(datetime.date(2019, 1, 5))
# datetime.datetime
from datetime import datetime
# 常用类方法
#     today
#     now
#     utcnow
#     fromtimestamp: 从时间戳中返回本地时间
dt = datetime(2019, 1, 5)
print(dt.today())
print(dt.now())
print(dt.fromtimestamp(time.time()))

# datetime.timedelta 表示一个时间间隔

from datetime import datetime, timedelta

t1 = datetime.now()
print(t1.strftime("%Y-%m-%d  %H:%M:%S"))

# td表示以小时的时间长度
td = timedelta(hours=1)

# 当前时间加上时间间隔后,把得到的一个小时后的时间格式化输出
print((t1+td).strftime("%Y-%m-%d  %H:%M:%S"))

# timeit 时间测量工具

def p():
    time.sleep(3.6)
t2 = time.time()
p()
print(time.time() - t2 )



# ##############################################################################################################

# os 操作系统相关
#     跟操作系统相关,主要是文件操作
#     主要包含在三个模块里
#         os, 操作系统目录相关
#         os.path 系统路径相关操作
#         shutil 高级文件操作,目录树的操作,文件赋值,删除,移动.
# os 模块
#     getcwd() 获取当前的工作目录
#     格式:os.getcwd()
#     返回值:当前工作路径的字符串
#     当前工作目录就是程序都在进行文件相关操作,默认查找文件的目录
import os

print(os.getcwd())

    # chdir() 改变当前的工作目录
    # change directory
    # 格式:os.chdir('路径')
    # 返回值 : 无





