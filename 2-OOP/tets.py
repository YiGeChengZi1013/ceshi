
# 导入模块的一种方法(当模块名 不允许导入时)  例如:001,002 5588
# import importlib
# haha = importlib.import_module("001")
#
# #模块别名
#
# import importlib as  p
# hehe = p.import_module("002")

# 导入模块中类或函数的方法
# from 模块名  import  类名,函数名

# 导入后不用使用别名
# from 模块名 import *
#
#
# if __name__ == '__main__':
# 获取路径列表

# import sys
# print(sys.path)
#
#
# for i in sys.path:
#     print(i)

# 添加搜索路径

# sys.path.append(dir)
# 模块的加载顺序
#
# 1 上搜索内存中已经加载好的模块
# 2 搜索python的内置模块
# 3 搜索sys.path路径

# 包
#     包是一种组织管理代码的方式,包里面存放的是模块
#     用于将模块包含在一起的文件夹就是包
#     自定义包结构
# 包导入的操作
#     import 包名
#     直接导入一个包 可以使用__init__.py中的内容。
#     直接使用方法
#         package_name.func_name
#         package_name.class_name.func_name()