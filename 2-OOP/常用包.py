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

