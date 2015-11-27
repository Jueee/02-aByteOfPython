#!/usr/bin/python
# Filename: try_except.py
# 还可以让try..catch块关联上一个else从句。当没有异常发生的时候，else从句将被执行。
import sys

try:
    s = input('Enter something --> ')
except EOFError:
    print ('\nWhy did you do an EOF on me?')
    sys.exit() # exit the program
except:
    print ('\nSome error/exception occurred.')
    # here, we are not exiting the program

print('Done')