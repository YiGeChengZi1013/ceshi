# coding = utf-8

# 文件
#     长久保存信息的一种数据信息集合
#     常见操作:
#         打开关闭(文件一旦打开,需要关闭操作)
#         读写内容
#         查找
#
#
# open 函数
#     open函数负责打开文件,带有很多参数
#     第一个参数:必须有,文件的路径和文件名称
#     mode:表明文件用什么方式打开
#         r:以只读方式
#         w:写方式,会覆盖以前的内容
#         x:创建方式打开,如文件已经存在,会报错.
#         a:append方式,以追加的方式对文件内容进行写入
#         b:binary方式,二进制方式写入
#         t:文本方式打开
#         +:可读写


# 打开文件,用写的方式
# f称之为文件句柄
# r 表示后面字符串内容不需要转义
# f = open(r"test001.txt", 'w')
# 文件打开后必须关闭
# f.close()
# 如果以写方式打开文件,默认是如果没有文件,则会创建文件





# with语句
#     with语句使用的技术是一种成为上下文管理协议的技术
#     自动判断文件,作用域,自动关闭不在使用的打开的文件句柄
# 例子1:
with open(r"test001.txt",'r') as f:
    pass
    # 下面的语句块开始对文件f进行操作
    # 在本模块中不需要再使用close关闭文件f


# 例子2:

with open(r'test001.txt', 'r') as f:
    # 按行读取内容
    strline = f.readline()
    # 此结构保证能够完整读取文件直到结束
    while strline:
        print(strline)
        strline = f.readline()
print("*"*40)


# list能用打开的文件作为参数，把文件内每一行作为一个元素
with open(r'test001.txt', 'r') as f:
    l = list(f)
    for line in l:
        print(line)
print("*"*40)



# read是按照字符读取文件内容
# 允许输入参数决定读取几个字符，如果没有制定，重当前位置读取到结尾
# 否则，从当前位置读取指定个数字符
with open(r'test001.txt', 'r', ) as f:
    strchar = f.read()  # read()可以加参数n，  n表示读取n个字符
    print(len(strchar))
    print(strchar)
print("*"*40)

#
# # seek(offset ,from)
#     移动文件的读取位置，也叫指针
#     from的读取范围：
#         0：从文件头开始偏移
#         1：从文件当前位置开始偏移
#         2：从文件末尾开始偏移
#     移动的单位是字节（byte）
#     一个汉字由若干个字节构成
#     返回文件只针对当前位置

# 例子：打开文件后，从第5个字节开始读取
with open(r'test001.txt', 'r', ) as f:
    f.seek(6, 0)
    strch = f.read()
    print(strch)
print('*'*40)



# tell 函数：用来显示文件读写指针的当前位置

with open(r'test001.txt', 'r') as f :
    strcar = f.read(3)
    pos = f.tell()
    while strcar:
        print(pos)
        print(strcar)
        strcar = f.read(3)
        pos = f.tell()
print("*"*40)



# 文件的写操作-》write
#     write(str)：把字符串写入文件
#     write(str):把字符串按行写入文件
#     区别：
#         write函数参数只能是字符串
#         writelines参数可以是字符串，也可以是字符序列

# 例子1：
with open(r'test001.txt', 'a') as f:
    f.write("生活不仅眼前的苟且，\n 还有远方的苟且")


with open(r'test001.txt', 'a') as f:
    f.writelines("生活不仅眼前的苟且",)
    f.writelines("还有远方的苟且")
# 也可以下面代码：
# l = ["生活不仅眼前的苟且，", "还有远方的苟且"]
# f.writelines(l)


# pickle 序列化，落地
#     序列化：把程序运行小红的信息保存在磁盘上
#     反序列化：序列化的反过程
#     pickle：python提供的序列化模块
#     pickle.dump :序列化
#     pickle.load：反序列化

import pickle

age =20

with open(r'test002.txt', 'wb') as f:
    pickle.dump(age, f)


with open(r'test002.txt', 'rb') as f:
    age = pickle.load(f)
    print(age)
# ####################################################################################





# shelve---持久化
#     持久化工具
#     类似字典，用kv对保存数据，存储方式跟字典也类似
#     open ，close


import shelve
# 打开文件
# shv相当于一个字典
shv = shelve.open(r'shv.db')
shv['one'] = 1
shv['two'] = 2
shv['three'] = 3
shv.close()

# 以上例子说明 shelve自动创建的不仅仅是一个shv.db文件，还包括其他格式文件

# shevle 读取案例：

shv = shelve.open(r'shv.db')
print(shv['one'])
print(shv['three'])
shv.close()

# shelve 特性：
#     不支持多个应用并行写入，可以并行读
#         为了解决这个问题，open的时候可以使用flag=r
#     写回问题：
#         shelve默认情况下不会等待持久化对象进行任何修改
#         解决方法：强制写回 writeback = True


# shelve只读方式打开
shv1 = shelve.open(r'G:\PycharmProjects\TEST003\2-OOP\shv.db', flag='r')
try:
    k1 = shv1['one']
    print(k1)
finally:
    shv1.close()

#  shelve 忘记写回，shv.close()关闭，但内容还是在内存中，没有写回数据，需要强制写回:
# shv1 = shelve.open(r'G:\PycharmProjects\TEST003\2-OOP\shv.db', writeback=True)

# shelve 使用with(就不用使用closse关闭文件了。) 管理上下文环境：
with  shelve.open(r'G:\PycharmProjects\TEST003\2-OOP\shv.db', writeback=True) as shv:
    k1 = shv1['one']
    print(k1)























