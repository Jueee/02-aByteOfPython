'''
os 模块包含普遍的操作系统功能。

它允许一个程序在编写后不需要任何改动，也不会发生任何问题，就可以在Linux和Windows下运行。
'''

import os

print(os.name)   # 指示你正在使用的平台。比如对于Windows，它是'nt'，而对于Linux/Unix用户，它是'posix'。

print(os.getcwd())  # 得到当前工作目录，即当前Python脚本工作的目录路径。

print(os.listdir()) # 返回指定目录下的所有文件和目录名

# os.remove()函数用来删除一个文件。
# os.system()函数用来运行shell命令。

#os.remove()函数用来删除一个文件。

print(os.linesep)  # 给出当前平台使用的行终止符。例如，Windows使用'\r\n'，Linux使用'\n'而Mac使用'\r'。

print(os.path.split('E:\\360\\Python\\PythonCode\\01Study\\02-aByteOfPython'))


print(os.path.isdir('E:\\360\\Python\\PythonCode\\01Study\\02-aByteOfPython'))  # 检验一个路径是否目录
print(os.path.isfile('E:\\360\\Python\\PythonCode\\01Study\\02-aByteOfPython')) # 检验一个路径是否文件

# 检验给出的路径是否真地存在
print(os.path.exists('E:\\360\\Python\\PythonCode\\01Study\\02-aByteOfPython')) 