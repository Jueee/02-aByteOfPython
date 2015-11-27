#!/usr/bin/python
# Filename: cat.py

import sys

def readfile(filename):
    '''Print a file to the standard output.'''
    f = file(filename)
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print(line,) # notice comma
    f.close()

print(sys.version)   # 安装的Python的版本信息
print(sys.version_info) # 提供一个更简单的方法来使你的程序具备Python版本要求功能。
print(sys.argv)      #用来获取命令行参数

# Script starts from here
if len(sys.argv) < 2:
    print('No action specified...')
    sys.exit()

if sys.argv[1].startswith('--'):
    option = sys.argv[1][2:]
    # fetch sys.argv[1] but without the first two characters
    if option == 'version':
        print('Version 1.2')
    elif option == 'help':
        print('''\
This program prints files to the standard output.
Any number of files can be specified.
Options include:
  --version : Prints the version number
  --help    : Display this help''')
    else:
        print('Unknown option.')
    sys.exit()
else:
    for filename in sys.argv[1:]:
        readfile(filename)